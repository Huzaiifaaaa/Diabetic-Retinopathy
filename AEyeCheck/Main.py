from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import os
import requests

import utils
import Predict

ALLOWED_EXTENSIONS = set(['jpeg'])
COARSE_GRAIN_PATH=r"C:\Users\huzai\Documents\GitHub\Diabetic-Retinopathy\AEyeCheck\static\model\cgc.pth"
FINE_GRAIN_PATH=r"C:\Users\huzai\Documents\GitHub\Diabetic-Retinopathy\AEyeCheck\static\model\fgc.pth"

#ngrok authtoken 2PQqFoWUiz9rGfLIrGgp8TYKU9G_61bT7NdRcBSGNucQsYiao
#ngrok http h5000

app = Flask(__name__)
app.secret_key = 'naseerbajwa'
apitoken="naseerbajwa"

@app.route("/api", methods=['GET', 'POST'])
def api():
    if request.method == 'POST':
        module = request.args.get("module")
        token = request.args.get("token")
        imagepath = request.args.get("imagepath")
        image_file = request.files["image"]

        if image_file and utils.allowed_files(image_file.filename, ALLOWED_EXTENSIONS) and (module=="DiabeticRetinopathy" or module=="Glaucoma") and token==apitoken:
            filename = secure_filename(image_file.filename)
            filename=utils.get_unique_filename(module)
            if module=="DiabeticRetinopathy":
                image_file.save(os.path.join(r'AEyeCheck\static\input\diabeticretinopathy', filename))
                session['apiimagepath'] = os.path.join(r'\static\input\diabeticretinopathy', filename)
            else:
                return "Invalid Request"
            
            return Predict.predict(module, session['apiimagepath'])

        else:
            return "Invalid Token or Module"

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

@app.route('/upload', methods = ['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        if f and utils.allowed_files(f.filename, ALLOWED_EXTENSIONS):
            filename = secure_filename(f.filename)
            filename=utils.get_unique_filename("DiabeticRetinopathy")
            f.save(os.path.join(r'AEyeCheck\static\input\diabeticretinopathy', filename))
            session['imagepath'] = os.path.join(r'\static\input\diabeticretinopathy', filename)

            #predict=Predict.Predict("DiabeticRetinopathy", COARSE_GRAIN_PATH,FINE_GRAIN_PATH)
            #predict.predict(session['imagepath'])

            return redirect(url_for('Diagnostics'))
        else:
            return redirect(url_for('DiabeticRetinopathy'))


app.run()