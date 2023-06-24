import requests
import json

return_ans= requests.get("http://api.open-notify.org/astros.json")

space_humans=return_ans.json()["number"]
print(f"number of space humans: {space_humans}")

print("Number of space humans is:")
print("---------------------")

for x in return_ans.json()["people"]:
    print(x)