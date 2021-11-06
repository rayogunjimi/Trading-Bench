import config.py

apikey = av_api_key

class interval(enum,Enum):
    _1min       = 0
    _5min       = 1
    _15min      = 2
    _30min      = 3
    _60min      = 4

    _daily       = 10
    _weekly      = 11
    _monthly     = 13

    _quarterly   = 20
    _annual      = 21

class function(enum,Enum):
    # Stock Time series
    TIME_SERIES_INTRADAY            = 0
    TIME_SERIES_INTRADAY_EXTENDED   = 1
    TIME_SERIES_DAILY               = 2
    TIME_SERIES_DAILY_ADJUSTED      = 3
    TIME_SERIES_WEEKLY              = 4
    TIME_SERIES_WEEKLY_ADJUSTED     = 5
    TIME_SERIES_MONTHLY             = 6
    TIME_SERIES_MONTHLY_ADJUSTED    = 7

    # Fundamental Data
    OVERVIEW                        = 10
    EARNINGS                        = 11
    INCOME_STATEMENT                = 12
    BALANCE_SHEET                   = 13
    CASH_FLOW                       = 14
    LISTING_STATUS                  = 15
    EARNINGS_CALENDAR               = 16
    IPO_CALENDAR                    = 17

    # Economic Indicators
    REAL_GDP                        = 20
    REAL_GDP_PER_CAPITA             = 21
    CPI                             = 22
    INFLATION                       = 23
    INFLATION_EXPECTATION           = 24
    CONSUMER_SENTIMENT              = 25
    RETAIL_SALES                    = 26

    # FOREX
    CURRENCY_EXCHANGE_RATE          = 30
    FX_INTRADAY                     = 31

    # Cryptocurrencies
    CURRENCY_EXCHANGE_RATE          = 40

    # Technical Indicators
    SMA                             = 50
    EMA                             = 51
    VWAP                            = 52
    MACD                            = 53
    STOCH                           = 54
    RSI                             = 55
    ADX                             = 56
    CCI                             = 57
    OBV                             = 57

    # Alternatives
    GLOBAL_QUOTE                    = 60
    SYMBOL_SEARCH                   = 61

class datatype(enum,Enum):
    json     = 1
    csv      = 2

# Portfolio Setup
symbol_owned = []
amount_owned = []
purchase_price = []
current_price = []

# Handle Requests
def get_request_url(interval , function, symbol, apikey, datatype):
    import enum
    import config.py

    queryurl = "https://www.alphavantage.co/query?"

    queryurl.append(      "function="   + function)
    queryurl.append("&" + "symbol="     + symbol)
    queryurl.append("&" + "interval="   + interval)
    queryurl.append("&" + "apikey="     + apikey)
    queryurl.append("&" + "datatype="   + datatype)

    return queryurl

def interpret_request(symbol, task):
    # Use HTTP/REST response to catch bad request
    if(task == "stock"):
        response_json = request( get_request_url(symbol, ) )
        current_price = response_json(1)
        return (current_price)

def execute_trade(symbol, amount):
    current_price = interpret_request(symbol, "stock")
    if ( symbol_owned.find(symbol) ):
        purchase_price[symbol_owned.find(symbol)] = (purchase_price[symbol_owned.find(symbol)]*amount_owned[symbol_owned.find(symbol)]+current_price*amount)/(amount_owned[symbol_owned.find(symbol)]+amount)
        amount_owned[symbol_owned.find(symbol)] = amount_owned[symbol_owned.find(symbol)] + amount
    else:
        symbol_owned.append(symbol)
        purchase_price.append(current_price)
        amount_owned.append(amount)

def query_price(symbol):
    return interpret_request(symbol, "stock")

def papertrade(end_date):
    from datetime import datetime
    if(int(end_date) > int(date())):
        while(date != time_interval):
            trading_algorithm()
    else:
        Exception("In paper trade mode end date must be in the future")

def backtest(start_date, end_date):
    from datetime import datetime
    if( int(end_date) < int(date()) and int(start_date) < int(date()) ):
        for date in range(start_date, end_date):
            trading_algorithm(date)
    else:
        Exception("In backtest mode start and end date must be in the past")

def show_protfolio_stats():
    import matplotlib
    import pandas

def trading_algorithm():
    # TODO: Implement sample algorithm
    execute_trade("IBM")
    show_protfolio_stats()

def main():
    import requests
    import json

    backtest("01-01-2020", "01-01-2021")
    # papertrade(dateitme.now(), datetime.today())


if __name__ == '__main__':
    main()