# dbs prediction

from flask import *
import joblib

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

@app.route("/result", methods=["POST"])
def result():
    q = float(request.form.get("q"))
    r = result = modelPKL.predict([[q]])
    return(render_template("result.html",r=r[0][0]))

if __name__ == "__main__":
    app.run()