import streamlit as st
from utility_functions import *
import plotly.graph_objects as go

#-- BOLIERPLATE --#
st.set_page_config(page_title="Stock Dashboard", layout="wide", page_icon="📈")
hide_menu_style = "<style> footer {visibility: hidden;} </style>"
st.markdown(hide_menu_style, unsafe_allow_html=True)

st.title("📈 Stock Dashboard")
popular_symbols = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA", "META", "BRK-B", "V", "NVDA", "JPM"]
symbol = st.sidebar.selectbox("Select a stock symbol:", popular_symbols, index=2)
data = get_stock_data(symbol=symbol)


price_difference, percentage_difference = calculate_price_difference(data)
latest_close_price = data.iloc[-1]["Close"]
max_52_week_high = data["High"].tail(252).max()
min_52_week_low = data["Low"].tail(252).min()

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Close Price", f"${latest_close_price:.2f}")
with col2:
    st.metric("Price Difference (YoY)", f"${price_difference:.2f}", f"{percentage_difference:+.2f}%")
with col3:
    st.metric("52-Week High", f"${max_52_week_high:.2f}")
with col4:
    st.metric("52-Week Low", f"${min_52_week_low:.2f}")

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