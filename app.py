from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/gemini", methods = ["POST"])
def gemini():
    recipe = request.form['recipe_love']
    return recipe