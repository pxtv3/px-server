from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "PX MODZ SERVER RUNNING"

app.run(host="0.0.0.0", port=5000)