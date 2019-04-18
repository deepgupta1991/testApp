# app = Flask(__name__)
#
#
# @app.route('/')
# def hello():
#     return "Hello World!"
#
# if __name__ == '__main__':
#     app.run()
from flask import Flask, request, render_template
from flask_restful import reqparse, abort, Api, Resource
import pickle
import pandas as pd
import numpy as np
import s3fs
from sklearn.externals import joblib

app = Flask(__name__)

@app.route('/')
def load_model():
    return render_template('index.html')

    #clf_path = ('lib/models/Voting')
    #list_file=pickle.load(clf_path)



# @app.route('/')
# def my_form():
#     return render_template('form.html')



@app.route('/',methods = ['GET', 'POST'])
def my_form_post():
    if request.method == 'GET':
        return redirect(url_for('/'))
    else:
        ifile= open('model/Voting','rb',buffering=0)
        a = pickle.load(ifile)
        values = request.form.getlist('email')
        values = np.reshape(values, (1, 6))
        predictions = a.predict(values)
        predictions = pd.Series(predictions)
        predictions=predictions.map({0:'Interested in Home appliances',1:'Interested in Gifts',3:'Interested in Merchendize',4:'Interested in luxury items',5:'Low Monetory Value',6:'High Average Transaction',7:'Very High Transaction',8:'Bulk Buyer',9:'High Monetory Value',10:'Very High Monetory Value'})
        return render_template('index.html',
                               values=predictions,array=values)

if __name__ == '__main__':
    app.run()