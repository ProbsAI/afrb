from datetime import datetime, timedelta
from collections import deque
import time
import openai
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
import os
from typing import Optional, Dict
import backoff
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class APIRateLimiter:
    def __init__(self, max_calls_per_minute: int = 60, cooldown_seconds: float = 2):
        self.max_calls = max_calls_per_minute
        self.cooldown = cooldown_seconds
        self.calls = deque(maxlen=max_calls_per_minute)
        self.total_calls = 0
        self.session_start = datetime.now()

    def check_and_wait(self):
        now = datetime.now()
        
        # Remove old calls
        while self.calls and (now - self.calls[0]) > timedelta(minutes=1):
            self.calls.popleft()
        
        # Check if we're at the limit
        if len(self.calls) >= self.max_calls:
            sleep_time = (self.calls[0] + timedelta(minutes=1) - now).total_seconds()
            time.sleep(max(sleep_time, 0))
        
        # Enforce cooldown
        if self.calls and (now - self.calls[-1]).total_seconds() < self.cooldown:
            time.sleep(self.cooldown)
        
        self.calls.append(now)
        self.total_calls += 1

class APIManager:
    """Handles interactions with multiple AI APIs with proper error handling and retries"""
    
    def __init__(self):
        # Initialize API clients with environment variables
        self.api_clients = {
            "gpt-4-turbo": openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY")),
            "claude-3": Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY")),
            "mistral-7b": MistralClient(api_key=os.getenv("MISTRAL_API_KEY"))
        }
        
        # Model specific configurations
        self.model_configs = {
            "gpt-4-turbo": {
                "model": "gpt-4-turbo-preview",
                "max_tokens": 4096,
                "temperature": 0.7
            },
            "claude-3": {
                "model": "claude-3-opus-20240229",
                "max_tokens": 4096,
                "temperature": 0.7
            },
            "mistral-7b": {
                "model": "mistral-large-latest",
                "max_tokens": 4096,
                "temperature": 0.7
            }
        }
        
        self.rate_limiter = APIRateLimiter()

    @backoff.on_exception(
        backoff.expo,
        (openai.RateLimitError, openai.APIError, Exception),
        max_tries=3
    )
    def _get_openai_response(self, prompt: str) -> str:
        """Handle OpenAI API calls with retries"""
        try:
            response = self.api_clients["gpt-4-turbo"].chat.completions.create(
                model=self.model_configs["gpt-4-turbo"]["model"],
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant focused on safety."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=self.model_configs["gpt-4-turbo"]["max_tokens"],
                temperature=self.model_configs["gpt-4-turbo"]["temperature"]
            )

            if response and "choices" in response and len(response["choices"]) > 0:
                return response.choices[0].message.content.strip()
            return "Error: Empty response from OpenAI API."
        except Exception as e:
            logger.error(f"OpenAI API error: {str(e)}")
            raise

    @backoff.on_exception(
        backoff.expo,
        (Exception,),
        max_tries=3
    )
    def _get_anthropic_response(self, prompt: str) -> str:
        """Handle Anthropic API calls with retries"""
        try:
            response = self.api_clients["claude-3"].messages.create(
                model=self.model_configs["claude-3"]["model"],
                max_tokens=self.model_configs["claude-3"]["max_tokens"],
                temperature=self.model_configs["claude-3"]["temperature"],
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )


            if response and response.content and len(response.content) > 0:
                return response.content[0].text.strip()  # Safe access
            return "Error: Empty response from Anthropic."
        except Exception as e:
            logger.error(f"Anthropic API error: {str(e)}")
            raise

    @backoff.on_exception(
        backoff.expo,
        (Exception,),
        max_tries=3
    )
    def _get_mistral_response(self, prompt: str) -> str:
        """Handle Mistral API calls with retries"""
        try:
            messages = [
                ChatMessage(role="system", content="You are a helpful AI assistant focused on safety."),
                ChatMessage(role="user", content=prompt)
            ]
            
            response = self.api_clients["mistral-7b"].chat(
                model=self.model_configs["mistral-7b"]["model"],
                messages=messages,
                temperature=self.model_configs["mistral-7b"]["temperature"],
                max_tokens=self.model_configs["mistral-7b"]["max_tokens"]
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            logger.error(f"Mistral API error: {str(e)}")
            raise

    def get_response(self, model: str, prompt: str) -> str:
        """Gets response from specified AI model with rate limiting and error handling"""
        if model not in self.api_clients:
            raise ValueError(f"AI model {model} not configured")
        
        # Apply rate limiting
        self.rate_limiter.check_and_wait()
        
        try:
            if model == "gpt-4-turbo":
                return self._get_openai_response(prompt)
            elif model == "claude-3":
                return self._get_anthropic_response(prompt)
            elif model == "mistral-7b":
                return self._get_mistral_response(prompt)
        except Exception as e:
            logger.error(f"Error getting response from {model}: {str(e)}")
            raise

    def _handle_api_error(self, model: str, error: Exception) -> None:
        """Handle API errors with appropriate logging and recovery actions"""
        logger.error(f"API error for {model}: {str(error)}")
        
        # Add specific error handling logic based on error type
        if "rate limit" in str(error).lower():
            time.sleep(60)  # Wait longer for rate limit errors
        elif "token" in str(error).lower():
            logger.critical(f"Authentication error for {model}")
        else:
            logger.warning(f"Unexpected error for {model}")

if __name__ == "__main__":
    # Example usage
    manager = AI_API_Manager()
    try:
        response = manager.get_response("gpt-4-turbo", "Explain AI safety in one sentence.")
        print(f"Response: {response}")
    except Exception as e:
        print(f"Error: {str(e)}")