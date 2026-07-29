#!/usr/bin/env python3
"""Reselling profit calculator — Depop / eBay / Poshmark / Mercari (US, 2026 fees).

Usage:
  python3 tools/profit_calc.py 45                          # net profit at $45 on all platforms
  python3 tools/profit_calc.py 45 --cogs 6 --packaging 0.5 # with your costs
  python3 tools/profit_calc.py 40 --boosted                # Depop boosted-listing scenario
  python3 tools/profit_calc.py --goal 100000 --asp 50      # sales/day needed for a profit goal

Fees verified July 2026 — re-verify quarterly (docs/01-market-analysis.md).
"""
import argparse

FEES = {
    # name: (percent_fee, fixed_fee)
    "Depop":    (0.033, 0.45),          # 0% commission + 3.3% + $0.45 processing (US)
    "eBay":     (0.1325, 0.30),         # typical clothing final value fee
    "Mercari":  (0.129, 0.50),          # ~10% selling + 2.9% processing
    "Poshmark": (0.20, 0.0),            # flat 20% on sales > $15
}
DEPOP_BOOST = 0.12  # US boosted-listing fee since March 2026, charged only on boosted sales


def net(price: float, pct: float, fixed: float, cogs: float, packaging: float,
        ship_cost: float, boost: float = 0.0) -> float:
    fees = price * (pct + boost) + fixed
    return price - fees - cogs - packaging - ship_cost


def main() -> None:
    p = argparse.ArgumentParser(description="Reselling profit calculator")
    p.add_argument("price", nargs="?", type=float, help="sale price in USD")
    p.add_argument("--cogs", type=float, default=7.0, help="item cost (default $7)")
    p.add_argument("--packaging", type=float, default=0.50, help="packaging cost (default $0.50)")
    p.add_argument("--shipping", type=float, default=0.0,
                   help="shipping cost YOU absorb (0 if buyer pays, default 0)")
    p.add_argument("--boosted", action="store_true", help="apply Depop 12%% boost fee")
    p.add_argument("--goal", type=float, help="annual net profit goal, e.g. 100000")
    p.add_argument("--asp", type=float, default=40.0, help="average sale price for goal math")
    args = p.parse_args()

    if args.goal:
        print(f"\n  GOAL: ${args.goal:,.0f}/yr net profit at ${args.asp:.0f} ASP "
              f"(COGS ${args.cogs:.2f})\n")
        print(f"  {'Platform':<10} {'Net/sale':>9} {'Sales/yr':>9} {'Sales/mo':>9} {'Sales/day':>10}")
        for name, (pct, fixed) in FEES.items():
            n = net(args.asp, pct, fixed, args.cogs, args.packaging, args.shipping)
            if n <= 0:
                print(f"  {name:<10} {'LOSS':>9}")
                continue
            yearly = args.goal / n
            print(f"  {name:<10} {'$%.2f' % n:>9} {yearly:>9,.0f} {yearly/12:>9,.0f} {yearly/365:>10.1f}")
        print("\n  (Cross-listing spreads this across platforms — the blended number is what matters.)\n")
        return

    if args.price is None:
        p.error("provide a sale price or --goal")

    print(f"\n  Sale price ${args.price:.2f} | COGS ${args.cogs:.2f} | "
          f"packaging ${args.packaging:.2f} | shipping absorbed ${args.shipping:.2f}\n")
    print(f"  {'Platform':<10} {'Fees':>8} {'Net profit':>11} {'Margin':>8}")
    for name, (pct, fixed) in FEES.items():
        boost = DEPOP_BOOST if (args.boosted and name == "Depop") else 0.0
        fees = args.price * (pct + boost) + fixed
        n = net(args.price, pct, fixed, args.cogs, args.packaging, args.shipping, boost)
        label = name + ("*" if boost else "")
        print(f"  {label:<10} {'$%.2f' % fees:>8} {'$%.2f' % n:>11} {n/args.price:>7.0%}")
    if args.boosted:
        print("\n  * Depop shown with 12% boosted-listing fee (charged only if boost causes sale)")
    print()


if __name__ == "__main__":
    main()
