from enum import Enum
from config import *

# simmulate trade execution delay of certain brokerage
trade_delay = 0

class api_argument(Enum):
    apikey = get_api_key()

     # Length of sampling resolution period in seconds
    time_period = 0

    class interval(Enum):
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

    class function(Enum):
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
        # CURRENCY_EXCHANGE_RATE          = 40

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

    class datatype(Enum):
        json     = 0
        csv      = 1

    class outputsize(Enum):
        compact     = 0
        full      = 1

    class adjusted(Enum):
        true     = 0
        false      = 1

    class slice(Enum):
        year1month1     = 0

# Portfolio Setup
request_time =  datetime(2020, 1, 1, 0, 0, 0, 0)
symbol_owned = []
amount_owned = []
purchase_price = []
current_price = []

# Handle Requests
def get_request_url( function = "GLOBAL_QUOTE", symbol = "IBM", interval = "1min", apikey = apikey, datatype = "json", time_period = "1", outputsize = "compact", adjusted = "true", slice = "year1month1"):
    import enum

    queryurl = "https://www.alphavantage.co/query?"

    queryurl = queryurl +       "function="     + function
    queryurl = queryurl + "&" + "symbol="       + symbol
    queryurl = queryurl + "&" + "interval="     + interval
    queryurl = queryurl + "&" + "apikey="       + apikey
    queryurl = queryurl + "&" + "datatype="     + datatype
    queryurl = queryurl + "&" + "time_period="  + time_period
    queryurl = queryurl + "&" + "outputsize="   + outputsize
    queryurl = queryurl + "&" + "adjusted="     + adjusted
    queryurl = queryurl + "&" + "slice="        + slice
    return queryurl

def find_in_json(response_json, time, price_type = "open"):


def send_and_interpret_request(symbol, task, time = ""):
    import requestsGLOBAL_QUOTE
    import json
    # Use HTTP/REST response to catch bad request
    if(task == "quotestock_now"):
        response_json = requests.get( get_request_url(function = "GLOBAL_QUOTE", symbol = symbol) ).json()
        current_price = find_in_json(response_json, price_type = "close")
        print(current_price)
        return (current_price)
    elif(task == "quotestock_past"):
        response_json = requests.get( get_request_url(function = "GLOBAL_QUOTE", symbol = symbol) ).json()
        current_price = find_in_json(response_json, time = time, price_type = "close")
        print(current_price)
        return (current_price)

def execute_trade(symbol, amount):
    wait(trade_delay)
    current_price = send_and_interpret_request(symbol, "quotestock")
    if ( symbol in symbol_owned):
        purchase_price[symbol_owned.index(symbol)] = (purchase_price[symbol_owned.index(symbol)]
                                                      *amount_owned[symbol_owned.index(symbol)]
                                                      +current_price*amount)/(amount_owned[symbol_owned.index(symbol)]+amount)
        amount_owned[symbol_owned.index(symbol)] = amount_owned[symbol_owned.index(symbol)] + amount
    else:
        symbol_owned.append(symbol)
        purchase_price.append(current_price)
        amount_owned.append(amount)

def query_price(symbol):
    return send_and_interpret_request(symbol, "quotestock")

def papertrade(start_date, stop_date):
    from datetime import datetime
    current_date = start_date
    while(current_date <= stop_date):
        if(current_date < start_date):
            trading_algorithm()
            print("Elapsing time.")
            current_date += timedelta(minute=1)
        else:
            trading_algorithm()
            print("Waiting for time to elapse.")
            wait(1)
            continue
            current_date = datetime.now()

def show_protfolio_stats():
    import matplotlib
    import pandas
    # Implement analyzer

def trading_algorithm():
    # TODO: Implement algorithm
    execute_trade("IBM", 1)
    show_protfolio_stats()

def main():
    from datetime import datetime
    start_date = datetime(2020, 1, 1, 0, 0, 0, 0)
    stop_date =  datetime(2021, 1, 1, 0, 0, 0, 0)
    papertrade(start_date, stop_date)


if __name__ == '__main__':
    main()