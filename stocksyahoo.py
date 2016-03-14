


##### pip install yahoo_finance,
# require python2
# from yahoo_finance import Share
import yahoo_finance

stocks = {'YHOO', 'GOOGL', 'AAPL'}

try:
    for stock in stocks:
        s = yahoo_finance.Share(stock)
        s.get_open()

        print "Stock name: " + stock
        print "Price: $" + s.get_price()
        print "AVG volume: " + s.get_avg_daily_volume()
        print "Market cap: $" + s.get_market_cap()
        print s.get_info()

except:
    print "****** Critical error, verify the stock's symbol ******"
    raise
