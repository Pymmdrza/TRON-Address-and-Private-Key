import requests

url = "https://api.shasta.trongrid.io/wallet/getaccountbalance"

payload = {
    "account_identifier": "{         \"address\": \"**YOURADDRESSHERE***\"     },",
    "block_identifier": {
        "hash": "0000000000010c4a732d1e215e87466271e425c86945783c3d3f122bfa5affd9",
        "number": 68682
    },
    "visible": True
}
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)
