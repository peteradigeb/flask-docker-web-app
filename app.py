from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello Peter ?</h1><p>This Flask app is running inside Docker ?</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
