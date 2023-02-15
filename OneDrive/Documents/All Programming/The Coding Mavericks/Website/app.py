from flask import Flask,render_template,request
import pickle
import numpy as np
import predictor as pred
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    symptom=request.form['symptoms']
    symptom_list=symptom.split(',')
    prediction=pred.predictDisease(symptom_list)
    return render_template("prediction.html",data=prediction)

if __name__=="__main__":
    app.run()