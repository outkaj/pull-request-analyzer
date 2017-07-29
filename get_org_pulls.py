import requests
import json
# for each repository, list all pull requests

organization_data = requests.get('https://api.github.com/orgs/lodash/repos').json()
repo_names = []
for index, item in enumerate(organization_data):
    repo_names.append(organization_data[index][u'name'])
print(repo_names)
pull_requests = []
for repo in repo_names:
    request = requests.get('https://api.github.com/repos/lodash/{}/pulls'.format(repo))
    pull_requests.append(request.json())
print(pull_requests)
