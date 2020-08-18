from forex_python.converter import CurrencyRates
import sys
rates = CurrencyRates()
convertFrom = ""
convertTo = ""
amount = 0

if len(sys.argv) < 4:
    convertFrom = input("Choose which currency to convert from: ")
    convertTo = input("Choose which currency to convert to: ")
    amount = input("What amount from start currency: ")
    converted = rates.convert(convertFrom, convertTo, int(amount))
    print('{} {}'.format(converted, convertTo))
elif len(sys.argv) > 4:
    print("Too many arguments")
else:
    convertFrom = sys.argv[1]
    convertTo = sys.argv[2]
    amount = sys.argv[3]
    converted = rates.convert(convertFrom, convertTo, int(amount))
    print('{} {}'.format(converted, convertTo))

