# 09 — The AI Operating Loop (how luckypull out-executes everyone)

Every competitor is one person guessing. luckypull is one person **executing** while an AI
does 100% of the research, writing, pricing, and analysis. This doc is the standing contract
for who does what, on what trigger.

## The loop

```
SOURCE (Maya) → INTAKE SHEET (Maya, 60s/item) → COMP + PRICE + COPY (Claude, same day)
→ PASTE + LIST (Maya, 2 min/item) → OFFERS/REPLIES (Maya pastes Claude scripts)
→ SHIP <24h (Maya) → LEDGER (Maya logs) → WEEKLY ANALYSIS (Claude) → REVISED BUY LIST (Claude)
→ back to SOURCE, smarter every cycle
```

The compounding edge: every week the ledger teaches us what *actually* sells at *actual*
prices in *our* shop — and the buy list, pricing, and copy all update on that data. Solo
sellers never close this loop. We close it every Sunday.

## Claude's standing jobs (send the trigger, get the output)

| Trigger (what Maya sends) | Claude returns | Turnaround |
|---|---|---|
| Haul intake sheet | Price + title + description + full tags per item, paste-ready | Same day |
| "Comp this" + item details/photo description | Sold-comp research, conservative + target price, where to list it | Same day |
| Screenshot/summary of an offer or message | Exact reply script | Immediate |
| Sunday ledger (CSV or numbers) | Full KPI review vs roadmap, weakest-lever diagnosis, next week's buy list + markdown queue | Same day |
| "Content batch" | 5 TikTok/Reel scripts + captions + hooks from this week's real inventory | Same day |
| Monthly | Trend re-scan (Depop risers, fee changes, category rebalance) → docs updated in repo | Monthly |
| Anytime | Strategy questions, negotiation math, "should I buy this bale?" | Immediate |

## Maya's non-negotiables (the physical layer)

1. 4–6 listings pasted/day (from Claude's prepared queue — 10–15 min)
2. Ship <24h
3. Offers to likers daily (Claude's discount ladder: 10–15%, doc 04)
4. 2 photo shoots + 1–2 sourcing runs/week
5. Log every intake and sale in `tools/inventory_tracker.csv`
6. Sunday: send Claude the ledger

## Escalation rules

- Any single item that might comp >$75 → don't guess, send to Claude for deep comp first
- Any week revenue misses plan by >30% → mid-week strategy check, not just Sunday
- Any platform policy/fee change noticed → Claude re-verifies and updates docs 01/04
- Before any bulk buy >$150 → Claude runs the bale math (cost/lb → expected pickable % →
  landed cost/item → projected margin)

## Why this beats the competition

- **Speed:** listings written in minutes, not evenings → the 4–6/day quota never slips
- **Pricing accuracy:** every price is comp-based, never vibes → no money left on the table,
  no dead stock from overpricing
- **SEO depth:** every listing gets full keyword/tag treatment → the +15% search-rank edge
  on 100% of inventory, not the 10% a tired human optimizes
- **Closed feedback loop:** weekly data → revised buy list → better sourcing → better data
- **Zero burnout on the thinking layer:** Maya's hours go only where a human is required
```
