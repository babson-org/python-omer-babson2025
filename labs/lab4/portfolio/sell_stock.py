
import time
import prices as _prices

def _find_position(self, sym):
    for p in self.positions:
        if p.get("sym") == sym:
            return p
    return None

def portfolio_sell_stock(self, sym: str, shares: float, price: float):
    """TODO:
    - Ensure symbol exists (use _find_position())
    - Ensure shares <= owned
    - Fetch last-close price via _prices.get_last_close_map([sym]) (use this price to sell shares)
    - Reduce position shares; adjust  'cost' proportionally by shares. (assumes average cost accounting)
    - Remove the position if shares drop to 0
    - Increase self.cash by proceeds
    - Hint: the amount you reduce cost is NOT the same as the amount you increase cash
    """
    sym = sym.upper()

    position = _find_position(self, sym)
    if position is None:
        print("Symbol not in portfolio.")
        return

    if shares <= 0:
        print("Number of shares must be positive.")
        return

    owned_shares = position.get("shares", 0.0)
    if shares > owned_shares:
        print("Cannot sell more shares than owned.")
        return

    last_close_map = _prices.get_last_close_map([sym])
    last_price = last_close_map.get(sym)
    if last_price is None:
        print("Could not fetch last close price.")
        return

    proceeds = last_price * shares

    old_cost = position.get("cost", 0.0)
    old_shares = owned_shares
    new_shares = old_shares - shares

    if new_shares == 0:
        self.positions.remove(position)
    else:
        new_cost = old_cost * (new_shares / old_shares)
        position["shares"] = new_shares
        position["cost"] = new_cost
        position["last_price"] = last_price
        position["last_update"] = time.time()

    self.cash += proceeds

    return

       
