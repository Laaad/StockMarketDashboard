import streamlit as st
from utility_functions import *
import plotly.graph_objects as go

#-- BOLIERPLATE --#
st.set_page_config(page_title="Stock Dashboard", layout="wide", page_icon="📈")
hide_menu_style = "<style> footer {visibility: hidden;} </style>"
st.markdown(hide_menu_style, unsafe_allow_html=True)

st.title("📈 Stock Dashboard")
popular_symbols = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA", "FB", "BRK-B", "V", "NVDA", "JPM"]
symbol = st.sidebar.selectbox("Select a stock symbol:", popular_symbols, index=2)
data = get_stock_data(symbol=symbol)
st.subheader("Candlestick Chart")
fig = go.Figure(data=[go.Candlestick(x=data.index,
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'])])
fig.update_layout(xaxis_rangeslider_visible=False)
st.plotly_chart(fig, use_container_width=True)

st.subheader("Summary")
st.dataframe(data.tail())

st.download_button("Download Stock Data Overview", data.to_csv(index=True), file_name=f"{symbol}_stock_data.csv", mime="text/csv")