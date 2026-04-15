from flask import Flask
import requests

app = Flask(__name__)

@app.route("/message", methods=["GET"])
def get_message():
    
    #reponse = requests.get("http://app3:5000/message")
    #app3_data = reponse.json()
    return {
        "from": "app2",
        "message": "Hej från app2",
       # "app2_response": app3_data
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

