# stockpredictor
Stock Prediction Web App In Python

This is a simple web app built with Streamlit to predict stock prices using historical data. The app fetches stock data using the Yahoo Finance API and displays it with an optional Simple Moving Average (SMA) overlay.

## Features

- Enter a stock ticker symbol (e.g., AAPL, TSLA, etc.).
- Choose the start and end date for the data range.
- Select the period for calculating the Simple Moving Average (SMA).
- Visualize the stock's historical close prices along with the SMA.

## Requirements

The following Python libraries are required to run the app:

- `streamlit`
- `yfinance`
- `pandas`
- `matplotlib`

You can install these dependencies by running:


pip install streamlit yfinance pandas matplotlib


## Running the App

### 1. Clone the Repository

Clone the repository to your local machine:


git clone <repository-url>
cd <repository-directory>


### 2. Set Up a Virtual Environment (Optional)

It's recommended to run the app in a virtual environment:

  python -m venv myenv
  .\myenv\Scripts\activate


### 3. Install Dependencies

Install the required Python libraries as stated above.


### 4. Run the App

Start the Streamlit app with the following command:


streamlit run stockpredictor.py


This will launch the app in your default browser. You'll be able to input a stock ticker symbol, select a date range, and visualize the stock's data along with the SMA.

### 5. App Interface

- Stock Ticker: Enter the stock symbol (e.g., AAPL, MSFT).
- Start Date: Choose the start date for historical data.
- End Date: Choose the end date for historical data.
- SMA Period: Select the period for calculating the Simple Moving Average.

### 6. Results

The app will display:

- A table with the latest stock data.
- A plot showing the stock's close prices along with the selected Simple Moving Average.
