# ROI and Risk Assessment

## Assumptions Table

| Assumption | Value | Basis |
|---|---|---|
| Complaints handled per month | 800 | Estimated mid-size lending fintech volume |
| Current manual time per complaint reply | 12 minutes | Includes reading, drafting, review |
| Time saved per reply with AI draft | 7 minutes | Human still reviews and edits, does not write from scratch |
| Support agent loaded hourly cost | 35 EUR | EU support role, salary plus overhead |
| Upfront build cost | 18,000 EUR | POC to production build, based on n8n plus LangGraph integration scope |
| Ongoing monthly cost | 900 EUR | Model API usage, hosting, monitoring |

These are planning assumptions, not confirmed figures. Replace with real numbers once Jane's company shares actual complaint volume and staff cost data.

## Upfront Costs

18,000 EUR. Covers diagnostic integration, AI draft system build, human review workflow, and testing.

## Ongoing Costs

900 EUR per month. Covers model usage, hosting, and monitoring.
10,800 EUR per year.

## Quantified Business Value

800 complaints per month, 7 minutes saved each, at 35 EUR per hour:

800 x 7 minutes = 5,600 minutes saved per month = 93.3 hours
93.3 hours x 35 EUR = 3,266 EUR saved per month
3,266 EUR x 12 = 39,192 EUR saved per year

## ROI Calculation

ROI = (Net Benefit / Total Cost) x 100

**12 months:**
Total cost = 18,000 + 10,800 = 28,800 EUR
Net benefit = 39,192 - 28,800 = 10,392 EUR
ROI = (10,392 / 28,800) x 100 = 36%

**36 months:**
Total cost = 18,000 + (10,800 x 3) = 50,400 EUR
Total value = 39,192 x 3 = 117,576 EUR
Net benefit = 117,576 - 50,400 = 67,176 EUR
ROI = (67,176 / 50,400) x 100 = 133%

## Break-Even Note

Monthly net gain after ongoing costs: 3,266 - 900 = 2,366 EUR.
Upfront cost of 18,000 EUR breaks even at roughly 8 months.

## Risk Matrix

| Risk | Category | Likelihood (1-5) | Impact (1-5) | Mitigation |
|---|---|---|---|---|
| Use case drifts into Annex III 5(b) high-risk territory without anyone deciding that | Regulatory | 2 | 5 | Fixed scope boundary, re-diagnosis required before any expansion, checked in `eu_ai_act_compliance.md` |
| AI draft contains wrong account or payment information | Technical | 3 | 3 | Mandatory human review before send, no auto-send |
| Customer not told they are interacting with AI-assisted content | Regulatory | 2 | 4 | Transparency notice required under Article 50, added to reply template |
| AI draft tone reads as dismissive or judgmental toward a financial hardship complaint | Ethical | 3 | 3 | Human review includes a tone check, not just fact check |
| Over-reliance on AI drafts reduces agent attention during review | Operational | 3 | 3 | Review workflow requires an explicit approve action, not passive accept |
| Model provider changes terms or starts using data for training without new consent | Regulatory | 2 | 4 | Vendor agreement confirmed in `gdpr_documentation.md`, checked before go-live |
| System downtime forces fallback to fully manual process | Operational | 2 | 2 | Manual process stays documented and ready, AI is additive not a replacement |

## Notes

These figures use placeholder assumptions. Before presenting to business judges, confirm actual complaint volume and staff cost with Jane's team if that data becomes available, and update this file.