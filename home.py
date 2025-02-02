import streamlit as st
from utilities.utlis import set_page
from utilities.stock_utils import getTickers
import yfinance as yf

set_page('Home','🏠')


stocks=getTickers()


if "selected_stock" not in st.session_state:
    st.session_state["selected_stock"] = stocks[0]  # Default stock


with st.sidebar:
    st.title("📈 stocks.io")
    st.session_state["selected_stock"] = st.selectbox(
        "Choose a stock", stocks, 
        index=stocks.index(st.session_state["selected_stock"])
    )

    st.markdown("---")  

    st.subheader("📂 Pages")
    if st.button("Charts 📈"):
        st.switch_page("pages/charts.py")
    if st.button("News 📰"):
        st.switch_page("pages/news.py")
    if st.button("Financial St. 📰"):
        st.switch_page("pages/income_statements.py")
   
    




def get_stock_data(stock):
    return yf.Ticker(stock).info




stock_data = get_stock_data(st.session_state['selected_stock'])

st.title(f"{st.session_state['selected_stock']}")
st.write("---")




with st.popover("About",use_container_width=False):

        
        st.write(f"**Website**: {stock_data['website']}")
        st.write(f"**Industry**: {stock_data.get('industry', 'N/A')}")
        st.write(f"**Sector**: {stock_data.get('sector', 'N/A')}")

        st.subheader("Summary")
        st.markdown(stock_data.get('longBusinessSummary', 'N/A'))


        st.subheader("Contact Information")
        st.write(f"**Address 1**: {stock_data.get('address1', 'N/A')}")
        st.write(f"**City**: {stock_data.get('city', 'N/A')}")
        st.write(f"**ZIP Code**: {stock_data.get('zip', 'N/A')}")
        st.write(f"**Country**: {stock_data.get('country', 'N/A')}")
        st.write(f"**Phone**: {stock_data.get('phone', 'N/A')}")
        st.write(f"**Fax**: {stock_data.get('fax', 'N/A')}")
    








st.subheader("Key Financials")


col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Market Cap", f"₹{ round(stock_data.get('marketCap', 0) / 1e7 ,2)} Crores")
    st.metric("PE Ratio", f"{stock_data.get('trailingPE', 'N/A')}")
    st.metric("ROE (Return on Equity)", f"{stock_data.get('returnOnEquity', 'N/A')}")
    st.metric("Beta", f"{stock_data.get('beta', 'N/A')}")
    
with col2:
    st.metric("Current Price", f"₹{stock_data.get('currentPrice', 'N/A')}")
    st.metric("Book Value", f"₹{stock_data.get('bookValue', 'N/A')}")
    st.metric("Target Mean Price", f"₹{stock_data.get('targetMeanPrice', 'N/A')}")
    st.metric("Recommendation", 'Buy' if stock_data.get('recommendationMean', 0) < 2 else 'Hold/Sell')
    
with col3:
    st.metric("52 Week High", f"₹{stock_data.get('fiftyTwoWeekHigh', 'N/A')}")
    st.metric("52 Week Low", f"₹{stock_data.get('fiftyTwoWeekLow', 'N/A')}")
    st.metric("Dividend Yield", f"{stock_data.get('dividendYield', 0) * 100 if stock_data.get('dividendYield', 0) != 'N/A' else 'N/A'}%")
    







