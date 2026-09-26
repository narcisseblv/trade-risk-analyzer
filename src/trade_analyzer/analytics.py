import pandas as pd

"""
This module provides functions to analyze trade data.
"""

def calculate_summary(trades: pd.DataFrame) -> dict:
    """
    Calculate summary statistics for the trades DataFrame.

    Args:
        trades (pd.DataFrame): A DataFrame containing trade data.

    Returns:
        dict: A dictionary containing the summary statistics.
    """
    highest_exposure_index = trades["Exposure"].idxmax()
    highest_exposure_trade = trades.loc[highest_exposure_index]

    return {
        "number_of_trades": len(trades),
        "total_exposure": trades["Exposure"].sum(),
        "total_result": trades["Result"].sum(),
        "highest_exposure_ticker": highest_exposure_trade["Ticker"],
        "highest_exposure": highest_exposure_trade["Exposure"]
    }


