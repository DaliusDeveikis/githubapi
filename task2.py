from github import Github

conn = Github("19124bd913960a2d99747b1af62a9c21569495b8")

repository = conn.get_user().get_repos()

for repo in repository:
    print(repo.name)
