# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 200,
    "MSFT": 300
}

total_investment = 0

print("Stock Portfolio Tracker")
print("Available Stocks:", list(stock_prices.keys()))

# Taking input from user
stock_name = input("Enter stock name: ").upper()
quantity = int(input("Enter quantity: "))

# Checking if stock exists
if stock_name in stock_prices:
    total_investment = stock_prices[stock_name] * quantity

    print("\nStock:", stock_name)
    print("Quantity:", quantity)
    print("Total Investment Value =", total_investment)

    # Optional: Save result in a text file
    file = open("portfolio.txt", "w")
    file.write("Stock: " + stock_name + "\n")
    file.write("Quantity: " + str(quantity) + "\n")
    file.write("Total Investment Value: " + str(total_investment))
    file.close()

    print("Result saved in portfolio.txt")

else:
    print("Stock not found!")