from flask import Flask

app = Flask(__name__)

@app.route("/")
def Hello():
    return "Hello, Sumathi!"

if __name__ == 'main':
    app.run()