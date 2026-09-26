from trade_analyzer.loader import load_trades
from trade_analyzer.analytics import calculate_summary
from pathlib import Path

def main() -> None:
    # Example usage of the Trade class

    file_path = Path(
        "data/raw/Open Stock Transaction Data 2020-2024.xlsx"
    )
    trades = load_trades(file_path)
    summary = calculate_summary(trades)

    print(trades[["source_year",
                  "Ticker",
                  "Result",
                  "Exposure"]].head())
    
    print(f"\nNumber of trades: {summary['number_of_trades']}") 
    print(f"Total exposure: {summary['total_exposure']:,.2f}")
    print(f"Total result: {summary['total_result']:,.2f}")
    print(
        "Highest exposure: "
        f"{summary['highest_exposure_ticker']} - "
        f"{summary['highest_exposure']:,.2f}"
    )

if __name__ == "__main__":
    main()
    