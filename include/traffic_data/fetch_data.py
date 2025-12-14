import requests
import json

# config für autobahn_id
#from config import AUTOBAHNEN / replaced with list in thsi file because of import errors when running in container



# Data Extraction
AUTOBAHNEN = ["A1", "A2", "A3","A4","A5","A6","A7","A8","A9"]
print(AUTOBAHNEN)

def fetch_traffic_data(autobahn_id: str):
    print("autobahn_ID", autobahn_id)
    url = f"https://verkehr.autobahn.de/o/autobahn/{autobahn_id}/services/warning"
    response = requests.get(url)
    print(response)
    return response

fetch_traffic_data(AUTOBAHNEN)


#url = 'https://verkehr.autobahn.de/o/autobahn/A8/services/warning'
#
#response = requests.get(url)
#data = response.json()
#
#
#num_warnings = len(data)
#print(f"There are {num_warnings} warnings in the JSON.")
#
#
#warning = data["warning"]
#
#
#for warnung in warning:
#    print(warnung.get("description"))
#