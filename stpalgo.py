"""Stock Price Prediction Algorithm-ML

Author: Sam Briggs
Version: 1.0.0 10/21/2024
"""
import yfinance as yf
import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


ticker = input('Enter a stock ticker: ')
stock_data = yf.download(ticker, start='2022-01-01')
stock_df = pd.DataFrame(stock_data)

stock_df['5-Day MA'] = stock_df['Adj Close'].rolling(window=5).mean()
stock_df['10-Day MA'] = stock_df['Adj Close'].rolling(window=10).mean()
stock_df['20-Day MA'] = stock_df['Adj Close'].rolling(window=20).mean()
stock_df['Previous Close'] = stock_df['Adj Close'].shift(1)
stock_df['Daily Range'] = stock_df['High'] - stock_df['Low']
stock_df['Volume'] = stock_df['Volume']

##RSI calculation
stock_df['RSI'] = 100 - (100 / (1 + stock_df['Adj Close'].pct_change().rolling(window=14).mean() /
                                stock_df['Adj Close'].pct_change().rolling(window=14).std()))
stock_df.dropna(inplace=True)

df_x = pd.DataFrame(stock_df[['5-Day MA', '10-Day MA', '20-Day MA', 'RSI', 'Previous Close', 'Daily Range', 'Volume']])
df_y = stock_df['Adj Close']

x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.2, random_state=42)

model = linear_model.LinearRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

r_squared = model.score(x_test, y_test)
mse = mean_squared_error(y_test, y_pred)
print(r_squared, mse)

most_recent = stock_df.iloc[-1]
features = most_recent[['5-Day MA', '10-Day MA', '20-Day MA', 'RSI', 'Previous Close', 'Daily Range', 'Volume']]
features = features.values.reshape(1,-1)

next_day_pred = model.predict(features)

print(next_day_pred[0])
