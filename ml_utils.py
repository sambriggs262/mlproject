"""Helper functions for fetching data, feature engineering, model training, and prediction.

Author: Sam Briggs
"""

import yfinance as yf
import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


def fetch_stock_data(ticker, start_date='2022-01-01'):
    """Download stock data from Yahoo Finance."""
    stock_data = yf.download(ticker, start=start_date)
    return pd.DataFrame(stock_data)


def engineer_features(df):
    """Create technical indicators and features."""
    df['5-Day MA'] = df['Adj Close'].rolling(window=5).mean()
    df['10-Day MA'] = df['Adj Close'].rolling(window=10).mean()
    df['20-Day MA'] = df['Adj Close'].rolling(window=20).mean()
    df['Previous Close'] = df['Adj Close'].shift(1)
    df['Daily Range'] = df['High'] - df['Low']
    df['Volume'] = df['Volume']

    # RSI
    df['RSI'] = 100 - (100 / (1 + df['Adj Close'].pct_change().rolling(window=14).mean() /
                              df['Adj Close'].pct_change().rolling(window=14).std()))
    df.dropna(inplace=True)
    return df


def prepare_data(df):
    """Prepare feature matrix and target."""
    X = df[['5-Day MA', '10-Day MA', '20-Day MA', 'RSI', 'Previous Close', 'Daily Range', 'Volume']]
    y = df['Adj Close']
    return train_test_split(X, y, test_size=0.2, random_state=42)


def train_model(x_train, y_train):
    """Train linear regression model."""
    model = linear_model.LinearRegression()
    model.fit(x_train, y_train)
    return model


def evaluate_model(model, x_test, y_test):
    """Evaluate model performance."""
    r2 = model.score(x_test, y_test)
    mse = mean_squared_error(y_test, model.predict(x_test))
    return r2, mse


def predict_next_day(model, latest_row):
    """Make prediction for the next day based on most recent features."""
    features = latest_row[['5-Day MA', '10-Day MA', '20-Day MA',
                           'RSI', 'Previous Close', 'Daily Range', 'Volume']]
    return model.predict(features.values.reshape(1, -1))[0]
