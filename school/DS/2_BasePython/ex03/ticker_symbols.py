import sys

def logic():
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }
    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }
    if len(sys.argv) == 2:
        tickers_low = {v.lower() : k for k, v in COMPANIES.items()}
        user_input_low = sys.argv[1].lower()
        if user_input_low in tickers_low:
            company = tickers_low[user_input_low]
            stocks_low = {k.lower() : v for k, v in STOCKS.items()}
            print(company, stocks_low[user_input_low])
        else:
            print("Unknown ticker")

if __name__ == "__main__":
    logic()