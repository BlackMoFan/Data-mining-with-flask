from flask import Flask, render_template, request, jsonify, Response
#import pandas as pd
import numpy as np

#------------------------------------
# new from https://www.geeksforgeeks.org/uploading-and-reading-a-csv-file-in-flask/
from distutils.log import debug
from fileinput import filename
import pandas as pd
from flask import *
import os
from werkzeug.utils import secure_filename
 
# local
UPLOAD_FOLDER = os.path.join('staticFiles', 'uploads')

# in pythonanywhere
#UPLOAD_FOLDER = "/home/Inglis/Data-mining-with-flask/staticFiles/uploads"

# Define allowed files
ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__)

# Configure upload file path flask
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
 
app.secret_key = 'This is your secret key to utilize session in Flask'

@app.route('/Act0LoadData/Upload/', methods=['GET', 'POST'])
def uploadFile():
    if request.method == 'POST':
        if 'file' not in request.files:
            # local
            session['uploaded_data_file_path'] = "staticFiles/excelTemplates/Iris.csv"
            # in pythonanywhere
            #session['uploaded_data_file_path'] = "/home/Inglis/Data-mining-with-flask/staticFiles/excelTemplates/Iris.csv"
        else:
            # upload file flask
            f = request.files.get('file')
    
            # Extracting uploaded file name
            data_filename = secure_filename(f.filename)
    
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], data_filename))
    
            session['uploaded_data_file_path'] = os.path.join(app.config['UPLOAD_FOLDER'], data_filename)
        return render_template('activity0FileUploaded.html')
    return render_template("activity0.html")
 
 
@app.route('/Act0LoadData/show_data/')
def showData():
    # Uploaded File Path
    data_file_path = session.get('uploaded_data_file_path', None)
    # read csv
    uploaded_df = pd.read_csv(data_file_path, encoding='unicode_escape')
    # Converting to html Table
    uploaded_df_html = uploaded_df.to_html()
    return render_template('activity0ShowData.html', data_var=uploaded_df_html)
 
 
if __name__ == '__main__':
    app.run(debug=True)
#------------------------------------

# app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ML/')
def ML():
    return render_template('ML.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    select_ = request.form.get('pos_1v1')
    print(select_)
    print('form val: ', request.form.values())
    exp_ = request.form.get('experience')

    int_features = [select_, exp_] 
    final_features = [np.array(int_features)]

    prediction = model.predict(final_features)

    res = prediction.item()

    return render_template('ML.html', prediction_text='Expected Salary Rate should be $ {}'.format(res))

#@app.route('/predict', methods=['POST'])
#def predict():
#
#    int_features = [int(x) for x in request.form.values()]
#    final_features = [np.array(int_features)]
#
#    prediction = model.predict(final_features)
#
#    res = prediction.item()
#
#    return render_template('ML.html', prediction_text='Expected Salary Rate should be $ {}'.format(res))

@app.route('/Act0LoadData/')
def activity0():
    return render_template('activity0.html')

@app.route('/Act1KNN/')
def activity1():
    return render_template('activity1.html')

@app.route('/Act2KMeansClustering/')
def activity2():
    return render_template('activity2.html')

@app.route('/Act3Association/')
def activity3():
    return render_template('activity3.html')

@app.route('/Act4Nbayes/')
def activity4():
    return render_template('activity4.html')

@app.route('/about/')
def about():
    return render_template('about.html')
