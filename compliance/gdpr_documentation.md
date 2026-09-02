# GDPR Documentation

## Data Flow Map

1. Customer submits a complaint through the existing support channel (email or web form).
2. Complaint text and account reference number enter the AI system.
3. AI drafts a reply based on complaint text and account history.
4. Draft goes to a human agent for review.
5. Agent sends the final reply, or edits it first.
6. Complaint text, draft, and final reply are logged for quality review.

No credit score, income data, or underwriting data enters this flow. If that changes, this map and the risk classification in `eu_ai_act_compliance.md` both need to be redone.

## Processing Activities Register

| Activity | Purpose | Legal Basis | Retention | Recipients |
|---|---|---|---|---|
| Complaint text collection | Respond to customer complaint | Contract (Art 6(1)(b)), servicing the loan agreement | 6 years, matches financial record-keeping rules | Internal support team, AI draft system |
| AI-drafted reply generation | Speed up response time | Legitimate interest (Art 6(1)(f)), balanced against customer right to human review | Not stored beyond the complaint record above | Internal support team only |
| Account reference lookup | Match complaint to correct customer account | Contract (Art 6(1)(b)) | Same as complaint record | Internal support team, core banking system |
| Quality review logging | Improve AI draft accuracy over time | Legitimate interest (Art 6(1)(f)) | 12 months | Internal QA team only |

## DPIA: AI-Drafted Reply Generation

This is the highest-risk processing activity here, since it is the only step where an AI system produces content that reaches a customer, and where a low-quality or wrong draft could cause harm if sent without review.

**Nature of processing:** complaint text and account reference are read by the AI system to generate a draft reply. No new data is created about the customer beyond the draft itself.

**Necessity and proportionality:** draft generation is optional at the point of use, a human can always write the reply manually. The AI does not send anything without human review.

**Risks identified:**
- AI draft contains factually wrong account information. Mitigated by human review before send.
- AI draft interprets a payment delay complaint in a way that reads as a credit judgment. Mitigated by keeping AI scope to reply drafting only, not decision-making.
- Complaint data used to train or fine-tune a model without separate consent. Mitigated by confirming with the AI vendor that no customer data is used for model training.

**Residual risk:** low, conditional on human review staying mandatory and the AI never bypassing that step.

**Conclusion:** proceed, with human review as a fixed control, not optional.

## Data Subject Rights Support

- Access: customer can request a copy of their complaint record and any AI-drafted reply tied to it.
- Rectification: customer can request correction of wrong account information used in a draft.
- Erasure: subject to retention rules above, complaint records tied to an active loan cannot be erased early, this is disclosed to the customer.
- Objection: customer can request a human-only reply process, opting out of AI drafting entirely, at any time.
- The AI-drafted reply is not an automated decision under Article 22, since a human reviews and can override it before anything is sent.

## Third-Party and Cross-Border Transfers

- The AI model provider is the only third party in this flow.
- If the AI vendor processes data outside the EU, a transfer mechanism (Standard Contractual Clauses or an adequacy decision) must be confirmed and documented before go-live.
- No other third party receives complaint or account data in this flow.
- This section must be updated with the actual vendor and hosting location once BrainyFuture and Jane confirm the production AI provider.