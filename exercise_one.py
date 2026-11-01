"""
File: exercise_one.py
------------------------
Description.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

revenue_2026 = 100
revenue_growth = 0.05
ebitda_margin = 0.20
depreciation = 4
capex = 6
delta_nwc = 1
tax_rate = 0.20
wacc = 0.09
terminal_growth = 0.02
net_debt = 15
asking_ev = 150

years = np.arange(2027, 2032)

# Part one: Financial forecasting

def forecast_financials(revenue_2026, revenue_growth, ebitda_margin,
                        depreciation, capex, delta_nwc, tax_rate):
    
    revenue_list = []
    ebitda_list = []
    ebit_list = []
    nopat_list = []
    fcff_list = []

    for i in range(len(years)): # The loop will run 5 times total, with i taking the values: 0, 1, 2, 3, 4.
        yearly_revenue = revenue_2026*(1+revenue_growth)**(i+1)
        revenue_list.append(yearly_revenue)

        yearly_ebitda = revenue_list[i]*ebitda_margin
        ebitda_list.append(yearly_ebitda)

        yearly_ebit = ebitda_list[i]-depreciation
        ebit_list.append(yearly_ebit)

        yearly_nopat = ebit_list[i]*(1-tax_rate)
        nopat_list.append(yearly_nopat)
        
        yearly_fcff = nopat_list[i] + depreciation - capex - delta_nwc
        fcff_list.append(yearly_fcff)


    table = pd.DataFrame(
    data={
        'Revenue': revenue_list,
        'EBITDA': ebitda_list,
        'EBIT' : ebit_list,
        'NOPAT' : nopat_list,
        'FCFF' : fcff_list
    }, 
    index=years
    )
    return table

forecast = forecast_financials(revenue_2026, revenue_growth, ebitda_margin, depreciation, capex, delta_nwc, tax_rate)
print(forecast)

# Part two: Discounted cash flow valuation
def calculate_dcf(forecast, wacc, terminal_growth, net_debt):
    
    fcff_present_value_list = []

    for i in range(len(forecast)):
        fcff_present_value_yearly = forecast["FCFF"].iloc[-1]/(1+wacc)**(i+1)
        fcff_present_value_list.append(fcff_present_value_yearly)

    terminal_value = forecast["FCFF"].iloc[-1]*(1+terminal_growth)/(wacc-terminal_growth)
    terminal_value_present_value = terminal_value/(1+wacc)**len(forecast)
    
    enterprise_value = sum(fcff_present_value_list) + terminal_value_present_value

    equity_value = enterprise_value - net_debt
    
    valuation_outputs = {
        "Terminal Value": terminal_value_present_value,
        "Enterprise Value": enterprise_value,
        "Equity Value": equity_value
        }
    return valuation_outputs

valuation_outputs = calculate_dcf(forecast, wacc, terminal_growth, net_debt)
print(valuation_outputs)