import simfin as sf
from simfin.names import *
import matplotlib.pyplot as plt 
import seaborn as sns

# Set your API-key for downloading data.
# If the API-key is 'free' then you will get the free data,
# otherwise you will get the data you have paid for.
# See www.simfin.com for what data is free and how to buy more.
sf.set_api_key('free')

# Set the local directory where data-files are stored.
# The dir will be created if it does not already exist.
sf.set_data_dir('~/simfin_data/')

# Load the annual Income Statements for all companies in USA.
# The data is automatically downloaded if you don't have it already.
df = sf.load_income(variant='annual', market='us')

# Print all Revenue and Net Income for Microsoft (ticker MSFT).
# print(df.loc['MSFT', [REVENUE, NET_INCOME]])


df_income.loc['MSFT', [REVENUE, NET_INCOME]].plot(grid=True)
plt.show()