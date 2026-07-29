# RESELL OS — The Depop & Multi-Platform Reselling Operating System

A complete, data-driven business system for building a six-figure reselling operation,
anchored on Depop and cross-listed to eBay, Poshmark, and Mercari.

**Built:** July 2026 · **Operator:** Maya · **System designed & maintained by:** Claude

---

## The one-paragraph thesis

The US secondhand apparel market grew ~4x faster than new-clothing retail in 2025 and online
resale is projected to nearly double to $48.3B by 2030. Depop now charges US sellers **0%
commission** (just 3.3% + $0.45 payment processing) — the best take-rate of any major
fashion marketplace. The sellers who make six figures are not lucky; they run a repeatable
system: cheap sourcing at $2–5/lb, disciplined curation into a recognizable brand, high-volume
listing (4–6 items/day), aggressive SEO + refresh cycles that feed the algorithm, and
cross-listing to 3+ platforms (which raises sell-through ~180%). This repo is that system,
written down, with the math checked.

## How to use this repo

Read in order. Each doc is a working playbook, not theory.

| # | File | What it is |
|---|------|-----------|
| 0 | [`docs/00-MASTER-PLAN.md`](docs/00-MASTER-PLAN.md) | The full business plan: model, unit economics, honest path to six figures |
| 1 | [`docs/01-market-analysis.md`](docs/01-market-analysis.md) | 2026 market assessment: size, growth, trends, fees, competition |
| 2 | [`docs/02-sourcing-playbook.md`](docs/02-sourcing-playbook.md) | Where to buy, what to buy, exact unit economics per channel |
| 3 | [`docs/03-listing-seo-playbook.md`](docs/03-listing-seo-playbook.md) | Photography, titles, tags, the Depop algorithm, refresh strategy |
| 4 | [`docs/04-pricing-and-profit.md`](docs/04-pricing-and-profit.md) | Pricing rules, offer strategy, markdown cadence, boost math |
| 5 | [`docs/05-operations-manual.md`](docs/05-operations-manual.md) | Daily/weekly workflows, shipping, customer service, KPIs |
| 6 | [`docs/06-scaling-roadmap.md`](docs/06-scaling-roadmap.md) | Month-by-month 12-month roadmap with revenue milestones |
| 7 | [`docs/07-brand-bible.md`](docs/07-brand-bible.md) | Shop identity, niche selection, social/content strategy |

### Tools

- **`tools/profit_calc.py`** — profit calculator: `python3 tools/profit_calc.py 45 --cogs 6 --shipping 4.50`
  computes exact net profit per sale on Depop/eBay/Poshmark/Mercari, and can back-solve
  "how many sales/month to hit a target income."
- **`tools/inventory_tracker.csv`** — the inventory ledger schema. Every item gets a SKU,
  cost, list date, and platform status. This file *is* the business's source of truth.
- **`templates/listing-template.md`** — copy-paste listing formula (title, description, tags).
- **`templates/weekly-review-template.md`** — the Sunday 30-minute business review.

## Division of labor

**Claude does:** market research, trend monitoring, pricing analysis, listing copy + SEO,
financial tracking/review, strategy updates, writing all content and social captions,
comp research ("what is this worth?").

**Maya does (the parts that physically require a human):** sourcing trips, photography,
shipping, the in-app actions Depop's terms require an account owner to do
(listing, offers, messages — paste Claude-prepared copy).

## The honest contract

Six-figure **revenue** is achievable in year one with full execution. Six-figure **profit**
typically takes 18–24 months and requires the scaling steps in doc 06 (higher average sale
price, cross-listing, and eventually outsourced fulfillment). Most Depop sellers make far
less — because they don't run a system. The plan in this repo is the system. Execution
volume is the variable.
