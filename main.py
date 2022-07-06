from forex_python.converter import CurrencyRates

c = CurrencyRates()

amount = int(input("Enter the amount:"))
from_currency = input("Enter Currency to convert from:").upper()
to_currency = input("To Currency:").upper()

print(from_currency, "to", to_currency,amount)
result = c.convert(from_currency, to_currency, amount)
print(result)