# Market Regime And TCO

Use this reference when timing, supply, or macro conditions may dominate the product decision.

## Trigger Categories

Always run market-regime analysis for:

- GPUs, CPUs, memory, SSDs, motherboards, power supplies, AI hardware
- phones, laptops, tablets, consoles, cameras
- cars, bikes, large appliances
- products affected by tariffs, subsidies, export controls, recalls, shortages, or platform transitions

## Market Regime Table

| Regime | Signals | Decision implication |
|---|---|---|
| Normal depreciation | Stock is broad, discounting visible, next-gen not imminent. | Waiting usually improves value. |
| Launch spike | MSRP cards rare, scalping, review units only, early defects. | Wait unless urgent or below threshold. |
| Structural shortage | Upstream capacity constrained, input costs rising, supplier lead times long. | Waiting may increase price; use threshold plan. |
| Demand shock | New use case absorbs supply, e.g. AI workloads for GPUs/memory. | Buy only if user benefits from the demand shock. |
| Policy shock | Tariffs, export controls, subsidy changes, regional SKU restrictions. | Verify region-specific price and warranty. |
| Replacement cliff | New generation, standard, socket, connector, software support change. | Avoid old stock unless deeply discounted. |

## GPU And AI Hardware Checklist

For GPUs and local AI hardware, include:

| Dimension | Check |
|---|---|
| VRAM fit | Target model sizes, quantization, context length, batch size, image/video workloads. |
| Utilization | Hours per week, bursty vs daily, production vs hobby. |
| Total build cost | GPU, PSU, 12V-2x6/ATX 3.x, case clearance, cooling, RAM, SSD, UPS, electricity. |
| Local vs cloud TCO | Cloud/rental hourly cost, expected usage, privacy, latency, setup overhead. |
| Market cycle | Street price vs MSRP, stock depth, memory/GDDR/HBM pressure, upcoming refresh. |
| Resale | Liquidity, depreciation, warranty transfer, mining/AI wear stigma. |
| Driver/software | CUDA, ROCm, framework support, known driver or firmware issues. |

## Wait-Risk Model

Do not say "wait" without stating what could go wrong with waiting.

| Wait benefit | Wait risk |
|---|---|
| Price may normalize. | Input costs may rise. |
| More retail reviews appear. | Stock may tighten. |
| Firmware defects may be fixed. | New tariffs or regional limits may hit. |
| New model may improve value. | Current alternatives may disappear or rise. |
| Used market may improve. | User loses productivity during the wait. |

## TCO Sketch

Use rough ranges if exact data is unavailable:

```text
net_cost = purchase_price + enabling_upgrades + operating_cost - expected_resale
cost_per_month = net_cost / expected_holding_months
cost_per_use_hour = net_cost / expected_use_hours
cloud_break_even_hours = net_cost / cloud_hourly_rate
```

For uncertain usage, recommend a rental/cloud trial before buying if the break-even point is high.

## Decision Threshold Template

```markdown
**价格阈值**
| Condition | Action |
|---|---|
| <= fair_value | Buy if fit is high. |
| fair_value to stretch_value | Buy only for high-utilization or urgent use. |
| > stretch_value | Do not buy; use fallback path. |

**等待风险**
- Upside:
- Downside:
- Trigger to re-evaluate:
```

## GPU Example Logic

For a flagship GPU:

- Gaming-only: favor lower tier unless the monitor workload truly needs flagship performance.
- AI hobby use: consider used previous-gen or cloud first.
- Daily local AI production: flagship can be rational if VRAM is the binding constraint and cloud break-even is reachable.
- Memory shortage or AI demand shock: waiting is not automatically better; use threshold prices and supply signals.
