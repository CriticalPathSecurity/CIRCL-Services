#!/usr/bin/env python3

import requests
import json

def log_to_json(data, filename="response_log.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

auth_str = "(provided credential pair)"
# Register at https://www.circl.lu/services/passive-dns/

url = "https://www.circl.lu/pdns/query/"
query = input("Enter your query: ")

auth = tuple(auth_str.split(':'))

response = requests.get(url + query, auth=auth)

print(response.text)

response_json = response.json()
log_to_json(response_json, "response_log.json")
