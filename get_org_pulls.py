import requests
import json
import os

def get_token_info():
    return {'Authorization': 'token %s' % os.environ['GITHUB_TOKEN'] }

def get_repo_names(url, headers):
    organization_data = requests.get(url, headers).json()
    return [organization_data[index][u'name'] for (index, item) in enumerate(organization_data)]

def get_pull_requests(repo_names, headers):
    return [requests.get('https://api.github.com/repos/lodash/{}/pulls'.format(repo), headers).json() for repo in repo_names]

if __name__ == '__main__':
    headers = get_token_info()
    repo_names = get_repo_names('https://api.github.com/orgs/lodash/repos', headers)
    pull_requests = get_pull_requests(repo_names, headers)
    for item in pull_requests:
        print(json.dumps(item, indent=2))
        
