# models.py defines what a Trdade is and how to calculate its exposure.
from dataclasses import dataclass
"""
Here we define a Trade class that represents a financial trade. 
The class  includes attributes 
for the trade ID, asset class, quantity, and price. 
It also includes a method to calculate the exposure of the trade based on the quantity and price.
"""

@dataclass
class Trade:
    trade_id: str
    asset_class:str
    quantity: float
    price: float

    def exposure(self) -> float:
        """Calculate the exposure of the trade."""
        return self.quantity * self.price
    