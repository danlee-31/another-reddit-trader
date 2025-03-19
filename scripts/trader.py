from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List, Dict, Any, Tuple
import os
import yfinance as yf

# Define Trade dataclass
@dataclass
class Trade:
    ticker: str
    date: datetime
    action: str  # 'buy' or 'sell'
    quantity: int

# Placeholder function to query Polygon API for stock price
def get_stock_price(ticker: str, date: datetime) -> float:
    """Fetches stock price from Polygon API for a given ticker and date."""
    # TODO: Implement API call
    stock = yf.Ticker(ticker)
    start = date.strftime('%Y-%m-%d')
    end = (date + timedelta(days=1)).strftime('%Y-%m-%d')
    data = stock.history(start=start, end=end)
    if not data.empty:
        return round(float(data['Close'].iloc[0]), 2)
    else:
        raise ValueError("No data found for the given date")

# Function to execute a trade and update portfolio
def execute_trade(portfolio: Dict[str, Dict[str, Any]], trade: Trade, balance: float) -> Tuple[Dict[str, Dict[str, Any]], float]:
    """Updates portfolio based on the trade action."""

    # call the "get_stock_price" function to get the stock price for the trade date
    price = get_stock_price(trade.ticker, trade.date)

    # check if the trade ticker is in the portfolio, if not add it
    #   initialize the stock position with average cost, shares, and trades list
    if trade.ticker not in portfolio:
        portfolio[trade.ticker] = {
            "average_cost": 0.0,
            "shares": 0,
            "trades": []
        }
    
    # if the action is 'buy', add number of shares; if 'sell', remove shares
    #   update the average cost based on the total cost of shares
    if trade.action == 'buy':
        total_cost = price * trade.quantity
        total_value = portfolio[trade.ticker]["average_cost"] * portfolio[trade.ticker]["shares"] + total_cost
        total_shares = portfolio[trade.ticker]["shares"] + trade.quantity
        portfolio[trade.ticker]["average_cost"] = total_value / total_shares
        portfolio[trade.ticker]["shares"] = total_shares
        balance -= total_cost
    elif trade.action == 'sell':
        if trade.quantity > portfolio[trade.ticker]["shares"]:
            raise ValueError("Not enough shares to sell")
        total_cost = price * trade.quantity
        portfolio[trade.ticker]["shares"] -= trade.quantity
        balance += total_cost

    portfolio[trade.ticker]["trades"].append(trade)

    return portfolio, balance

# Main function to process trades
def process_trades(trades: List[Trade], balance: float) -> Tuple[Dict[str, Dict[str, float]], float]:
    """Processes a list of trades and returns the updated portfolio."""

    # TODO: create a portfolio dictionary to store the current position of each stock
    portfolio = {}

    # TODO: loop through each "trade" in the list of trade "trades"
    #   call the "execute_trade" function to update the portfolio
    for trade in trades:
        portfolio, balance = execute_trade(portfolio, trade, balance)

    # TODO: return the final portfolio
    return portfolio, balance

# Example usage
if __name__ == "__main__":
    balance = 100000.0
    trade_list = [
        Trade("AAPL", datetime(2025, 3, 4), "buy", 10),
        Trade("AAPL", datetime(2025, 3, 5), "buy", 5),
        Trade("AAPL", datetime(2025, 3, 11), "sell", 8),
        Trade("TSLA", datetime(2025, 3, 12), "buy", 3)
    ]
    
    final_portfolio, final_balance = process_trades(trade_list, balance)
    print(final_portfolio)
    print(final_balance)
