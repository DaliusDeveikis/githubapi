import urllib.request
import json
from task1 import api_response, create_text as ct

for keys, values in api_response.items():
    emoji_list = []
    if "emoji" in keys:
        emoji_list.append(values)
        ct("emoji.txt", emoji_list)


def main():
    url_list = []
    listas = []
    with open("emoji.txt") as file:
        a = file.read()
        listas.append(a)
        for i in listas:
            webUrl = urllib.request.urlopen(i)
            data = webUrl.read()
            dict_data = json.loads(data.decode('utf-8'))
            for keys, values in dict_data.items():
                if "lithuania" in keys:
                    url_list.append(values[:-3])
                    ct("lt_flag.txt", url_list)
                else:
                    pass


if __name__ == "__main__":
    main()
