
import yfinance as yf
import time
import pandas as pd

while(True):

    pd.set_option('display.width', 1000)
    pd.set_option('display.max_columns', 500)
    symbol = yf.Ticker("BTC-USD")
    df = symbol.history(start="2022-12-1", end="2023-2-2", period="max", interval="5m")
    df.head(100)

    #print(df['30 day ma'])
    #df['30_day_ma'] = df['close'].rolling(window=30).mean()
    #print(df)

    # updating our dataFrame to have only
    # one column 'Close' as rest all columns
    # are of no use for us at the moment
    # using .to_frame() to convert pandas series
    # into dataframe.
    df = df['Close'].to_frame()

    # calculating simple moving average
    # using .rolling(window).mean() ,
    # with window size = 30
    df['SMA30'] = df['Close'].rolling(30).mean()
    df['SMA9'] = df['Close'].rolling(9).mean()

    # removing all the NULL values using
    # dropna() method
    df.dropna(inplace=True)

    # printing Dataframe
    print(df)

    last = (df.iloc[-1:])
    print(last)
    lastcolumn30= df.iloc[-1]["SMA30"]
    print(lastcolumn30)
    lastcolumn9= df.iloc[-1]["SMA9"]
    print(lastcolumn9)

    #if df.iloc[-1]["SMA30"] > df.iloc[-1]["SMA9"]:
       # print("30>9")
    #time.sleep(60)

    if lastcolumn30 > lastcolumn9:
        print("SELL")
    elif lastcolumn30 < lastcolumn9:
        print("BUY")
    else:
        print("Intersect")

Return()
