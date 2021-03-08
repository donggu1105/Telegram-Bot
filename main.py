import json
from flask import Flask



app = Flask(__name__)

if __name__ == "__main__":
    app.run(host="0,0,0,0", port="8080")


@app.route('/')
def get_bot_info():

    with open("telegram_code.json", "r") as fp:
        api_key = json.load(fp)["telegram_code"]
        print(api_key)