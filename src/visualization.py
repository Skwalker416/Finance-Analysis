import matplotlib.pyplot as plt

def plot_with_sma(data, sma):
    """Plot stock price with SMA."""
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['Close'], label='Close Price', alpha=0.8)
    plt.plot(data.index, sma, label='20-Day SMA', linestyle='--')
    plt.title("Stock Price with SMA")
    plt.legend()
    plt.show()

def plot_rsi(data, rsi):
    """Plot RSI."""
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, rsi, label='RSI', color='orange')
    plt.axhline(70, linestyle='--', color='red', alpha=0.7)
    plt.axhline(30, linestyle='--', color='green', alpha=0.7)
    plt.title("RSI (Relative Strength Index)")
    plt.legend()
    plt.show()
