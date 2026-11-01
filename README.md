# Financial Scenario Simulator

**Corporate Finance · Financial Forecasting · DCF Valuation · Scenario Analysis**

A Python-based learning project that develops a financial forecasting and valuation model for a hypothetical Swiss manufacturing company. The objective is to evaluate whether a proposed acquisition price is supported by the company's projected free cash flows.

> **Project status:** Assignment / work in progress. The supplied Quarto document contains starter code and exercises, not a completed financial model or investment recommendation.

## Business case

Acting as a junior analyst at a Swiss corporate finance advisory firm, you are asked to assess a potential acquisition. The seller is seeking an **enterprise value of CHF 150 million**. The analysis uses a five-year forecast (2027–2031), a discounted cash flow (DCF) model, alternative operating scenarios, and a valuation sensitivity analysis.

All financial data are **hypothetical** and expressed in **CHF millions**.

### Base-case assumptions

| Parameter | Assumption |
| --- | ---: |
| Revenue (2026) | CHF 100m |
| Annual revenue growth | 5% |
| EBITDA margin | 20% |
| Annual depreciation and amortisation | CHF 4m |
| Annual capital expenditure | CHF 6m |
| Annual change in net working capital | CHF 1m |
| Corporate tax rate | 20% |
| WACC | 9% |
| Terminal growth rate | 2% |
| Net debt | CHF 15m |
| Seller's asking enterprise value | CHF 150m |

## Project objectives

1. **Financial forecasting:** Project revenue, EBITDA, EBIT, NOPAT, and unlevered free cash flow for 2027–2031.
2. **DCF valuation:** Discount forecast cash flows, estimate terminal value, and derive enterprise and equity values.
3. **Scenario analysis:** Compare bear, base, and bull cases and benchmark their valuations against the asking price.
4. **Sensitivity analysis:** Evaluate how changes in WACC and terminal growth affect enterprise value; visualise the results in a heatmap.
5. **Investment recommendation:** Summarise the valuation, key risks, due diligence priorities, and implications for acquisition negotiations.

**Optional extension:** Build an interactive simulator using Streamlit or Matplotlib controls.

## Tools

- **Python 3** — financial calculations and model logic
- **NumPy** — numerical operations
- **pandas** — financial forecast and scenario tables
- **Matplotlib** — charts and sensitivity heatmap
- **Quarto** — reproducible analytical report and HTML output
- **Streamlit** *(optional)* — interactive scenario inputs

## Repository structure

```text
financial-scenario-simulator/
├── README.md
├── Financial_Scenario_Simulator.qmd    # Editable Quarto assignment
└── Financial_Scenario_Simulator.html   # Rendered assignment
```

Additional scripts, data exports, or figures may be added as the project develops.

## Getting started

1. Install Python 3 and [Quarto](https://quarto.org/).
2. Install the required Python packages:

   ```bash
   python -m pip install numpy pandas matplotlib jupyter
   ```

3. Open `Financial_Scenario_Simulator.qmd` and complete the `TODO` sections.
4. Change each completed Python chunk from `#| eval: false` to `#| eval: true` (or remove that option) when it is ready to run.
5. Render the report:

   ```bash
   quarto render Financial_Scenario_Simulator.qmd --to html
   ```

The provided HTML is the **assignment handout**, not evidence that the financial calculations have been completed.

## Financial methodology

The model calculates free cash flow to the firm (FCFF) as:

$$
FCFF_t = EBIT_t(1-T) + D\&A_t - CapEx_t - \Delta NWC_t
$$

Enterprise value is estimated by discounting the explicit forecast cash flows and terminal value:

$$
EV = \sum_{t=1}^{5}\frac{FCFF_t}{(1+WACC)^t}
+ \frac{FCFF_5(1+g)}{(WACC-g)(1+WACC)^5}
$$

Equity value is then estimated as **enterprise value minus net debt**. The model assumes year-end cash flows and constant operating parameters within each scenario.

## Expected deliverables

- A reproducible five-year financial forecast
- A DCF valuation with enterprise and equity values
- Bear, base, and bull case comparisons
- A WACC-versus-terminal-growth sensitivity heatmap
- A concise investment recommendation supported by model results
- A rendered Quarto HTML report

## Learning outcomes

The project combines corporate finance concepts with practical Python skills: writing reusable functions, structuring financial data, checking assumptions, communicating uncertainty, and translating model outputs into an investment decision.

## Disclaimer

This is an educational project using fictional company data. It is not investment advice and should not be interpreted as a valuation of an actual business.
