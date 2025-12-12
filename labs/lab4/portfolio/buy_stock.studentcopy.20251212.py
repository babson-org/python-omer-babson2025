

import prices as _prices
import time

def _find_position(self, sym):
    for p in self.positions:
        if p.get("sym") == sym:
            return p
    return None

def portfolio_buy_stock(self, sym: str, shares: float, price: float):
    """TODO:    
    - Validate sym in DOW30
         In the lab4 folder is a file prices.py.  Look at the file and find out what DOW30 is
         You can access DOW30 with _prices.DOW30 (see how we import prices above)
    - Validate shares > 0
    - Fetch last-close price via _prices.get_last_close_map([sym]) (use this price to buy shares)
    - Make sure the client has enough cash to make the purchase (price * shares)

    - IMPORTANT: in self.positions there should only be one dictionary per symbol

    - Add the purchase to an existing position or create a new position in self.positions 
    - Be sure to decrease the client cash attribute
    NOTE: UI prompts are handled in main.py: this method only prints for invalid ticker and insufficient funds. The rest are handled in main.py
    """
    sym = sym.upper()

    if sym not in _prices.DOW30:
        raise ValueError(f"Unknown symbol: {sym}")

    if shares <= 0:
        raise ValueError("Shares must be positive.")

    trade_price = float(price)
    trade_cost = trade_price * shares

    if trade_cost > self.cash:
        raise ValueError("Insufficient cash to buy stock.")

    for pos in self.positions:
        if pos["sym"] == sym:
            pos["shares"] += shares
            pos["cost"] += trade_cost
            break
    else:
        self.positions.append(
            {
                "sym": sym,
                "shares": shares,
                "cost": trade_cost,
            }
        )

    self.cash -= trade_cost
    return