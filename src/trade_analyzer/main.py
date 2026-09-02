from trade_analyzer.models import Trade

def main() -> None:
    # Example usage of the Trade class
    trade = Trade(trade_id="T001",
                  asset_class="Equity",
                  quantity=100,
                  price=50.0)

    print(f"Trade : {trade.trade_id}")
    print(f"Exposition : {trade.exposure():,.2f} €")

if __name__ == "__main__":
    main()
    