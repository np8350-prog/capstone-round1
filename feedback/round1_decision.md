# Round 1 Decision

## Feedback Summary

- Teaching staff confirmed the EU AI Act framing (Annex III 5(b)) fits the use case better than CFPB.
- The live n8n to Groundwork POC was seen as strong evidence of a working system, not just a mockup.
- Dashboard was scattered need an update,needed a single place. KPI tile and all section added post-feedback.
- Question raised on how Groundwork's judgment itself gets checked, not just the client's use case.
- Lineage from project3's Platform Risk to this capstone was clear and well documented.

## Decision

KEEP

No change to industry, sector, size, or use case. Jane's complaint-handling scenario stays as the worked example. The credit-decision explainability risk stays the core problem.

## What Changes for Round 2

The teacher feedback on checking Groundwork's own judgment quality becomes a new Round 2 item: an LLM-as-judge layer. It reviews a completed DiagnosticReport and scores whether the verdict and cited evidence actually hold up. This adds to the scope, it does not replace anything.

## Round 2 Priorities

1. EU AI Act and GDPR compliance documentation. Required deliverable, 30% of the Round 2 rubric combined.
2. Incident-Grounded Evidence. New Pinecone namespace, LangGraph retrieval step, matches use cases to real incidents.
3. Fix Router. Suggests existing tools or a build shape, confidence scored.
4. LLM-as-judge. Checks the reasoning quality of Use Case Readiness itself.

## First Idea for MVP Scope

Ship compliance docs first since they need no new infrastructure. Then build Incident-Grounded Evidence as the technical core, since Fix Router depends on the same DiagnosticReport extension. LLM-as-judge runs last or in parallel once the report structure is stable.