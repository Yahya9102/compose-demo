from flask import Flask
import requests

app = Flask(__name__)

@app.route("/hello", methods=["GET"])
def get_message():
    reponse = requests.get("http://app2:5000/message")
    data = reponse.json()
    return {
        "from": "app1",
        "message": "Hej från app1",
        "app2_response": data
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

