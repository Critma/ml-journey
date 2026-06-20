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
        companies_low = {k.lower(): v for k, v in COMPANIES.items()}
        user_input_low = sys.argv[1].lower()
        if user_input_low in companies_low:
            print(STOCKS[companies_low[user_input_low]])
        else:
            print("Unknown company")

if __name__ == "__main__":
    logic()