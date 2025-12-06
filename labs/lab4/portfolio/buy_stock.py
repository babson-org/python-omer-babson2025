

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
        print("Invalid ticker symbol.")
        return

    if shares <= 0:
        print("Number of shares must be positive.")
        return

    last_close_map = _prices.get_last_close_map([sym])
    last_price = last_close_map.get(sym)

    if last_price is None:
        print("Could not fetch last close price.")
        return

    total_cost = last_price * shares

    if self.cash < total_cost:
        print("Insufficient funds to complete purchase.")
        return

    position = _find_position(self, sym)
    now = time.time()

    if position is None:
        position = {
            "sym": sym,
            "shares": shares,
            "cost": total_cost,
            "last_price": last_price,
            "last_update": now,
        }
        self.positions.append(position)
    else:
        position["shares"] += shares
        position["cost"] += total_cost
        position["last_price"] = last_price
        position["last_update"] = now

    self.cash -= total_cost
    return