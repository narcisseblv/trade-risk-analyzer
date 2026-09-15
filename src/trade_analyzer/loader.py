from pathlib import Path
import pandas as pd

def load_trades(file_path: str) -> pd.DataFrame:
    """
    Load trades from a CSV file into a pandas DataFrame.

    Args:
        file_path (str): The path to the CSV file containing trade data.
    """
    sheets = pd.read_excel(
        file_path,
        sheet_name = ["2023", "2024"]
    )
    frames = []

    for sheet_name, df in sheets.items():
        df = df.copy()
        df["source_year"] = sheet_name
        frames.append(df)

    trades = pd.concat(frames, ignore_index=True)

    trades = trades[
        trades["Action"].isin(["Market buy", "Market sell"])

    ].copy()

    trades["Result"] = trades["Result"].fillna(0.0).astype(float)

    trades["Currency conversion fee"] = (
        trades["Currency conversion fee"].fillna(0.0).astype(float)
    )

    base_exposure = (
        trades["No. of shares"] * trades["Price / share"] / trades["Exchange rate"]
    )

    trades.loc[trades["Result"] >= 0, "Exposure"] = base_exposure + trades["Currency conversion fee"]
    trades.loc[trades["Result"] < 0, "Exposure"] = base_exposure - trades["Currency conversion fee"]

    trades = trades.reset_index(drop=True).copy()
    
    return trades
