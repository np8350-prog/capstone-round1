# Use Cases — BrainyFuture x Jane's Consumer Lending Fintech

Three use cases, scoped for a medium consulting agency serving a medium fintech client. Each one is
justified against BrainyFuture's size and Jane's constraints, not generic AI capability.

## Use case 1: Diagnose a client's proposed AI use case before any build starts

**What it is.** Jane wants to automate complaint triage and response. Before any consultant recommends
a build, the use case runs through Groundwork's Use Case Readiness module, scored against six documented
AI failure patterns.

**Why it fits BrainyFuture's size.** Ten consultants, ten domains, no single senior reviewer can sit on
every engagement. A shared diagnostic step means every consultant applies the same standard, regardless
of who picks up the call.

**Why it fits Jane's fear.** Jane's stated concern is not "can AI help," it is "can I trust an
unexplainable decision with money and credit on the line." Diagnosis-before-build is the direct answer:
nothing gets recommended until it has been checked.

## Use case 2: Surface which failure pattern a use case matches, with reasoning shown

**What it is.** Rather than a pass/fail score, the diagnosis names which of the six failure patterns
applies to Jane's case and why, with the reasoning trace captured in LangSmith.

**Why it fits BrainyFuture's size.** A named, traceable failure pattern is something a consultant can
explain to a client without needing the platform's original author in the room. It scales expertise
instead of concentrating it.

**Why it fits Jane's fear.** This is the direct fix for the black-box problem. Jane does not need to
trust the platform blindly. She can see which specific risk was flagged and why.

## Use case 3: Give BrainyFuture leadership a live view of engagement risk across the agency

**What it is.** A dashboard view, for Chleo, showing risk patterns across engagements, grounded in the
AI Incident Database rather than internal data alone, since BrainyFuture does not yet have a large
internal engagement history to draw on.

**Why it fits BrainyFuture's size.** At ten consultants, Chleo cannot personally review every engagement.
A live, aggregate risk view lets her manage quality at the agency level instead of the individual level.

**Why it fits Jane's fear, indirectly.** It proves the audit-before-automate discipline is not
case-by-case improvisation. It is a standing practice Chleo can point to before Jane ever asks.

## Out of scope for Round 1

- Full incident-grounded evidence retrieval (Round 2 MVP scope, not built yet)
- Fix Router suggestion logic (Round 2 MVP scope, not built yet)
- Any live production data from Jane's company (public or synthetic data only, per project constraints)