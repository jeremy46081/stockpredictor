import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def main():
    st.title("Stock Prediction Web App")

    st.sidebar.header("User Input")

    # Sidebar inputs
    ticker_symbol = st.sidebar.text_input("Enter Stock Ticker", "AAPL")
    start_date = st.sidebar.date_input("Start Date", datetime(2015, 1, 1))
    end_date = st.sidebar.date_input("End Date", datetime.today())

    sma_period = st.sidebar.slider("Simple Moving Average Period (Days)", 5, 100, 20)

    if start_date > end_date:
        st.error("Error: End date must fall after start date.")
    else:
        # Fetch data
        data = fetch_stock_data(ticker_symbol, start_date, end_date)

        if data is not None:
            # Display data
            st.subheader(f"Stock Data for {ticker_symbol.upper()}")
            st.write(data.tail())

            # Plot data
            plot_stock_data(data, sma_period, ticker_symbol)

@st.cache
def fetch_stock_data(ticker_symbol, start_date, end_date):
    try:
        stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)
        return stock_data
    except Exception as e:
        st.error(f"An error occurred while fetching data: {e}")
        return None

def plot_stock_data(data, sma_period, ticker_symbol):
    data["SMA"] = data["Close"].rolling(window=sma_period).mean()

    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data["Close"], label="Close Price", color="blue")
    plt.plot(data.index, data["SMA"], label=f"{sma_period}-Day SMA", color="orange")
    plt.title(f"{ticker_symbol.upper()} Stock Price with {sma_period}-Day SMA")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.grid()
    
    st.pyplot(plt)

if __name__ == "__main__":
    main()
