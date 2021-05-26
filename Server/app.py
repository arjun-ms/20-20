#Imports
from flask import Flask, render_template, request,jsonify
from werkzeug.utils import redirect
import os
import predict


#Init
app = Flask(__name__)

#Routes

###Home

@app.route("/")
def hello():

    return render_template("index.html")

###Upload
@app.route("/upload", methods=["POST"])
def upload():
    file = request.files
    file = file.to_dict(flat=False)
    file = file['myFile'][0]
    file_ext = file.filename
    file_ext = file_ext.split(".")[1]
    if file_ext not in ["jpg", "png", "jpeg", "JPG", "PNG", "JPEG"]:
        print('Not Supported')
        return jsonify('Accepting only "jpg", "png", "jpeg" formats')
    else:
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'uploads', file.filename)
        file.save(file_path)
    result = predict.predict(file_path)
    os.remove(file_path)
    return jsonify(result)

#Run
if __name__ == "__main__":
    app.run()
