from utils import load_data, clean_data
from indicators import calculate_sma, calculate_rsi, calculate_macd
from analysis import calculate_daily_returns, calculate_volatility
from visualization import plot_with_sma, plot_rsi

def main():
    # Load and clean data
    raw_data = load_data("data/raw/yfinance_data.csv")
    data = clean_data(raw_data)
    
    # Calculate indicators
    sma = calculate_sma(data)
    rsi = calculate_rsi(data)
    macd, macdsignal, macdhist = calculate_macd(data)
    
    # Perform analysis
    daily_returns = calculate_daily_returns(data)
    volatility = calculate_volatility(data)
    
    # Visualize results
    plot_with_sma(data, sma)
    plot_rsi(data, rsi)

if __name__ == "__main__":
    main()