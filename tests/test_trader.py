import pytest
import json
from datetime import datetime
from scripts.trader import Trade, process_trades

# Load test data from JSON file
with open('/Users/junhyuck.lee/Documents/GitHub/another-reddit-trader/tests/test_trades.json') as f:
    test_data = json.load(f)

@pytest.fixture
def trades():
    return [Trade(ticker=trade['ticker'], date=datetime.strptime(trade['date'], '%Y-%m-%d'), action=trade['action'], quantity=trade['quantity']) for trade in test_data['trades']]

def test_process_trades(trades):
    expected_portfolio = test_data['expected_portfolio']
    result_portfolio = process_trades(trades)
    assert result_portfolio == expected_portfolio