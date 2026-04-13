from flask import Flask

app = Flask(__name__)

@app.route("/message", methods=["GET"])
def get_message():
    return {
        "from": "app2",
        "message": "Hej från app2"
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

