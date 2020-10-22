import requests
import json

response = requests.get('https://api.github.com/')
api_response = json.loads(response.text)
value = api_response.values()

requireparameters = []
noparameters = []

for api in value:
    if "{" in api:
        requireparameters.append(api)
    else:
        noparameters.append(api)


def create_text(text_name, param):
    """
    :param text_name: LT -> Teksto pavadinimas.
    :param param: LT -> Perduodami tekstiniai duomenys.
    :return: LT -> Gražina ir sukuria tekstinį ar kitą failą.
    """
    with open(text_name, "w") as file:
        file.write("\n".join(param))


create_text("AllPossibleGitHubAPI.txt",api_response)
create_text("AllPossibleGitHubAPI_requireparameters.txt", requireparameters)
create_text("AllPossibleGitHubAPI_noparameters.txt", noparameters)
