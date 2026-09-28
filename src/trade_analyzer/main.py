import argparse
from trade_analyzer.loader import load_trades
from trade_analyzer.analytics import calculate_summary
from pathlib import Path

def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Analyze trade exposure from an Excel file."
    )

    parser.add_argument(
        "file_path",
        type=Path,
        help="Path to the Excel trade file."
    )
    return parser.parse_args()



def main() -> None:

    args = parse_arguments()

    trades = load_trades(args.file_path)
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
    