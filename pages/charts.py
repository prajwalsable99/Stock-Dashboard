import streamlit as st 
import plotly.graph_objects as go
import yfinance as yf
from utilities.utlis import set_page
import pandas_ta as ta    

set_page('Charts and History','📈')

st.write(f"### Selected Stock: **{st.session_state['selected_stock']}**")

def get_stock_data(stock, period):
    stock_data = yf.Ticker(stock)
    data = stock_data.history(period=period)


    if period != '1mo':
        data["MACD"] = ta.macd(data["Close"])["MACD_12_26_9"]
    
    data["MA30"] = ta.sma(data["Close"], length=30)

   
    data["RSI"] = ta.rsi(data["Close"], length=14)

    return data
def plot_candlestick_chart(df):
    fig = go.Figure(data=[go.Candlestick(x=df.index,
                                         open=df['Open'], high=df['High'],
                                         low=df['Low'], close=df['Close'],
                                         name='Candlestick')])
    fig.update_layout(title='Candlestick Chart and Indicators', xaxis_title='Date', yaxis_title='Price')
    st.plotly_chart(fig)
   


def plot_line_chart(df, indicators, period):
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines', name='Close Price'))

    if 'MA30' in indicators:
       
        fig.add_trace(go.Scatter(x=df.index, y=df['MA30'], mode='lines', name='MA30', line=dict(color='orange')))

    if 'RSI' in indicators:
        fig.add_trace(go.Scatter(x=df.index, y=df['RSI'], mode='lines', name='RSI', line=dict(color='purple')))

    if 'MACD' in indicators and period != '1mo':
        fig.add_trace(go.Scatter(x=df.index, y=df['MACD'], mode='lines', name='MACD', line=dict(color='blue')))
    
    fig.update_layout(title=f"{stock_symbol} Stock Price with Indicators", xaxis_title='Date', yaxis_title='Price')
    st.plotly_chart(fig)

st.title("Stock Analysis Dashboard")
 


stock_symbol = st.session_state['selected_stock']

time_range = st.selectbox("Select time range", ["1mo", "6mo", "1y", "3y", "10y"])

indicators = st.multiselect("Select Indicators", ["MA30", "RSI", "MACD"])




df = get_stock_data(stock_symbol, time_range)



plot_line_chart(df, indicators, time_range)
plot_candlestick_chart(df)