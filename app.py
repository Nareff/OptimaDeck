from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/config")
def config():
    secret_key = os.getenv("SECRET_KEY")
    return f"Current secret key: {secret_key}"

@app.route("/run")
def run():
    cmd = request.args.get("cmd")
    os.system(cmd)
    return f"Executed: {cmd}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)