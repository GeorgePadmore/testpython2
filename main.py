from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    secret = "notfound"
    return "Home sweet home"



if __name__ == "__main__":
    app.run(debug=True)



