from github import Github

conn = Github("your_token")

repository = conn.get_user().get_repos()

for repo in repository:
    print(repo.name)
