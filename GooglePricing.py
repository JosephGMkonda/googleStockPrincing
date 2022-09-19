import yfinance as yf
import streamlit as st
import pandas as pd

st.write(
    """
    # Google Stock pricing
    
    """
)

tickerSymbol = 'MSFT'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='id',start='2010-5-31', end='2020-5-31')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
st.line_chart(tickerDf.Open)
st.line_chart(tickerDf.Low)
st.line_chart(tickerDf.High)