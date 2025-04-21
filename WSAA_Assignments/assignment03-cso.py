# Assignment 3 - CSO Exchequer Account API Data import
# Python Program that retrieves the dataset for the "exchequer account (historical series)" from the CSO API
# and stores it into a file called "cso.json"

# Import dependencies
import requests
import json

# Exchequer account API URL
exchequer_url = "https://ws.cso.ie/public/api.jsonrpc?data=%7B%22jsonrpc%22:%222.0%22,%22method%22:%22PxStat.Data.Cube_API.ReadDataset%22,%22params%22:%7B%22class%22:%22query%22,%22id%22:%5B%5D,%22dimension%22:%7B%7D,%22extension%22:%7B%22pivot%22:null,%22codes%22:false,%22language%22:%7B%22code%22:%22en%22%7D,%22format%22:%7B%22type%22:%22JSON-stat%22,%22version%22:%222.0%22%7D,%22matrix%22:%22FIQ02%22%7D,%22version%22:%222.0%22%7D%7D"
#
#  get and save the urlresponse as a json file
response = requests.get (exchequer_url)
exchequer_account = response.json()
print (exchequer_account)

# Save the response to a file and open as ex
with open ("cso.json", "w") as ex:
 json.dump(exchequer_account, ex)