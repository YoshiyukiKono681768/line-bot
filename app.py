from flask import Flask, request

app = Flask(__name__)

@app.route("/callback", methods=["POST"])
def callback():
    return "OK", 200  # LINE requires a 200 response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
