import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/callback", methods=["POST"])
def callback():
    return "OK", 200  # LINE needs a 200 response

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Use Railway's assigned port
    app.run(host="0.0.0.0", port=port)
