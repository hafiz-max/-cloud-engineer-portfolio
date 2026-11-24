
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "project": "Cloud Engineer Portfolio",
        "message": "My first Docker application!",
        "status": "running"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/version")
def version():
    return jsonify({
        "application": "Cloud Engineer Portfolio",
        "version": "1.1.0",
        "environment": "development"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
