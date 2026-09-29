# Trade Risk Analyzer

A Python command-line application that loads stock transactions from an Excel file and calculates portfolio exposure and risk indicators.

## Features

- Loads transactions from the `2023` and `2024` Excel sheets
- Filters `Market buy` and `Market sell` transactions
- Calculates exposure for each trade
- Calculates total exposure and total result
- Identifies the ticker with the highest exposure
- Provides a command-line interface
- Includes automated tests

## Project structure

```text
trade-risk-analyzer/
├── src/
│   └── trade_analyzer/
│       ├── __init__.py
│       ├── analytics.py
│       ├── loader.py
│       ├── main.py
│       └── models.py
├── tests/
│   └── test_analytics.py
├── data/
├── pyproject.toml
├── README.md
└── .gitignore
```

## Requirements

- Python 3.10 or newer
- pandas
- openpyxl
- pytest

## Installation

Clone the repository:

```bash
git clone https://github.com/narcisseblv/trade-risk-analyzer.git
```

Enter the project directory:

```bash
cd trade-risk-analyzer
```

Create a virtual environment:

```bash
python3 -m venv blv
```

Activate it on macOS or Linux:

```bash
source blv/bin/activate
```

Install the project in editable mode:

```bash
python -m pip install --editable .
```

## Input file

The application expects an Excel file containing sheets named:

- `2023`
- `2024`

Only rows whose `Action` column contains `Market buy` or `Market sell` are analyzed.

The Excel file must include the following fields used by the application:

- `Action`
- `Ticker`
- `No. of shares`
- `Price / share`
- `Exchange rate`
- `Result`
- `Currency conversion fee`

The original Excel dataset is not included in this repository.

## Exposure calculation

The base exposure is calculated as:

```text
Base exposure = No. of shares × Price / share ÷ Exchange rate
```

The currency conversion fee is then applied according to the trade result:

```text
If Result >= 0:
    Exposure = Base exposure + Currency conversion fee

If Result < 0:
    Exposure = Base exposure - Currency conversion fee
```

## Usage

Display the command help:

```bash
trade-analyzer --help
```

Analyze an Excel file:

```bash
trade-analyzer "path/to/trades.xlsx"
```

Example:

```bash
trade-analyzer "data/raw/Open Stock Transaction Data 2020-2024.xlsx"
```

Quotes are recommended when the file path contains spaces.

## Output

The application displays:

- Number of analyzed trades
- Total exposure
- Total result
- Ticker with the highest exposure
- Value of the highest exposure

Example output:

```text
Number of trades: 250
Total exposure: 125,430.50
Total result: 3,240.75
Highest exposure: AAPL — 12,500.00
```

## Tests

Run the automated tests from the project root:

```bash
pytest
```

A successful execution should display a result similar to:

```text
1 passed
```

## Technologies

- Python
- pandas
- openpyxl
- pytest
- setuptools