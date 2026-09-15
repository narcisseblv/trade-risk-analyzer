from trade_analyzer.models import Trade
from trade_analyzer.loader import load_trades
from pathlib import Path

def main() -> None:
    # Example usage of the Trade class
    trade = Trade(trade_id="T001",
                  asset_class="Equity",
                  quantity=100,
                  price=50.0)
    """
    print(f"Trade : {trade.trade_id}")
    print(f"Exposition : {trade.exposure():,.2f} €")
    """
    file_path = Path(
        "data/raw/Open Stock Transaction Data 2020-2024.xlsx"
    )
    trades = load_trades(file_path)
    print(trades[["source_year",
                  "Ticker",
                  "Result",
                  "Exposure"]].head())
    print(f"\nNumber of trades: {len(trades)}")
    print(f"Total exposure: {trades['Exposure'].sum():,.2f}")

if __name__ == "__main__":
    main()
    