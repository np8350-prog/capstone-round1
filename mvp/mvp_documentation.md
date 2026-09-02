# MVP Documentation

## What this MVP is

Groundwork is a working, deployed AI diagnostic platform. This isn't a mockup or a demo script, it's live software: real API calls, a real database, a real deployed backend, and error handling that was tested against actual failures during this build, not assumed.

A user can go to the live app, submit a real AI use case, and get back a genuine, evidence-grounded readiness report in under a few minutes, with two additional AI passes available on demand: a tool/build recommendation (Fix Router) and an independent quality check on the diagnosis itself (LLM-as-Judge).

## Where it runs

| Component | Tech | Hosted on |
|---|---|---|
| Frontend + API routes | Next.js (TypeScript) | Vercel |
| Vendor-risk research agent | Python, FastAPI, LangGraph | Railway |
| Vector search (RAG) | Pinecone | Pinecone Cloud |
| Report storage | Vercel Blob | Vercel |
| LLM calls | OpenAI Responses API | — |

Two repos:
- `groundwork-nelly15.vercel.app` — the product itself, repo: `np8350-prog/groundwork-workspace/Groundwork`
- `platform-risk-research-agent-production.up.railway.app` — the vendor-risk backend, repo: `np8350-prog/platform-risk-research-agent`

## Core AI capability, and proof each one actually runs

### 1. Use Case Readiness diagnostic
Takes a company, a use case description, jurisdiction, end user, current workflow, and optional evidence (tickets/logs). Returns a six-dimension scored report: verdict, disqualifiers, red flags, a fix-first recommendation, and a live web-search reality check.

**Proof it runs:** tested live via `curl` and through the UI against `http://localhost:3000/audit/readiness` and the deployed Vercel app. A real EU jurisdiction test correctly triggered an EU AI Act Annex III 5(b) disqualifier, citing real regulation text and real government guidance pulled via web search.

### 2. Platform Risk vendor diagnostic
Scores an AI vendor (e.g. Zapier, Eightfold AI) on six dimensions: data handling, vendor stability, incident history, community signal, compliance posture, integration risk.

**Proof it runs:** tested live against the Railway-hosted backend. A real request for vendor "Zapier" returned a full report in ~2m16s (down from 300+ seconds before the performance fix), including real disqualifiers, real cited sources, and three scored vendor alternatives.

### 3. Incident-Grounded Evidence
The Incident History dimension is grounded in a real, ingested database of 1,641 documented AI incidents (from the AI Incident Database), searched by semantic similarity, not keyword matching.

**Proof it runs:** a real query for "Eightfold AI" hiring-tool risk correctly retrieved a real, relevant incident ("Eightfold AI Hiring Tools Allegedly Secretly Scored Job Applicants") with a calculated confidence score, and that retrieval directly shaped the AI's written reasoning for that dimension.

### 4. Fix Router
Given a diagnosis's fix-first recommendation, returns 2-3 ranked suggestions: an existing tool, or a build shape (n8n vs. LangGraph), each with a stated confidence level and a real, checkable source.

**Proof it runs:** live tested against a real EU compliance fix-first task, returned the real European Commission AI Act Service Desk, a real named classifier tool (Conformy), and a correctly-reasoned LangGraph build recommendation, not fabricated tools.

### 5. LLM-as-Judge
A second, independent AI pass reviews a completed diagnostic report's own internal reasoning (not the client's use case), checking five specific things: pattern-reason consistency, evidence-claim consistency, verdict consistency, confidence calibration, and Fix Router suggestion quality. Every check is always shown, "clear" or "flagged," never silent.

**Proof it runs:** live tested against a real report. It correctly caught a real overclaiming issue, a Fix Router suggestion labeled "strong evidence" when its cited source only proved general product capability, not fitness for the client's specific compliance need.

## Basic error handling, built and tested

- **Diagnosis timeout, local**: Node's default 5-minute fetch timeout was hit and reproduced live; fixed with a custom `undici` dispatcher (`instrumentation.ts`) raising the local dev ceiling to 10 minutes.
- **Diagnosis timeout, production**: Vercel's Hobby plan hard-limits any function to 300 seconds. `maxDuration` raised to 300, paired with an `AbortController` that cancels at 290 seconds and returns a clean `504` response instead of a silent platform kill.
- **RAG retrieval failure**: both `retrieve_framework_context` and `retrieve_incident_matches` catch any Pinecone or embedding failure and return an empty result instead of crashing, the report still generates, just without that grounding.
- **LLM scoring failure**: each of Platform Risk's six dimension-scoring calls is independently wrapped; one failed call falls back to an honest "unverified, no signal found" pattern instead of losing the other five real scores.
- **Structured output validation**: every AI response (diagnosis, Fix Router, Judge) is validated against a strict JSON schema before being trusted; a malformed response returns a `502` with a clear error, never a corrupted report silently saved.
- **Backward compatibility**: newly added report fields (`checkedAreas`, `headline`, `steps`, `practicalNote`) default safely to empty/null when reading older, already-saved reports, confirmed by reproducing and fixing a real crash on an old report missing the new fields.

## Repo structure (Groundwork)
Groundwork/
├── app/
│ ├── api/
│ │ ├── diagnose/route.ts # Use Case Readiness
│ │ ├── modules/platform-risk/route.ts # Proxies to Railway agent
│ │ └── reports/[id]/
│ │ ├── alternatives/route.ts
│ │ ├── fix-router/route.ts
│ │ └── judge/route.ts
│ ├── audit/[module]/page.tsx
│ └── report/[id]/page.tsx
├── components/
│ ├── ReportView.tsx / ResultDashboard.tsx
│ ├── FixRouterCard.tsx
│ ├── JudgeCard.tsx
│ └── PrintReport.tsx
├── lib/
│ ├── prompts/ (readiness.ts, fixRouter.ts, judge.ts)
│ ├── report-store.ts / fix-router-store.ts / judge-store.ts
│ └── types.ts
├── instrumentation.ts
├── requirements.txt # n/a — this repo is Node; see package.json
└── .env.example


## Repo structure (platform-risk-research-agent)
platform-risk-research-agent/
├── agent/
│ ├── graph.py # LangGraph pipeline
│ ├── nodes.py # watchlist, research, retrieval, synthesis, finalize
│ └── state.py # Pydantic report schema
├── rag/
│ ├── retrieval.py # embeddings, Pinecone, ingestion
│ └── corpus_incidents/aiid_dashboard_source.csv
├── backend/app.py # FastAPI entrypoint
├── requirements.txt
└── .env.example


## Running it locally

```bash
# Groundwork
cd Groundwork
npm install
npm run dev
# → http://localhost:3000

# platform-risk-research-agent
cd platform-risk-research-agent
pip install -r requirements.txt --break-system-packages
python run_incident_ingest.py   # one-time, ingests the incident corpus
uvicorn backend.app:app --reload
```

Both `.env.example` files list the required keys: `OPENAI_API_KEY`, `PINECONE_API_KEY`, `AI_GATEWAY_API_KEY`.

## Known limitations

- Diagnosis time is genuinely variable (roughly 1-5 minutes), driven by how much web research and reasoning the model decides a given use case needs, not a fixed number.
- Vercel Hobby's 300-second hard limit is a real ceiling on production; an unusually complex diagnosis could still time out in production even with the fix, only a plan upgrade removes that ceiling entirely.
- Incident-Grounded Evidence is limited to whatever the AI Incident Database contains as of ingestion; it isn't re-fetched automatically on a schedule.