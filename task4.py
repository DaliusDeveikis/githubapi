from task2 import conn

for repo in conn.search_repositories("microsoft dotnet"):
    print(repo)
