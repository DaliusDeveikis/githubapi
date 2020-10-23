from github import Github
from config import my_api_key

conn = Github(my_api_key)

repository = conn.get_user().get_repos()

for repo in repository:
    print(repo.name)
