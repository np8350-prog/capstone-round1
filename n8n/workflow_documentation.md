# n8n Workflow Documentation

Workflow name: `groundwork-use-case-readiness`, built in n8n Cloud.

## What it does

A three-node workflow that mirrors, live, the diagnosis step a BrainyFuture consultant runs before
recommending any AI build to a client. Built deliberately small: three nodes, each one understood and
confirmed working before the next was added, rather than a larger flow copied without understanding it.

## Nodes

**1. Webhook (trigger).** Method: POST. Path: `/diagnose`. Receives a JSON body with one field,
`use_case_description`. This stands in for a consultant submitting a client's proposed AI use case, for
example through a form or an internal tool. Tested directly with curl from the terminal, confirmed the
payload lands correctly under `body.use_case_description` in the node's output.

**2. HTTP Request.** Calls the live Groundwork Use Case Readiness endpoint directly, not a stub:

```
POST https://groundwork-nelly15.vercel.app/api/diagnose
Headers: x-api-key: <redacted>, Content-Type: application/json
Body: { "companyName": "Jane's Fintech Co", "useCase": "{{ $json.body.use_case_description }}" }
```

The `useCase` value is pulled live from node 1's output using n8n expression syntax, not hardcoded. This
is a real call to Groundwork's live OpenAI Responses API diagnostic, with web search enabled, so it
takes up to two minutes to return. Timeout on this node is set to 150000ms to accommodate the route's
own 120-second cap.

**3. Edit Fields (Set node).** Reshapes the full `DiagnosticReport` response into a clean, readable
summary for logging: `verdict`, `summary` (or `fixFirstQuestion`), `companyName`. n8n's own Executions
tab retains the full input/output history for every run, which serves as the workflow's log, no
separate logging service was needed for this scope.

## A real run, for the record

Tested end to end with the following input:

> "AI agent drafts replies to customer complaints about loan payment delays"

Result:

```json
{
  "verdict": "Not ready",
  "fixFirstQuestion": "Using a representative set of resolved complaints, can reviewers verify every factual claim and approve the draft faster than writing the response themselves, with no increase in corrections or escalations?",
  "companyName": "Jane's Fintech Co"
}
```

The full diagnostic behind this verdict cited five real regulatory and enforcement sources (CFPB
complaint-handling rules, Federal Reserve compliance guidance, Regulation X error-resolution timelines,
and a real Wells Fargo servicing enforcement action) to argue that "drafting a reply" understates the
actual investigation, remediation, and accountability work a payment-delay complaint requires. A
"Not ready" verdict here is the intended outcome, not a failure of the demo: it demonstrates that the
diagnostic catches real risk rather than approving every use case by default.

## Credentials

The Groundwork API key (`x-api-key`) is stored directly in the HTTP Request node inside n8n, not in
this repository. No credentials or workflow exports containing the live key are committed here.

## Known limitations, stated plainly

- This flow was tested via n8n's test-webhook mode, not yet activated as a production webhook.
- The workflow calls Groundwork's real live diagnostic. It is not a stub, a decision made once the
  Groundwork endpoint's password-protection bypass (`x-api-key` header) was confirmed working.
- Node 3 logs to n8n's own Executions history rather than an external sheet or file, sufficient for
  this scope and rubric requirement.