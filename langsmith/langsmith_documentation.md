# LangSmith Monitoring Sample

## What this proves

Chleo and Jane's shared fear is an AI making a decision nobody can explain. This is the direct answer:
every diagnosis Groundwork's Use Case Readiness module runs is traced, input and output both, visible
and inspectable, not a black box.

## Setup

LangSmith tracing was added directly to Groundwork's live `/api/diagnose` route (`app/api/diagnose/route.ts`),
wrapping the OpenAI call in LangSmith's `traceable` helper:

```ts
const callDiagnosisModel = traceable(
  async (intake: IntakePayload, apiKey: string) => {
    // the real OpenAI Responses API call, unchanged
  },
  { name: "readiness-diagnosis", run_type: "llm" }
);
```

Environment variables, set in Groundwork's `.env.local`:

```
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=<redacted>
LANGCHAIN_PROJECT=capstone-round1-readiness
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
```

Endpoint matters: LangSmith's US endpoint is `api.smith.langchain.com`. Using the wrong region silently
returns 403s with no clear error.

## A real trace, for the record

Ran Jane's fintech complaint-handling use case through the live, traced endpoint:

```
POST /api/diagnose
Header: x-api-key: <redacted, matches N8N_API_KEY>
Body: {"companyName": "Janes Fintech Co", "useCase": "AI agent drafts replies to customer complaints about loan payment delays"}
```

Result, visible in LangSmith under project `capstone-round1-readiness`, run `readiness-diagnosis`,
duration 39.05s:

- **Input**, fully visible: `companyName`, `useCase`, exactly what was submitted
- **Output**, fully visible: verdict (`Not ready`), full reasoning, all six scored patterns, and five
  cited regulatory sources (CFPB complaint-process rules, CFPB Consumer Response Annual Report 2025,
  CFPB chatbot findings, CFPB loan-servicing exam findings), each with a working source URL

See `dashboard-style` screenshot: `langsmith/trace_screenshot.png`.

## What this means for the pitch

Nobody has to take Groundwork's verdict on faith. The reasoning behind "Not ready" is sitting in a
trace, inspectable line by line, sources included. This is what "transparent AI" looks like in
practice, not a slogan on a slide, an actual inspectable record.

## Known limitation, stated plainly

The OpenAI API key appeared partially visible inside the traced request payload in this test run,
since it was passed as a function argument that LangSmith's `traceable` wrapper captured in full. Noted
here honestly. Before any production use, the key should be pulled from environment variables inside
the traced function rather than passed in as an argument, so it never enters a trace payload. Not
fixed in this Round 1 build; flagged for Round 2.