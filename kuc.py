import ccxt
import pandas as pd
kucoin = ccxt.kucoin()


#BITCOIN:
# set the symbol and the timeframe
symbol = 'BTC/USDT'
timeframe = '1d'

# set the since and limit
since = kucoin.milliseconds() - 30*24*60*60*1000
limit = 30

# fetch the historical cand data
ohlcv = kucoin.fetch_ohlcv(symbol, timeframe, since, limit)

# convert the data to pandas dataframe
df = pd.DataFrame(ohlcv, columns=["time", "open", "high", "low", "close", "volume"])

#calculate the rolling mean for the last 30 days

df['30rolling_mean'] = df['close'].rolling(30).mean()
df['9rolling_mean'] = df['close'].rolling(9).mean()
mean30=df.iloc[-1]['30rolling_mean']
mean9=df.iloc[-1]['9rolling_mean']

print(symbol)
print(mean30)
print(mean9)
#print(df1)
#print(df
if mean30 > mean9:
    print("SELL")
elif mean30 < mean9:
    print("BUY")
else:
    print("Intersect")
Depth=mean9-mean30
print(Depth)


