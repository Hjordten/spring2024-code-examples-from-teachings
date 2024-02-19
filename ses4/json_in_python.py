import requests 
import json
import os
import subprocess

# URL of the API endpoint
url = 'https://api.github.com/orgs/python-elective-kea/repos'

# Send a GET request to the URL and get the content
response = requests.get(url)

# Parse the JSON response
data = json.loads(response.text)

# Extract the clone URLs and store them in a list
clone_urls = [repo['clone_url'] for repo in data]

# Create a new folder for cloning the repositories
new_folder = 'cloned_repos'
os.makedirs(new_folder, exist_ok=True)

# Change the current working directory to the new folder
os.chdir(new_folder)

# Clone each repository into the new folder
for clone_url in clone_urls:
    subprocess.run(['git', 'clone', clone_url])
