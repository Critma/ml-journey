import sys

def parse_line(line) -> list:
    comma = False
    values = []
    current_value = ''
    for sym in line:
        if sym == ',':
            if comma:
                return []
            comma = True
            values.append(current_value.strip())
            current_value = ''
        else:
            if sym == ' ':
                continue
            comma = False
            current_value += sym
    values.append(current_value)
    return values

def get_info(values: list):
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
    low_companies = {k.lower() : v for k, v in COMPANIES.items()}
    low_normal_companies = {k.lower() : k for k, v in COMPANIES.items()}
    low_tickers = {v.lower() : k for k, v in COMPANIES.items()}
    low_normal_tickers = {v.lower() : v for k, v in COMPANIES.items()}
    for value in values:
        val = value.lower()
        if val in low_companies:
            print(f"{low_normal_companies[val]} stock price is {STOCKS[low_companies[val]]}")
        elif val in low_tickers:
            print(f"{low_normal_tickers[val]} is a ticker symbol for {low_tickers[val]}")
        else:
            print(f"{value} is an unknown company or an unknown ticker symbol")
        
def logic():
    if len(sys.argv) == 2:
        result = parse_line(sys.argv[1])
        if len(result) == 0:
            return
        get_info(result)


if __name__ == "__main__":
    logic()