import sys
import pandas as pd

ticker = sys.argv[1]
quantity = float(sys.argv[2])
sell_date = sys.argv[3]
## FORMAT OF DATE: YYYY-MM-DD
buy_date = sys.argv[4]

df = pd.read_csv('us-shareprices-daily.csv', sep = ";")

sell_price = df.loc[(df['Ticker'] == ticker) & (df['Date'] == buy_date)]['Open'].tolist()[0]
buy_price = df.loc[(df['Ticker'] == ticker) & (df['Date'] == sell_date)]['Open'].tolist()[0]

# print(buy_price)
# print(sell_price)

sell_value = quantity * float(sell_price)
buy_value = quantity * float(buy_price)
gains = buy_value - sell_value

print(f"Trading {ticker}")
print(f"Bought ${round(buy_value, 2)}")
print(f"Sold ${round(sell_value, 2)}")
print(f"Gain of ${round(gains, 2)}")