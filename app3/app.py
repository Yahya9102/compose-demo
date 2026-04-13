from flask import Flask

app = Flask(__name__)

@app.route("/message", methods=["GET"])
def get_message():
    return {
        "from": "app3",
        "message": "Hej från app3"
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

