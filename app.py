from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World, with cloud build-deploy!"
# run the app.
if __name__ == "__main__":
    app.run()
