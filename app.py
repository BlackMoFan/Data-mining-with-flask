from flask import Flask, render_template, request, jsonify, Response
#import pandas as pd
import numpy as np

app = Flask(__name__)

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
