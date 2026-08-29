# Cost Analysis

## The comparison

Two ways a BrainyFuture consultant can evaluate whether a client's AI use case is safe to build:
manual judgment alone, or manual judgment supported by Groundwork's Use Case Readiness diagnostic.

## Manual judgment, cost per engagement

A senior consultant reviewing a client's proposed AI use case, unaided, spends time researching the
regulatory landscape, checking for known failure patterns, and forming a defensible judgment. Based on
BrainyFuture's own billing structure, a senior consultant's time is valued at approximately €120–150 per
hour. A thorough manual readiness review, comparable in depth to the diagnosis Jane's case received,
realistically takes 2 to 4 hours: research, pattern-matching against known risks, drafting a
recommendation.

**Manual cost per engagement: roughly €240–600.**

This also does not standardize. Ten consultants, ten independent judgment calls, no shared record of
reasoning, nothing to hand a client as evidence of due diligence.

## With Groundwork's Use Case Readiness diagnostic

The diagnosis itself, as tested, takes under 40 seconds to run (39.05s in the live LangSmith trace) and
requires no consultant research time to produce a first-pass, source-cited readiness verdict. Consultant
time shifts from research and pattern-matching to review and client conversation, roughly 30 to 45
minutes to read the diagnostic report, verify it against the specific client context, and prepare a
recommendation.

**Assisted cost per engagement: roughly €60–110** (30–45 minutes of consultant time at €120–150/hour),
plus API costs for the diagnosis call itself (OpenAI Responses API with web search, a few cents to low
single-digit euros per run).

## Grounded assumption for time savings

Stanford HAI's 2026 AI Index measured productivity gains of 14 to 15 percent in customer-support-type
work from AI assistance. This project's own comparison, roughly 2 to 4 hours down to 30 to 45 minutes,
is a larger gain than that benchmark, which is expected: HAI's figure covers general customer-support
productivity broadly, while this comparison is for one narrow, structured task, use case diagnosis
specifically, where a tool can front-load the research entirely. The HAI figure is used here as a
conservative outside anchor, not as this project's own claimed number.

## Savings across ten consultants

At even a conservative 10 engagements diagnosed per month across the agency:

- Manual: 10 × ~€400 average = ~€4,000/month in consultant time
- Assisted: 10 × ~€85 average = ~€850/month in consultant time, plus minimal API cost

**Estimated monthly time-cost reduction: roughly €3,000–3,500**, before accounting for the harder-to-
price value of standardized judgment across all ten consultants and a documented, source-cited record
for every engagement.

## Assumptions, stated plainly

- Consultant hourly rate (€120–150) is an estimate based on typical mid-size AI consulting agency
  rates, not BrainyFuture's confirmed rate card.
- Manual review time (2–4 hours) is estimated from the depth of research visible in the live diagnostic
  trace, not from a timed observation of an actual BrainyFuture consultant.
- 10 engagements/month is a placeholder volume assumption for a 10-consultant agency, not a measured
  figure.
- These are Round 1 estimates for a pitch-level conversation, not audited figures. Round 2's ROI
  assessment will refine these with tighter assumptions and a formal 12/36-month projection.
