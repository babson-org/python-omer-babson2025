
import time
def portfolio_add_cash(self, amount: float):
    """TODO:
    - Reject negative amounts
    - Otherwise add to self.cash
    - Print message showing how much cash added and what you new cash balance is
    - return not needed
    """
    if amount < 0:
        print("Cannot add a negative amount of cash.")
        return

    self.cash += amount
    print(f"Added ${amount:,.2f} cash. New cash balance is ${self.cash:,.2f}.")