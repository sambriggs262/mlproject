# MarketModel – Stock Price Prediction with Machine Learning

**MarketModel** is a simple machine learning project that predicts a stock’s next-day adjusted close price using technical indicators like moving averages, RSI, and volume. Built in Python using scikit-learn, it demonstrates core ML concepts applied to real market data.

---

## 📈 Features

- 📥 Fetches historical stock data using Yahoo Finance  
- ⚙️ Generates technical indicators (MAs, RSI, etc.) for feature engineering  
- 🧠 Trains a linear regression model to predict the next-day closing price  
- 📊 Evaluates model performance with R² and Mean Squared Error  
- 🔮 Outputs a prediction for the next trading day  

---

## 🛠️ Tech Stack

- Python 3.10+  
- yfinance  
- pandas  
- scikit-learn  

---

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sambriggs262/MarketModel.git
   cd MarketModel
   ```

2. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

```bash
python main.py
```

Enter any stock ticker symbol (e.g. AAPL, MSFT). The program will:
- Download historical data from Yahoo Finance (starting in 2022)
- Engineer features
- Train a regression model
- Output:
  - R² Score
  - Mean Squared Error
  - Predicted next-day adjusted close price

---

## 📁 Project Structure

```
MarketModel/
├── main.py              # CLI entry point
├── ml_utils.py          # Helper functions for data prep, modeling, evaluation
├── requirements.txt     # Dependencies
├── .gitignore           # Git exclusions
└── README.md            # You're here
```

---

## 📌 Notes

- This model is educational and not intended for financial advice or trading decisions.
- Accuracy may vary depending on the stock and time frame.

---

## 👤 Author

**Sam Briggs**  
[GitHub](https://github.com/sambriggs262) • [LinkedIn](https://linkedin.com/in/sam-briggs-8a825b327)

---

## 📜 License

This project is open source and available under the MIT License.

