# Assignment 4

# import dependencies
from github import Github
import requests 
import json 
import re
from config import apikeys as cfg

apikey = cfg["githubkeyab"] # import the api key from the config file

g = Github(apikey)

#ab_repo = g.get_repo("Gtalen/wsaa-course-material-2024")



apikey = cfg["githubkeyab"] # import the api key from the config file

url = "https://api.github.com/repos/Gtalen/wsaa-course-material-2024"

#url = "https://api.github.com/users/andrewbeattycourseware/repos?perpage=100"

response = requests.get(url, auth = ("token", apikey)) 
print (response.status_code) #check if response is succesful

responses = response.text #convert the response to json format
print (responses) #print response 

ab_response = responses.replace("andrew", "ebele") #replace andrew with ebele in the response

# Save the response to a file and open as ab
with open ("ab_response.json", "w") as ab:  # open file in write mode
 json.dump(ab_response, ab, indent=4)  # save the JSON data to the file




