import requests
import json
import os

def get_repo_names(url):
    organization_data = requests.get(url, auth=(os.environ['GITHUB_TOKEN'], 'x-oauth-basic')).json()
    return [organization_data[index][u'name'] for (index, item) in enumerate(organization_data)]

def get_pull_requests(repo_names):
    params = {'state': 'all'}
    return [requests.get('https://api.github.com/repos/lodash/{}/pulls'.format(repo), params, auth=(os.environ['GITHUB_TOKEN'], 'x-oauth-basic')).json() for repo in repo_names]

if __name__ == '__main__':
    repo_names = get_repo_names('https://api.github.com/orgs/lodash/repos')
    pull_requests = get_pull_requests(repo_names)
    for item in pull_requests:
        print(json.dumps(item, indent=2))
