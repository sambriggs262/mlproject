"""CLI entry point for stock prediction using ML.

Author: Sam Briggs
"""

from ml_utils import (
    fetch_stock_data,
    engineer_features,
    prepare_data,
    train_model,
    evaluate_model,
    predict_next_day
)

def main():
    ticker = input("Enter a stock ticker: ").upper()
    stock_df = fetch_stock_data(ticker)

    if stock_df.empty:
        print(
            f"Failed to fetch data for '{ticker}'. Please check the ticker symbol or try again later.")
        return

    stock_df = engineer_features(stock_df)

    if stock_df.empty:
        print("Insufficient data after feature engineering. Try a different ticker.")
        return

    x_train, x_test, y_train, y_test = prepare_data(stock_df)
    model = train_model(x_train, y_train)

    r2, mse = evaluate_model(model, x_test, y_test)
    print(f"R² Score: {r2:.4f}")
    print(f"Mean Squared Error: {mse:.4f}")

    next_day_price = predict_next_day(model, stock_df.iloc[-1])
    print(f"Predicted next-day closing price: ${next_day_price:.2f}")


if __name__ == "__main__":
    main()
