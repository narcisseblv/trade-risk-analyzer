import pandas as pd

from trade_analyzer.analytics import calculate_summary


def test_calculate_summary() -> None:
	trades = pd.DataFrame({
	"Ticker": ["AAPL","MSFT","GOOGL"],
	"Exposure": [1000.0, 2500.0, 1500.0],
	"Result": [50.0, -20.0, 30.0]
	}
	)

	summary = calculate_summary(trades)

	assert summary["number_of_trades"] == 3
	assert summary["total_exposure"] == 5000.0
	assert summary["total_result"] == 60.0
	assert summary["highest_exposure_ticker"] == "MSFT"
	assert summary["highest_exposure"] == 2500.0

