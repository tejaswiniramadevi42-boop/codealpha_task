# CodeAlpha - Stock Portfolio Tracker

print("======================================")
print("       STOCK PORTFOLIO TRACKER")
print("======================================")

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = {}
total_investment = 0

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} - ${price}")

print("\nEnter your stock details.")
print("Type 'done' when you have finished.\n")

while True:
    stock = input("Enter stock symbol: ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available. Please choose from the listed stocks.\n")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.\n")
            continue

        investment = stock_prices[stock] * quantity

        portfolio[stock] = {
            "quantity": quantity,
            "price": stock_prices[stock],
            "investment": investment
        }

        total_investment += investment

        print(f"Added {quantity} shares of {stock}.")
        print(f"Investment: ${investment}\n")

    except ValueError:
        print("Please enter a valid number.\n")


# Display portfolio summary
print("\n======================================")
print("          PORTFOLIO SUMMARY")
print("======================================")

if len(portfolio) == 0:
    print("No stocks were added.")
else:
    print(f"{'Stock':<10}{'Quantity':<10}{'Price':<10}{'Investment':<15}")
    print("-" * 45)

    for stock, details in portfolio.items():
        print(
            f"{stock:<10}"
            f"{details['quantity']:<10}"
            f"${details['price']:<9}"
            f"${details['investment']:<15}"
        )

    print("-" * 45)
    print(f"Total Investment: ${total_investment}")

print("\nThank you for using Stock Portfolio Tracker!")