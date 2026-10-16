# Stock Portfolio Tracker
# CodeAlpha Python Internship - Task 2

# Hardcoded stock prices (in USD)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 370,
    "AMZN": 155,
    "META": 320,
    "NFLX": 480
}


def show_available_stocks():
    print("\nAvailable Stocks:")
    print("-" * 30)
    for name, price in stock_prices.items():
        print(f"  {name:6}  ->  ${price}")
    print("-" * 30)


def get_portfolio():
    portfolio = {}

    print("\nEnter stock name and quantity.")
    print("Type 'done' when finished.\n")

    while True:
        stock = input("Stock name: ").upper().strip()

        if stock == "DONE":
            break

        if stock not in stock_prices:
            print(f"  '{stock}' not found. Try again.\n")
            continue

        try:
            qty = int(input(f"Quantity of {stock}: "))
            if qty <= 0:
                print("  Quantity must be positive.\n")
                continue
        except ValueError:
            print("  Please enter a valid number.\n")
            continue

        # Add to portfolio (if already exists, add quantity)
        if stock in portfolio:
            portfolio[stock] += qty
        else:
            portfolio[stock] = qty

        print(f"  Added {qty} shares of {stock}.\n")

    return portfolio


def calculate_total(portfolio):
    total = 0
    print("\n" + "=" * 45)
    print("         PORTFOLIO SUMMARY")
    print("=" * 45)
    print(f"{'Stock':<8}{'Qty':<8}{'Price':<10}{'Value':<10}")
    print("-" * 45)

    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = price * qty
        total += value
        print(f"{stock:<8}{qty:<8}${price:<9}${value:<9}")

    print("-" * 45)
    print(f"TOTAL INVESTMENT: ${total}")
    print("=" * 45)

    return total


def save_to_file(portfolio, total):
    choice = input("\nSave result to file? (y/n): ").lower().strip()

    if choice != "y":
        print("Result not saved.")
        return

    with open("portfolio.txt", "w") as f:
        f.write("STOCK PORTFOLIO REPORT\n")
        f.write("=" * 35 + "\n")
        f.write(f"{'Stock':<8}{'Qty':<8}{'Value':<10}\n")
        f.write("-" * 35 + "\n")

        for stock, qty in portfolio.items():
            value = stock_prices[stock] * qty
            f.write(f"{stock:<8}{qty:<8}${value:<10}\n")

        f.write("-" * 35 + "\n")
        f.write(f"Total Investment: ${total}\n")

    print("Saved to portfolio.txt successfully.")


def main():
    print("=" * 45)
    print("      STOCK PORTFOLIO TRACKER")
    print("=" * 45)

    show_available_stocks()

    portfolio = get_portfolio()

    if not portfolio:
        print("\nNo stocks added. Exiting.")
        return

    total = calculate_total(portfolio)
    save_to_file(portfolio, total)

    print("\nThank you for using Stock Portfolio Tracker!")


if __name__ == "__main__":
    main()