import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

tickers = [
    "XLC", "XLY", "XLP", "XLE", "XLF", "XLV", "XLI", "XLK", "XLB", "VNQ", "XLU",
    "SHY", "IEF", "TLT", "TIP", "VCSH", "LQD", "VCLT", "HYG",
    "GLTR", "DBE", "DBB", "DBA"
]

start_date = "2001-01-01"
end_date = pd.Timestamp.today().strftime("%Y-%m-%d")

for ticker in tickers:
    df = yf.download(ticker, start=start_date, end=end_date)
    df.index = pd.to_datetime(df.index)

    df.to_csv(f"{ticker}.csv")

    df["MA50"] = df["Close"].rolling(window=50).mean()
    df["MA200"] = df["Close"].rolling(window=200).mean()

    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df["Close"], label="Close")
    plt.plot(df.index, df["MA50"], label="50-day MA")
    plt.plot(df.index, df["MA200"], label="200-day MA")
    plt.title(f"{ticker}: Closing Price & Moving Averages")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.tight_layout()

    plt.savefig(f"{ticker}_close_ma.png")
    plt.close("all")
