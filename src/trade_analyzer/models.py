from dataclasses import dataclass

@dataclass
class Trade:
    trade_id: str
    asset_class:str
    quantity: float
    price: float

    def exposure(self) -> float:
        """Calculate the exposure of the trade."""
        return self.quantity * self.price
    