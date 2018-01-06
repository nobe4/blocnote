import requests
import json

token =  ""
moreFiles = True

while moreFiles:
    response = requests.get("https://slack.com/api/files.list", params={"token":token})

    data = json.loads(response.content)
    moreFiles = int(data['paging']['total']) > 0
    print data['paging']

    for file in data["files"]:
        response = requests.get("https://slack.com/api/files.delete", params={"token":token, "file":file["id"]})
        print file["id"], response.content
