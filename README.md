# Capstone Round 1: BrainyFuture × Groundwork

**Campus ID:** project-5
**Author:** Nelly Pourmehr

## The pitch, in one line

BrainyFuture, a mid-size AI consulting agency, uses its own diagnostic platform, Groundwork, to check a
client's proposed AI use case against six documented failure patterns before recommending any build.
This repo is the Round 1 pitch package: research, a live dashboard, a working POC, and transparent
monitoring, built around one real client scenario.

**Lineage disclosure.** Platform Risk shipped in project3. This capstone extends Groundwork with two
new capabilities: Use Case Readiness applied to a live client scenario here in Round 1, and, in Round 2,
Fix Router plus incident-grounded evidence.

## The scenario

Chleo, CEO of BrainyFuture, is worried her ten consultants each judge AI risk differently. Jane, CEO of
a mid-size consumer lending fintech, wants AI help with slow, manual complaint handling, but is afraid
of unexplainable AI credit decisions. Full story: `research/sector_research.md`.

## What's in this repo

| Folder | Contents |
|---|---|
| `research/` | Sector research, opportunities/risks (incl. EU AI Act framing), three use cases |
| `dashboard/` | Tableau workbook (`dashboard.twbx`) built on the AI Incident Database, 4 views, documented and corroborated against MIT's independent AI Risk Initiative data |
| `n8n/` | Three-node POC: webhook → live Groundwork diagnosis call → clean summary. Documented with a real test run |
| `langsmith/` | Live tracing wired into Groundwork's own `/api/diagnose` route. Real trace screenshot and documentation |
| `cost_estimation/` | Manual vs. AI-assisted diagnosis cost comparison, rollout timeline, all assumptions stated |
| `feedback/` | `round1_decision.md`, completed after presenting to teaching staff |
| `data/` | Cleaned AI Incident Database export used for the dashboard |

## Why Tableau, not PowerBI

PowerBI Desktop does not run on Mac. Tableau Desktop is used instead, stated here and in the dashboard
documentation so the substitution is never a surprise to a grader.

## Data sources

- **AI Incident Database** (incidentdatabase.ai): primary dashboard dataset, 1,641 real documented AI
  incidents.
- **MIT AI Risk Initiative** (airisk.mit.edu): independent corroborating classification of the same
  underlying incidents, used to confirm two of the four dashboard views.
- **CFPB Consumer Complaint Database**: secondary, used only for realism inside Jane's worked example,
  not the primary dataset (both BrainyFuture and Jane's company are EU-based; the EU AI Act, not the
  CFPB, is the governing compliance frame — see `research/sector_research.md`).
- **Stanford HAI AI Index 2026**: cited for grounded cost/ROI assumptions, not charted directly.

## The result that anchors this pitch

Jane's use case, run through the live Use Case Readiness diagnostic, returned a **"Not ready"** verdict,
grounded in five real regulatory sources (CFPB complaint-handling rules, Federal Reserve compliance
guidance, Regulation X error-resolution timelines, and a real Wells Fargo servicing enforcement action).
Full trace: `langsmith/trace_screenshot.png`. This is the intended outcome, not a failed demo: it shows
the diagnostic catches real risk instead of approving every use case by default.

## Post-Presentation Fix

The Groundwork diagnostic endpoint failed to save reports in production during the Round 1 demo. Local filesystem writes do not persist on Vercel. Fixed by switching report-store.ts to Vercel Blob storage. put() replaces writeFile(). get() and list() replace readFile() and readdir(). The report is a JSON blob keyed by id, so the swap was close to drop-in. Postgres was considered and deferred. It is the right choice later, when the dashboard needs to query across many reports, not for single save/retrieve by id.

## Setup

This repo is documentation and evidence, not a runnable application. The diagnostic engine it calls
(Groundwork's Use Case Readiness module) lives in a separate private repository and is deployed at
`https://groundwork-nelly15.vercel.app`.

To inspect the dashboard: open `dashboard/dashboard.twbx` in Tableau Desktop.
To inspect the POC: see `n8n/workflow_documentation.md` and the redacted `n8n/workflow.json`.