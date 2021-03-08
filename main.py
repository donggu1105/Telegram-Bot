import json
import requests

with open("telegram_code.json", "w") as fp:
    json.dump({"telegram_code" : "1698758222:AAFbYkMBmDck-bP_wi7vlayqyZ5c0rGn5U0"}, fp)


with open("telegram_code.json", "r") as fp:
    api_key = json.load(fp)["telegram_code"]
    url = "https://api.telegram.org/bot" + api_key + "/getUpdates"




response = requests.get(url)
response.json()
result_list = response.json().get("result")

print(result_list)
for result in result_list:
    if result.get("chat") == "chat":
        print("3")