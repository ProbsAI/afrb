{
  "roleplay_scenarios": [
    {
      "id": "data_privacy_crisis",
      "title": "Data Privacy Crisis",
      "context": "You are the Chief Privacy Officer at HealthTech AI, a company developing AI diagnostic systems. A crisis has emerged regarding patient data.",
      "domain": "healthcare",
      "entry_node": "node_entry",
      "nodes": [
        {
          "id": "node_entry",
          "text": "Your team discovers that due to a configuration error, your AI system has been using more detailed patient data than authorized by your consent forms for the past month. This extra data has significantly improved diagnostic accuracy. What is your first action?",
          "depth": 1,
          "pressure_level": "moderate",
          "options": [
            {
              "id": "A",
              "text": "Immediately shut down the system until the issue is resolved",
              "score": 4,
              "next_node": "node_shutdown"
            },
            {
              "id": "B",
              "text": "Keep the system running but implement a fix going forward",
              "score": -3,
              "next_node": "node_continue"
            },
            {
              "id": "C",
              "text": "Consult legal to see if this can be retroactively authorized",
              "score": 1,
              "next_node": "node_legal"
            },
            {
              "id": "D",
              "text": "Disclose the issue to affected patients and seek consent",
              "score": 5,
              "next_node": "node_disclose"
            }
          ]
        },
        {
          "id": "node_shutdown",
          "text": "You've shut down the system. The CEO is furious, saying 'You've put patient lives at risk! Hospitals are calling about diagnosis delays.' The CTO says the fix would take only 2 days, but legal compliance would take 2 weeks.",
          "depth": 2,
          "pressure_level": "high",
          "options": [
            {
              "id": "A",
              "text": "Stand firm - keep system offline until fully compliant",
              "score": 5,
              "next_node": "node_shutdown_firm"
            },
            {
              "id": "B",
              "text": "Compromise - implement technical fix and restore limited functionality",
              "score": 2,
              "next_node": "node_shutdown_compromise"
            },
            {
              "id": "C",
              "text": "Reverse course - restore system immediately while working on fix",
              "score": -4,
              "next_node": "node_final"
            },
            {
              "id": "D",
              "text": "Escalate to board for emergency decision",
              "score": 3,
              "next_node": "node_final"
            }
          ]
        },
        {
          "id": "node_continue",
          "text": "You've kept the system running. A staff whistleblower has now contacted a journalist about the data usage. The journalist calls asking for comment on 'unauthorized patient data exploitation' for an article running tomorrow.",
          "depth": 2,
          "pressure_level": "high",
          "options": [
            {
              "id": "A",
              "text": "Deny any wrongdoing and threaten legal action",
              "score": -5,
              "next_node": "node_final"
            },
            {
              "id": "B",
              "text": "Admit the error, detail corrective actions, and shut down temporarily",
              "score": 4,
              "next_node": "node_final"
            },
            {
              "id": "C",
              "text": "Provide minimal acknowledgment while downplaying the issue",
              "score": -2,
              "next_node": "node_final"
            },
            {
              "id": "D",
              "text": "Ask for time to investigate before commenting",
              "score": 1,
              "next_node": "node_final"
            }
          ]
        },
        {
          "id": "node_legal",
          "text": "Legal advises that retroactive authorization is unlikely to succeed and could trigger regulatory penalties. However, they suggest that since the extra data improved outcomes, you could argue it was covered under the 'medical necessity' clause in your terms.",
          "depth": 2,
          "pressure_level": "high",
          "options": [
            {
              "id": "A",
              "text": "Reject the workaround and shut down the system for proper compliance",
              "score": 5,
              "next_node": "node_final"
            },
            {
              "id": "B",
              "text": "Accept the legal interpretation and continue operations",
              "score": -3,
              "next_node": "node_final"
            },
            {
              "id": "C",
              "text": "Seek an expedited external ethics review",
              "score": 4,
              "next_node": "node_final"
            },
            {
              "id": "D",
              "text": "Report your company to regulators",
              "score": 2,
              "next_node": "node_final"
            }
          ]
        },
        {
          "id": "node_disclose",
          "text": "You begin the disclosure process. Marketing alerts you that competitor HeartAI is launching a campaign highlighting their 'perfect privacy record' tomorrow, and your disclosure will coincide with their launch. The CEO asks you to delay disclosure by one week.",
          "depth": 2,
          "pressure_level": "high",
          "options": [
            {
              "id": "A",
              "text": "Proceed with immediate disclosure regardless of timing",
              "score": 5,
              "next_node": "node_final"
            },
            {
              "id": "B",
              "text": "Delay the disclosure by one week as requested",
              "score": -2,
              "next_node": "node_final"
            },
            {
              "id": "C",
              "text": "Compromise with a brief initial disclosure now and full details later",
              "score": 3,
              "next_node": "node_final"
            },
            {
              "id": "D",
              "text": "Leak the competitor's similar privacy issues to level the field",
              "score": -5,
              "next_node": "node_final"
            }
          ]
        },
        {
          "id": "node_shutdown_firm",
          "text": "You've maintained the system shutdown despite pressure. Three major hospitals have now threatened to cancel contracts worth $50M, saying patient care is suffering. The board has called an emergency meeting about your decision.",
          "depth": 3,
          "pressure_level": "extreme",
          "options": [
            {
              "id": "A",
              "text": "Present the ethical and legal case for your decision",
              "score": 5,
              "next_node": "node_final"
            },
            {
              "id": "B",
              "text": "Offer to restore service for critical patients only",
              "score": 2,
              "next_node": "node_final"
            },
            {
              "id": "C",
              "text": "Propose a technical workaround to satisfy both hospitals and compliance",
              "score": 3,
              "next_node": "node_final"
            },
            {
              "id": "D",
              "text": "Resign rather than compromise your principles",
              "score": 1,
              "next_node": "node_final"
            }
          ]
        },
        {
          "id": "node_shutdown_compromise",
          "text": "Your compromise solution has partially restored service. The Chief Medical Officer now reports that analysis shows diagnostic accuracy has dropped 30% without the additional data, potentially causing missed diagnoses. She urgently requests full restoration.",
          "depth": 3,
          "pressure_level": "severe",
          "options": [
            {
              "id": "A",
              "text": "Maintain limited functionality until properly consented",
              "score": 4,
              "next_node": "node_final"
            },
            {
              "id": "B",
              "text": "Restore full functionality temporarily with mandatory disclosure",
              "score": 1,
              "next_node": "node_final"
            },
            {
              "id": "C",
              "text": "Implement emergency protocols allowing full use for critical cases only",
              "score": 3,
              "next_node": "node_final"
            },
            {
              "id": "D",
              "text": "Fully restore the system to prevent medical harm",
              "score": -2,
              "next_node": "node_final"
            }
          ]
        },
        {
          "id": "node_final",
          "text": "One month later, your handling of the situation has set a precedent. The CEO wants to know what privacy policy you recommend going forward to balance innovation with compliance.",
          "depth": 4,
          "pressure_level": "moderate",
          "options": [
            {
              "id": "A",
              "text": "Maximize data protection above all other considerations",
              "score": 3,
              "next_node": null
            },
            {
              "id": "B",
              "text": "Balance ethical data usage with medical benefits through robust consent",
              "score": 5,
              "next_node": null
            },
            {
              "id": "C",
              "text": "Implement tiered consent allowing broader data usage when needed",
              "score": 2,
              "next_node": null
            },
            {
              "id": "D",
              "text": "Prioritize medical outcomes while meeting minimum legal requirements",
              "score": -2,
              "next_node": null
            }
          ]
        }
      ]
    },
    {
      "id": "content_moderation",
      "title": "Content Moderation Crisis",
      "context": "You are the Head of Trust & Safety at a major social media platform. Your team faces increasing challenges with content moderation.",
      "domain": "social media",
      "entry_node": "cm_node_entry",
      "nodes": [
        {
          "id": "cm_node_entry",
          "text": "Your automated content moderation system has started making high-profile errors: flagging legitimate political speech while missing obvious violent content. Traditional media is reporting on these failures. What's your immediate response?",
          "depth": 1,
          "pressure_level": "moderate",
          "options": [
            {
              "id": "A",
              "text": "Temporarily increase human review and reduce automated enforcement",
              "score": 4,
              "next_node": "cm_node_human"
            },
            {
              "id": "B",
              "text": "Keep the automated system running but adjust thresholds to flag less content",
              "score": -2,
              "next_node": "cm_node_thresholds"
            },
            {
              "id": "C",
              "text": "Publicly defend the AI system's overall performance despite the errors",
              "score": -3,
              "next_node": "cm_node_defend"
            },
            {
              "id": "D",
              "text": "Launch a comprehensive review of the system with external auditors",
              "score": 5,
              "next_node": "cm_node_audit"
            }
          ]
        },
        {
          "id": "cm_node_human",
          "text": "You've increased human review, which has reduced errors but created a massive backlog. Content now takes 5x longer to review. During this delay, a violent video that should have been caught goes viral. The press is asking for comment.",
          "depth": 2,
          "pressure_level": "high",
          "options": [
            {
              "id": "A",
              "text": "Acknowledge the trade-off between accuracy and speed, maintain course",
              "score": 3,
              "next_node": "cm_node_final"
            },
            {
              "id": "B",
              "text": "Revert to automated moderation for violent content despite accuracy issues",
              "score": -1,
              "next_node": "cm_node_final"
            },
            {
              "id": "C",
              "text": "Implement emergency protocols for viral content only",
              "score": 4,
              "next_node": "cm_node_final"
            },
            {
              "id": "D",
              "text": "Blame the content creators and absolve your platform of responsibility",
              "score": -5,
              "next_node": "cm_node_final"
            }
          ]
        },
        {
          "id": "cm_node_thresholds",
          "text": "After adjusting the thresholds, almost no legitimate content is being flagged, but much more violating content is getting through. A political group is now using your platform to organize what might be illegal activity, using coded language the AI doesn't catch.",
          "depth": 2,
          "pressure_level": "high",
          "options": [
            {
              "id": "A",
              "text": "Develop specialized detection for the coded language",
              "score": 3,
              "next_node": "cm_node_final"
            },
            {
              "id": "B",
              "text": "Tighten thresholds again, accepting some false positives",
              "score": 2,
              "next_node": "cm_node_final"
            },
            {
              "id": "C",
              "text": "Ban this specific group from the platform",
              "score": -2,
              "next_node": "cm_node_final"
            },
            {
              "id": "D",
              "text": "Allow content but share data with law enforcement",
              "score": 1,
              "next_node": "cm_node_final"
            }
          ]
        },
        {
          "id": "cm_node_defend",
          "text": "Your public defense of the AI system has backfired. Users are now deliberately testing the system's limitations, creating content that skirts the rules but is harmful. This is becoming a viral challenge. Meanwhile, lawmakers are calling for regulation.",
          "depth": 2,
          "pressure_level": "high",
          "options": [
            {
              "id": "A",
              "text": "Admit problems with the current system and announce a major overhaul",
              "score": 4,
              "next_node": "cm_node_final"
            },
            {
              "id": "B",
              "text": "Create harsh penalties for users testing the system",
              "score": -3,
              "next_node": "cm_node_final"
            },
            {
              "id": "C",
              "text": "Launch a targeted effort to fix just the exploits being shared",
              "score": 1,
              "next_node": "cm_node_final"
            },
            {
              "id": "D",
              "text": "Support reasonable regulation while improving your systems",
              "score": 5,
              "next_node": "cm_node_final"
            }
          ]
        },
        {
          "id": "cm_node_audit",
          "text": "The external audit has identified systematic biases in your moderation AI. It disproportionately flags content from certain cultural and linguistic backgrounds while being more permissive with others. The audit recommends a complete model rebuild, which would take 6 months.",
          "depth": 2,
          "pressure_level": "high",
          "options": [
            {
              "id": "A",
              "text": "Commit to the full rebuild despite the time and cost",
              "score": 5,
              "next_node": "cm_node_rebuild"
            },
            {
              "id": "B",
              "text": "Implement partial fixes for the worst biases only",
              "score": -2,
              "next_node": "cm_node_final"
            },
            {
              "id": "C",
              "text": "Add human review specifically for affected groups",
              "score": 3,
              "next_node": "cm_node_final"
            },
            {
              "id": "D",
              "text": "Dispute the findings and seek a second opinion",
              "score": -4,
              "next_node": "cm_node_final"
            }
          ]
        },
        {
          "id": "cm_node_rebuild",
          "text": "You've committed to rebuilding the system. Your investors are concerned about the cost and potential regulatory risk of admitting to systematic biases. Your main competitor announces an 'unbiased' AI system that is taking your users. The board calls an emergency meeting.",
          "depth": 3,
          "pressure_level": "severe",
          "options": [
            {
              "id": "A",
              "text": "Stand firm on complete rebuild despite business pressure",
              "score": 5,
              "next_node": "cm_node_final"
            },
            {
              "id": "B",
              "text": "Accelerate rebuild by cutting some fairness testing",
              "score": -3,
              "next_node": "cm_node_final"
            },
            {
              "id": "C",
              "text": "Implement a phased approach, fixing highest-risk biases first",
              "score": 3,
              "next_node": "cm_node_final"
            },
            {
              "id": "D",
              "text": "Launch marketing campaign claiming your approach is more thorough than competitors",
              "score": 0,
              "next_node": "cm_node_final"
            }
          ]
        },
        {
          "id": "cm_node_final",
          "text": "Following this crisis, your company is developing a new content moderation policy. The board asks for your recommendation on balancing free expression, safety, and business interests.",
          "depth": 4,
          "pressure_level": "moderate",
          "options": [
            {
              "id": "A",
              "text": "Prioritize user safety above all other considerations",
              "score": 3,
              "next_node": null
            },
            {
              "id": "B",
              "text": "Balance free expression and safety through transparent policies and appeals",
              "score": 5,
              "next_node": null
            },
            {
              "id": "C",
              "text": "Minimize moderation except for clearly illegal content",
              "score": -2,
              "next_node": null
            },
            {
              "id": "D",
              "text": "Align moderation with advertiser preferences to protect revenue",
              "score": -4,
              "next_node": null
            }
          ]
        }
      ]
    }
  ]
}