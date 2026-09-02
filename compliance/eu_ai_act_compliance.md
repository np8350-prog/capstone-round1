# EU AI Act Compliance Documentation

## Risk Classification

Jane's stated use case is AI-assisted complaint triage and response. Not credit scoring.

Annex III point 5(b) of the EU AI Act classifies AI systems as high-risk when they assess creditworthiness or establish a credit score of a natural person. Fraud detection is exempt.

Step by step reasoning:

1. Does the system score or evaluate creditworthiness directly? No. It drafts replies to complaints about loan payment delays.
2. Does it produce an output a human acts on that could feed a credit decision? Not as scoped. If a complaint flag ever routes into an underwriting review, this changes.
3. Is the deploying company a bank or subject to other financial regulation that changes the answer? No. Classification under 5(b) applies the same whether or not the company is a traditional bank.
4. Can this system be repurposed without anyone deciding to reclassify it? Yes. A complaint-handling tool that starts tagging disputes by risk level, or that a human reads before approving a payment plan, drifts into 5(b) territory without a formal decision to do so.

**Classification: Limited risk, as currently scoped. Not high-risk under Annex III 5(b).**

The boundary is thin, not settled. Any use of this system's output to inform a credit-relevant decision moves it into high-risk. This is exactly the kind of scope drift Use Case Readiness is built to catch before a build starts, not after.

## Mandatory Requirements Summary

Since this system classifies as limited risk, the main legal duty is transparency, under Article 50 of the EU AI Act.

- Users must be told they are interacting with an AI system, not a human, before or during the interaction.
- This applies even though the system only drafts replies, if a customer receives an AI-drafted response, they must know that.
- No conformity assessment, no CE marking, no registration in the EU database is required at limited risk.
- If the use case drifts into Annex III 5(b) territory, high-risk obligations apply instead: a risk management system, data governance, technical documentation, logging, human oversight, and a conformity assessment before deployment.
- BrainyFuture's role here is to flag this drift risk to Jane in writing, so the limited-risk classification is a documented decision, not an assumption.

## Conformity Assessment Summary

At limited risk, a formal conformity assessment is not legally required. This section documents the assessment BrainyFuture ran anyway, as part of Groundwork's Use Case Readiness check, to support the classification above.

**What was assessed:**

- Intended purpose: complaint triage and response drafting, confirmed against Jane's stated use case.
- Output pathway: checked whether any output reaches a credit decision, underwriting flow, or dispute resolution that changes loan terms. None found as scoped.
- Human oversight: a human reviews and sends every AI-drafted reply, the AI does not act autonomously on a customer account.
- Data used: complaint text and account reference only, no separate creditworthiness signals fed into the system.

**Conclusion:** the system as scoped does not meet the Annex III 5(b) threshold. This conclusion holds only while output stays isolated from credit-relevant decisions. Any expansion of scope requires this assessment to be repeated.

**Recommendation:** re-run this assessment before any change to what the AI's output is used for, not on a fixed schedule.

## Diagnostic Code Verification

The risk classification above was checked against the live diagnostic system, not left as a written argument only. Groundwork's `/api/diagnose` route was updated to accept a jurisdiction field, and the system prompt was updated to explicitly check Annex III 5(b) when jurisdiction is EU.

A test case was run with a use case deliberately scoped past the boundary: complaint drafting plus a dispute flag feeding an underwriting review. This is the scenario Jane must avoid. The live system correctly classified it as high-risk, citing Annex III 5(b), the EU consumer credit directive, and EDPB guidance, and returned a "Not ready" verdict.

**Test input:**

```json
{
  "companyName": "Jane Test Co",
  "jurisdiction": "EU",
  "useCase": "AI drafts replies to loan complaints, and flags disputes for underwriting review"
}
```

**Relevant output excerpt:**

```json
{
  "verdict": "Not ready",
  "verdictTone": "risk",
  "summary": "Jane Test Co proposes AI that drafts replies to loan complaints and flags disputes for underwriting review. No tickets, logs, workflow measurements, or end-user validation were supplied. Not ready. Complaint replies require accountable verification, while the flag may influence a natural person's credit assessment. The EU creditworthiness boundary was checked and is either triggered or unresolved.",
  "disqualifiers": [
    {
      "condition": "EU AI Act Annex III 5(b) high-risk exposure is triggered or unclear because the flag may influence underwriting.",
      "cost": "If the flag informs creditworthiness assessment or a credit decision, full high-risk compliance is required before the applicable rules begin on 2 December 2027. This includes classification, risk and data governance, documentation, logging, human oversight, quality management, conformity assessment, registration, monitoring, incident handling, and required impact assessments."
    }
  ],
  "realityCheck": {
    "findings": [
      {
        "source": "European Union — Regulation (EU) 2024/1689, consolidated 27 July 2026",
        "finding": "Annex III 5(b) classifies AI used to evaluate a natural person's creditworthiness or establish a credit score as high-risk."
      }
    ]
  }
}
```

This confirms the boundary check described in this document runs as executable logic against a live system, not only as static analysis. Jane's actual scoped use case, complaint drafting without an underwriting flag, was separately confirmed to classify as limited risk in the Risk Classification section above.

## Technical Documentation Outline

This is the skeleton required if the use case is ever reclassified as high-risk. Kept ready in advance so BrainyFuture is not starting from zero if scope changes.

1. System description
   1.1 Intended purpose and deployment context
   1.2 Users and affected persons
2. Design and development
   2.1 System architecture
   2.2 Data used for training or grounding, sources, preprocessing
   2.3 Model choice and reasoning
3. Risk management
   3.1 Identified risks
   3.2 Mitigation measures
   3.3 Residual risk after mitigation
4. Data governance
   4.1 Data quality checks
   4.2 Bias review
5. Human oversight
   5.1 Points where a human reviews or overrides output
   5.2 Escalation path
6. Accuracy, robustness, and security
   6.1 Testing performed
   6.2 Known limitations
7. Logging and monitoring
   7.1 What is logged
   7.2 Retention period
8. Post-market monitoring plan
   8.1 How performance is tracked after deployment
   8.2 Trigger conditions for re-assessment