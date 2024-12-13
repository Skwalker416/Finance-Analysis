import talib

def calculate_sma(data, timeperiod=20):
    """Calculate Simple Moving Average (SMA)."""
    return talib.SMA(data['Close'], timeperiod=timeperiod)

def calculate_rsi(data, timeperiod=14):
    """Calculate Relative Strength Index (RSI)."""
    return talib.RSI(data['Close'], timeperiod=timeperiod)

def calculate_macd(data):
    """Calculate MACD (Moving Average Convergence Divergence)."""
    macd, macdsignal, macdhist = talib.MACD(
        data['Close'], 
        fastperiod=12, 
        slowperiod=26, 
        signalperiod=9
    )
    return macd, macdsignal, macdhist
