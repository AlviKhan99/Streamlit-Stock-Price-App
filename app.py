#Import all modules:
import yfinance as yf
import streamlit as st

st.write("""
# Stock Price App

Displayed are the stock **opening price**, **closing price** and ***volume*** of APPLE!
""")


#define the ticker symbol
tickerSymbol = 'AAPL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2012-11-19', end='2022-11-19')
# Open	High	Low 	Close	Volume	Dividends	Stock Splits

st.write("""
## Opening Price
""")
st.line_chart(tickerDf.Open)

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)

st.write("""
## Volume
""")
st.line_chart(tickerDf.Volume)




