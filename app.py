# dbs prediction

from flask import *
import joblib
from groq import Groq
import os

#delete this before syn

model = Groq()
modelPKL = joblib.load("dbs.pkl")

app = Flask(__name__)

@app.route("/")
def index():
    return(render_template("index.html"))

@app.route("/main", methods=["POST"])
def main(): 
    q = request.form.get("q")
    return(render_template("main.html", q=q))

@app.route("/dbs", methods=["POST"])
def dbs():
    return(render_template("dbs.html"))

@app.route("/chatbot", methods=["POST"])
def chatbot():
    return(render_template("chatbot.html"))

@app.route("/result", methods=["POST"])
def result():
    q = float(request.form.get("q"))
    r = result = modelPKL.predict([[q]])
    return(render_template("result.html",r=r[0][0]))

@app.route("/chatResult", methods=["POST"])
def chatResult():
    q = request.form.get("q")
    r = r = model.chat.completions.create(model = 'openai/gpt-oss-120b',messages = [
        {'role': 'user', 'content': q}])

    return(render_template("chatResult.html",r=r.choices[0].message.content))

if __name__ == "__main__":
    app.run()