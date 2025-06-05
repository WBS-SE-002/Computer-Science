from flask import Flask

app = Flask(__name__)

@app.route("/todo")
def hello():
    return '<h1>Salut</h1>'


@app.route("/posts")
def greeting():
    return 'Here are some posts'