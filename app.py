# dbs prediction

from flask import *

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

if __name__ == "__main__":
    app.run()