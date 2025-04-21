# Assignment 4 - A Python program that reads a file from a repository
# Replaces all occurrences of the text "andrew" with "ebele"
# Commits the updated file back to the repository.

# import dependencies
from github import Github
import requests
from config import apikeys as cfg

# import the api key from the config file
apikey = cfg["githubkey"]

#authenticate with the GitHub API key
g = Github(apikey)

# Access repository with HTTPS GET method
repo = g.get_repo("Gtalen/Authentication-testin")
#print (repo.clone_url) # print the clone url of the repository

file_info = repo.get_contents("ab.txt") # get the contents of the file ab.txt
urloffile = file_info.download_url # get the download url of the file ab.txt
print (urloffile)


response = requests.get(urloffile)
file_content = response.text # get the content of the file ab.txt
#print (file_content)

content_update = file_content.replace("andrew", "ebele") #replace andrew with ebele in the response
#print (file_edit)

# update content of the file on github
repo.update_file(file_info.path, "Replaced andrew with ebele in Ab text file ", content_update, file_info.sha)

# check if the content has changed using a for loop
if file_content != content_update: #
    print("Update committed.")
else:
    print("No changes to commit.")
g = Github(apikey)