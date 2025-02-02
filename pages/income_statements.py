import streamlit as st
from utilities.utlis import set_page
from utilities.stock_utils import getTickers
import yfinance as yf
import plotly.graph_objects as go

set_page('income statements','🏠')



stock_curr = st.session_state['selected_stock']
stock=yf.Ticker(stock_curr)



df=stock.income_stmt



important_metrics = [
    "Total Revenue", "Cost Of Revenue", "Gross Profit", "Operating Income", "Operating Expense",
    "EBIT", "EBITDA", "Net Income", "Diluted EPS", "Basic EPS", 'Operating Revenue',"Tax Provision", "Pretax Income"
]

df_filtered = df.loc[important_metrics]


st.write(f"### Profit & Loss Statement : {stock_curr} ")
st.write(df_filtered)

fig = go.Figure(data=[
    go.Bar(x=df_filtered.columns, y=df_filtered.loc["Total Revenue"], name="Total Revenue", marker=dict(color='blue')),
    go.Bar(x=df_filtered.columns, y=df_filtered.loc["Net Income"], name="Net Income", marker=dict(color='green')),
    go.Bar(x=df_filtered.columns, y=df_filtered.loc["Operating Income"], name="Operating Income", marker=dict(color='orange')),
    go.Bar(x=df_filtered.columns, y=df_filtered.loc["EBITDA"], name="EBITDA", marker=dict(color='yellow')),
])

fig.update_layout(
    title="Key Profit & Loss Metrics Overview",
    xaxis_title="Year",
    yaxis_title="Amount (INR)",
    barmode="group",  
    showlegend=True
)

st.plotly_chart(fig)



st.write(f"### Balance Sheet  : {stock_curr} ")

st.dataframe(stock.balance_sheet)

st.write(f"### Cash flow  : {stock_curr} ")
st.dataframe(stock.cash_flow)