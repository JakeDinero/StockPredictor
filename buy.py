import sys
import pandas as pd

ticker = sys.argv[1]
quantity = float(sys.argv[2])
buy_date = sys.argv[3]
## FORMAT OF DATE: YYYY-MM-DD
sell_date = sys.argv[4]

df = pd.read_csv('us-shareprices-daily.csv', sep = ";")

buy_price = str(df.loc[(df['Ticker'] == ticker) & (df['Date'] == buy_date)]['Open']).split(" ")[0]
sell_price = str(df.loc[(df['Ticker'] == ticker) & (df['Date'] == sell_date)]['Open']).split(" ")[0]

buy_value = quantity * float(buy_price)
sell_value = quantity * float(sell_price)
gains = float(sell_value) - float(buy_value)

print(f"Trading {ticker}")
print(f"Bought ${str(buy_value)}")
print(f"Sold ${str(sell_value)}")
print(f"Gain of ${gains}")