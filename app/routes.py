from flask import render_template
from app import app

@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Martin"}
    posts = [
        {
            "author": {"username": "Martin"},
            "body": "Another sunny day in Boulder!"
        },
        {
            "author": {"username": "Martin"},
            "body": "Ready for Game of Thrones!"
        }
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)
