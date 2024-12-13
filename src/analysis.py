import pynance as pn

def calculate_daily_returns(data):
    """Calculate daily returns."""
    return pn.data.daily_ret(data['Close'])

def calculate_volatility(data):
    """Calculate rolling volatility."""
    return pn.data.volatility(data['Close'], window=20)
