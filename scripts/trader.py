from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict
import os

# Define Trade dataclass
@dataclass
class Trade:
    ticker: str
    date: datetime
    action: str  # 'buy' or 'sell'
    quantity: int

# Placeholder function to query Polygon API for stock price
def get_stock_price(ticker: str, date: str) -> float:
    """Fetches stock price from Polygon API for a given ticker and date."""
    # TODO: Implement API call
    return 100.0  # Placeholder price

# Function to execute a trade and update portfolio
def execute_trade(portfolio: Dict[str, Dict[str, float]], trade: Trade):
    """Updates portfolio based on the trade action."""

    # TODO: call the "get_stock_price" function to get the stock price for the trade date
    
    # TODO: check if the trade ticker is in the portfolio, if not add it
    #   initialize the stock position with average cost, shares, and trades list
    
    # TODO: if the action is 'buy', add number of shares; if 'sell', remove shares
    #   update the average cost based on the total cost of shares

    # TODO: return the updated portfolio
    return None #stub

# Main function to process trades
def process_trades(trades: List[Trade]) -> Dict[str, Dict[str, float]]:
    """Processes a list of trades and returns the updated portfolio."""

    # TODO: create a portfolio dictionary to store the current position of each stock

    # TODO: loop through each "trade" in the list of trade "trades"
    #   call the "execute_trade" function to update the portfolio

    # TODO: return the final portfolio
    return None #stub

# Example usage
if __name__ == "__main__":
    trade_list = [
        Trade("AAPL", datetime(2025, 3, 4), "buy", 10),
        Trade("AAPL", datetime(2025, 3, 5), "buy", 5),
        Trade("AAPL", datetime(2025, 3, 11), "sell", 8),
        Trade("TSLA", datetime(2025, 3, 12), "buy", 3)
    ]
    
    final_portfolio = process_trades(trade_list)
    print(final_portfolio)
