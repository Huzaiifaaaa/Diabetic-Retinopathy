from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def Index():
    return render_template("Index.html")

@app.route("/Glaucoma")
def Glaucoma():
    return render_template("Glaucoma.html")

@app.route("/DiabeticRetinopathy")
def DiabeticRetinopathy():
    return render_template("DiabeticRetinopathy.html")



app.run()