import sqlite3
from trader import Trade, Portfolio, Holding

def initialize_database():
    """Initializes the database with tables if they do not exist."""
    conn = sqlite3.connect("trader.db")
    c = conn.cursor()

    # Create trades table
    c.execute("""
        CREATE TABLE IF NOT EXISTS trades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticker TEXT,
            date TEXT,
            action TEXT,
            quantity INTEGER
        )
    """)

    # Create holdings table
    c.execute("""
        CREATE TABLE IF NOT EXISTS holdings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticker TEXT,
            average_cost REAL,
            shares INTEGER
        )
    """)

    # Create portfolio table
    c.execute("""
        CREATE TABLE IF NOT EXISTS portfolio (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            balance REAL
        )
    """)

    conn.commit()
    conn.close()

def insert_trade(trade: Trade):
    """Inserts a trade into the database."""   
    conn = sqlite3.connect("trader.db")
    c = conn.cursor()

    c.execute("""
        INSERT INTO trades (ticker, date, action, quantity)
        VALUES (?, ?, ?, ?)
    """, (trade.ticker, trade.date, trade.action, trade.quantity))

    conn.commit()
    conn.close()

def insert_holding(holding: Holding):
    """Inserts a holding into the database."""
    conn = sqlite3.connect("trader.db")
    c = conn.cursor()

    c.execute("""
        INSERT INTO holdings (ticker, average_cost, shares)
        VALUES (?, ?, ?)
    """, (holding.ticker, holding.average_cost, holding.shares))

    conn.commit()
    conn.close()

def insert_portfolio(portfolio: Portfolio):
    """Inserts a portfolio into the database."""
    conn = sqlite3.connect("trader.db")
    c = conn.cursor()

    c.execute("""
        INSERT INTO portfolio (balance)
        VALUES (?)
    """, (portfolio.balance,))

    conn.commit()
    conn.close()

def get_trades() -> list:
    """Returns a list of trades from the database."""
    conn = sqlite3.connect("trader.db")
    c = conn.cursor()

    c.execute("SELECT * FROM trades")
    trades = c.fetchall()

    conn.close()
    return trades

def get_holdings() -> list:
    """Returns a list of holdings from the database."""
    conn = sqlite3.connect("trader.db")
    c = conn.cursor()

    c.execute("SELECT * FROM holdings")
    holdings = c.fetchall()

    conn.close()
    return holdings

def get_portfolio() -> list:
    """Returns a list of portfolios from the database."""
    conn = sqlite3.connect("trader.db")
    c = conn.cursor()

    c.execute("SELECT * FROM portfolio")
    portfolio = c.fetchall()

    conn.close()
    return portfolio