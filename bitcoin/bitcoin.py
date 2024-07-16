import json
import requests
import sys
check = sys.argv[1].replace(".", "")
if len(sys.argv) != 2:
   sys.exit(1)
if not (check).isdigit():
    sys.exit(1)
n = sys.argv[1]
f_n = float(n)
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
response_js = response.json()
rate = response_js.get("bpi", {}).get("USD", {}).get("rate")
integer = (rate).replace(",", "")
amount = (float(integer) * f_n)
print(f"${amount:,.4f}")
