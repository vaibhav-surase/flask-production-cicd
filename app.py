from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Version 2 deployed using CI/CD!"

@app.route("/health")
def health():
    return "Healthy"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
