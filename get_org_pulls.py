import requests
import json

def get_repo_names(url):
    organization_data = requests.get(url).json()
    return [organization_data[index][u'name'] for (index, item) in enumerate(organization_data)]

def get_pull_requests(repo_names):
    return [requests.get('https://api.github.com/repos/lodash/{}/pulls'.format(repo)).json() for repo in repo_names]

if __name__ == '__main__':
    repo_names = get_repo_names('https://api.github.com/orgs/lodash/repos')
    pull_requests = get_pull_requests(repo_names)
    for item in pull_requests:
        print(item)
        print("\n")
