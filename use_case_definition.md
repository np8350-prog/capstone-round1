# Use Case Definition

## Business Problem Statement

Jane's company handles loan complaints manually. Response times are slow, and consultants judge each AI opportunity by instinct instead of a shared standard. Jane also fears that any AI touching customer accounts could drift into unexplainable credit decisions, without anyone deciding that on purpose.

## Company Profile

- Industry: consumer lending fintech
- Size: mid-size
- Location: EU-based
- Current state: complaint handling is manual, no AI in the loop today. No standardized way to assess whether a proposed AI use case is safe to build.

## Proposed AI Solution and System Type

An AI system that drafts replies to customer complaints about loan payment delays. A human agent reviews and sends every draft, the AI never sends a reply on its own.

System type: assistive, human-in-the-loop text generation. Not a decision-making system, not a scoring system.

This use case is diagnosed first by Groundwork's Use Case Readiness tool, BrainyFuture's internal check that runs every client idea through a fixed six-failure-pattern framework before any build is recommended.

## Key Stakeholders and Interests

- Jane, CEO: wants faster complaint handling, without regulatory or reputational risk.
- Jane's support team: wants less manual drafting work, without losing control over what gets sent.
- Jane's customers: want fast, accurate replies, and to know when they are talking to an AI.
- Chleo, BrainyFuture CEO: wants a consistent, defensible standard applied across all ten consultants, not personal judgment case by case.
- BrainyFuture consultants: need a tool that gives them a clear verdict and evidence, not just a guess.

## Success Criteria

1. Complaint response time drops measurably, target is a defined percentage reduction once baseline data is collected, tracked before and after rollout.
2. Zero complaint replies sent without human review, tracked through the review log.

## Out-of-Scope Boundaries

- The AI does not assess creditworthiness, does not produce a credit score, and does not feed any underwriting or dispute-resolution decision. If this changes, the use case must be re-diagnosed under Annex III 5(b).
- The AI does not send replies without human review.
- The AI does not access data outside complaint text and account reference.

## Evolution from Round 1

Round 1 decision was KEEP, no change to industry, sector, or use case. Jane's complaint-handling scenario and the credit-decision explainability risk stayed the core problem.

One addition came from teacher feedback after the Round 1 presentation: an LLM-as-judge layer, checking whether Use Case Readiness's own verdict and evidence hold up, not just checking the client's use case. This is a new Round 2 build item, added to the locked scope, not a change to Jane's use case itself.