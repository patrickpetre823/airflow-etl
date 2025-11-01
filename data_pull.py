import requests
import json

url = 'https://verkehr.autobahn.de/o/autobahn/A8/services/warning'

response = requests.get(url)
data = response.json()

#print(json.dumps(data, indent=2, ensure_ascii=False))

# assuming your JSON is loaded into 'data'
num_warnings = len(data)
print(f"There are {num_warnings} warnings in the JSON.")

#print(type(data))
#
#print(data.keys())

warning = data["warning"]


for warnung in warning:
    print(warnung.get("description"))

#for warning in data["warning"]:
#    print(warning["description"])