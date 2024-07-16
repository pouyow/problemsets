import json
import requests
import sys
try:
    if len(sys.argv) != 2:
        sys.exit()
    n = sys.argv[1]
    int_n = int(n)
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response_js = response.json()
    rate = response_js.get("bpi", {}).get("USD", {}).get("rate")
    integer = (rate).replace(",", "")
    amount = (float(integer) * int_n)
    print(f"${amount:,.4f}")
except ValueError:
    print("fuck u")
