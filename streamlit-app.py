import requests
import streamlit
import pandas as pd

def get_stock_data(symbol):

    API_KEY = streamlit.secrets['api']['api_key']

    url = f"https://api.marketstack.com/v1/eod?access_key={API_KEY}"

    querystring = {"symbols":symbol}

    response = requests.get(url, params=querystring)
    data_list = response.json()['data']

    if "error" in response:
        streamlit.error(f"Error:{response['error']}")

    stock_data = pd.DataFrame(data_list)
    stock_data['date'] = pd.to_datetime(stock_data['date'])
    stock_data.set_index('date', inplace=True)
    stock_data = stock_data[['open', 'high', 'low', 'close', 'volume']]
    stock_data.columns = ['Open', 'High', 'Low', 'Close', 'Volume']

    return stock_data