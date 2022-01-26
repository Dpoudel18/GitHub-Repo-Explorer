import json
import requests
import sys
from time import sleep
from config import *

user_name = username
token = token_key

def get_data_files(username,repo_name, component):
    """
    Returns all the contributors of the specified repository
    """
    if component == 'issues' or component == 'pulls': # get both open and closed issues and pull requests
        url = f"https://api.github.com/repos/{username}/{repo_name}/{component}?state=all&simple=yes&per_page=100&page=1"

    else:
        url = f"https://api.github.com/repos/{username}/{repo_name}/{component}?simple=yes&per_page=100&page=1"

    response = requests.get(url,auth=(user_name,token)) # use authorized token for get endpoint

    print(url)

    if str(response) == '<Response [403]>': # check for api limit error
        return 'API request limit exceeded'

    if str(response) == '<Response [404]>': # check for invalid url paramaters/arguments
        return 'Invalid url parameters'  

    json_response = response.json() # store the json response 

    try:
        while 'next' in response.links.keys(): # iterate through each page and add the response to 'json_response'
            print('Pulling data from ' + response.links['next']['url'])
            remaining_api_calls = requests.get('https://api.github.com/rate_limit', auth=(user_name,token)).json()['rate']['remaining']
            print("remaining_api_calls: ",remaining_api_calls)
            if remaining_api_calls == 1:
                sleep(3600)
            response = requests.get(response.links['next']['url'],auth=(user_name,token))
            json_response.extend(response.json())
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")

    if component == 'issues':
        with open(f'json_response/{component}_and_pulls.json', 'w', encoding='utf-8') as f: # store the output as a JSON file
            json.dump(json_response, f, ensure_ascii=False, indent=4)
    else:
        with open(f'json_response/{component}.json', 'w', encoding='utf-8') as f: # store the output as a JSON file
            json.dump(json_response, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    github_username = 'pandas-dev'
    repo_name = 'pandas'
    components = ['milestones']#['contributors','commits','issues', 'milestones']
    for component in components:
        get_data_files(github_username,repo_name, component)
