from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import os
import requests

import utils

ALLOWED_EXTENSIONS = set(['jpeg'])

#2PQqFoWUiz9rGfLIrGgp8TYKU9G_61bT7NdRcBSGNucQsYiao
#ngrok authtoken 1xre3GrEK8vyPrBcae6s14QNaHb_4pG96LviFgkzV2uKGsouJ
#ngrok http https://localhost:5000 -host-header="localhost:5000"

app = Flask(__name__)
app.secret_key = 'naseerbajwa'
#app.config['UPLOAD_FOLDER'] = 'AEyeCheck/input/diabeticretinopathy'

@app.route("/")
def Index():
    return render_template("Index.html")

@app.route("/Glaucoma")
def Glaucoma():
    return render_template("Glaucoma.html")

@app.route("/DiabeticRetinopathy")
def DiabeticRetinopathy():
    return render_template("DiabeticRetinopathy.html")

@app.route("/Diagnostics")
def Diagnostics():
    if session['imagepath']:
        return render_template("Diagnostics.html", uploadedimage = session['imagepath'])
    else:
        return redirect(url_for('Index'))

@app.route('/drupload', methods = ['GET', 'POST'])
def drupload():
    if request.method == 'POST':
        f = request.files['file']
        if f and utils.allowed_files(f.filename, ALLOWED_EXTENSIONS):
            filename = secure_filename(f.filename)
            filename=utils.get_unique_filename("DiabeticRetinopathy")
            f.save(os.path.join(r'AEyeCheck\static\input\diabeticretinopathy', filename))
            session['imagepath'] = os.path.join(r'\static\input\diabeticretinopathy', filename)
            return redirect(url_for('Diagnostics'))
        else:
            return redirect(url_for('DiabeticRetinopathy'))


app.run()