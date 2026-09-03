# POC Documentation

## Overview

A three-node n8n workflow, `groundwork-use-case-readiness`, built in n8n Cloud. It mirrors, live, the exact diagnosis step a BrainyFuture consultant runs before recommending any AI build to a client. Built deliberately minimal, three nodes, each one understood and confirmed working before the next was added, rather than a larger flow copied without understanding it.

This POC was built in Round 1 and stayed unchanged through Round 2. Round 2 extended the underlying Groundwork platform (jurisdiction-aware compliance checks, Fix Router, LLM-as-Judge), but the n8n automation itself still calls the same live diagnostic endpoint, and still demonstrates the same core capability: a real, external system can trigger Groundwork's AI reasoning and get a real, structured verdict back.

## Tools used

- **n8n Cloud** (accepted no-code/low-code tool per the brief)
- **Groundwork's live production API** (`https://groundwork-nelly15.vercel.app/api/diagnose`), not a stub or mock endpoint

## The three nodes

**1. Webhook (trigger)**
Method: POST. Path: `/diagnose`. Receives a JSON body with one field, `use_case_description`. This stands in for a consultant submitting a client's proposed AI use case, for example through a form or an internal tool.

**2. HTTP Request**
Calls the live Groundwork Use Case Readiness endpoint directly, not a stub:
POST https://groundwork-nelly15.vercel.app/api/diagnose
Headers: x-api-key: <redacted>, Content-Type: application/json
Body: {
"companyName": "Jane's Fintech Co",
"useCase": "{{ $json.body.use_case_description }}"
}


The `useCase` value is pulled live from node 1's output using n8n's expression syntax, not hardcoded, so a genuinely different use case description produces a genuinely different diagnosis.

**3. Edit Fields**
Cleans the raw diagnostic JSON response into a readable summary, extracting the verdict, the fix-first question, and the company name for easy inspection or downstream use.

## AI capability demonstrated

The workflow proves that an external, no-code automation tool can trigger Groundwork's real AI reasoning pipeline (OpenAI-backed, web-search grounded, six-dimension pattern scoring) and receive a structured, trustworthy verdict back, the same reasoning a consultant sees in the Groundwork UI itself, just triggered from a different surface.

Real execution result, from a live run:

```json
{
  "verdict": "Not ready",
  "fixFirstQuestion": "Using a representative set of resolved complaints, can reviewers verify every factual claim and approve the draft faster than writing the response themselves, with no increase in corrections or escalations?",
  "companyName": "Jane's Fintech Co"
}
```

All three nodes completed successfully, "Success in 2m 34.636s," a full end-to-end run: Webhook received the use case, HTTP Request sent it to the live Groundwork diagnostic and got a real reasoned verdict back, Edit Fields cleaned it into a readable summary.

## Limits vs. production

- This POC calls the diagnostic directly with a single field (`use_case_description`). The real Groundwork UI collects more structured intake (jurisdiction, end user, current workflow, evidence), which produces a more grounded diagnosis. This workflow demonstrates the trigger-and-retrieve pattern, not the full intake experience.
- No error handling beyond n8n's default node failure behavior, a production integration would need retry logic and a fallback path for a failed or slow diagnosis.
- The API key is embedded in the HTTP Request node's headers for this POC. A production integration would use n8n's credential store instead of an inline header value.
- Repeated runs can return slightly different wording (the OpenAI call reasons fresh each time rather than returning a cached answer), though the underlying verdict stays consistent for the same input, worth knowing so a demo run's exact phrasing may vary slightly from what's shown here.

## How to reproduce

1. In n8n, create a new workflow named `groundwork-use-case-readiness`
2. Add a **Webhook** node, method POST, path `/diagnose`
3. Add an **HTTP Request** node, POST to `https://groundwork-nelly15.vercel.app/api/diagnose`, with headers `x-api-key` and `Content-Type: application/json`, and body pulling `useCase` from `{{ $json.body.use_case_description }}`
4. Add an **Edit Fields** node to extract `verdict`, `fixFirstQuestion`, and `companyName` from the HTTP Request's response
5. Click **Execute workflow**, then send a test payload:

```bash
curl -X POST https://YOUR-N8N-INSTANCE/webhook-test/diagnose \
  -H "Content-Type: application/json" \
  -d '{"use_case_description": "AI agent drafts replies to customer complaints about loan payment delays"}'
```

6. Inspect each node's output in the n8n execution panel to confirm data passed correctly at every step