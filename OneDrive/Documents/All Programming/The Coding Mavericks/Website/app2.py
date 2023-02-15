from flask import Flask,render_template,request
import pickle
import numpy as np
import predictor as pred
app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def index():
    symptom_list = [
        'Itching',	
        'Skin Rash',
        'Nodal Skin Eruptions',	
        'Continuous Sneezing',	
        'Shivering',	
        'Chills',	
        'Joint Pain',	
        'Stomach Pain',	
        'Acidity',	
        'Ulcers On Tongue',	
        'Muscle Wasting',	
        'Vomiting',	
        'Burning Micturition',	
        'Spotting Urination',	
        'Fatigue',	
        'Weight Gain',	
        'Anxiety',	
        'Cold Hands And Feets',	
        'Mood Swings',	
        'Weight Loss',	
        'Restlessness',	
        'Lethargy',	
        'Patches In Throat',	
        'Irregular Sugar Level',	
        'Cough',	
        'High Fever',
        'Sunken Eyes',	
        'Breathlessness',	
        'Sweating',	
        'Dehydration',	
        'Indigestion',	
        'Headache',	
        'Yellowish Skin',	
        'Dark Urine',	
        'Nausea',	
        'Loss Of Appetite',	
        'Pain Behind The Eyes',	
        'Back Pain',	
        'Constipation',	
        'Abdominal Pain',	
        'Diarrhoea',	
        'Mild Fever',	
        'Yellow Urine',	
        'Yellowing Of Eyes',	
        'Acute Liver Failure',	
        'Fluid Overload',	
        'Swelling Of Stomach',	
        'Swelled Lymph Nodes',	
        'Malaise',	
        'Blurred And Distorted Vision',	
        'Phlegm',	
        'Throat Irritation',	
        'Redness Of Eyes',	
        'Sinus Pressure',	
        'Runny Nose',	
        'Congestion',	
        'Chest Pain',	
        'Weakness In Limbs',	
        'Fast Heart Rate',	
        'Pain During Bowel Movements',	
        'Pain In Anal Region',
        'Bloody Stool',	
        'Irritation In Anus',	
        'Neck Pain',	
        'Dizziness',	
        'Cramps',	
        'Bruising',	
        'Obesity',	
        'Swollen Legs',	
        'Swollen Blood Vessels',	
        'Puffy Face And Eyes',	
        'Enlarged Thyroid',	
        'Brittle Nails',	
        'Swollen Extremeties',	
        'Excessive Hunger',	
        'Extra Marital Contacts',	
        'Drying And Tingling Lips',	
        'Slurred Speech',	
        'Knee Pain',	
        'Hip Joint Pain',
        'Muscle Weakness',	
        'Stiff Neck',
        'Swelling Joints',	
        'Movement Stiffness',	
        'Spinning Movements',	
        'Loss Of Balance',	
        'Unsteadiness',	
        'Weakness Of One Body Side',	
        'Loss Of Smell',
        'Bladder Discomfort',	
        'Foul Smell Of Urine',	
        'Continuous Feel Of Urine',	
        'Passage Of Gases',	
        'Internal Itching',	
        'Toxic Look (Typhos)',	
        'Depression',
        'Irritability',	
        'Muscle Pain',	
        'Altered Sensorium',	
        'Red Spots Over Body',	
        'Belly Pain',
        'Abnormal Menstruation',	
        'Dischromic  Patches',	
        'Watering From Eyes',
        'Increased Appetite',
        'Polyuria',	
        'Family History',	
        'Mucoid Sputum',	
        'Rusty Sputum',	
        'Lack Of Concentration',	
        'Visual Disturbances',	
        'Receiving Blood Transfusion',	
        'Receiving Unsterile Injections',	
        'Coma',	
        'Stomach Bleeding',	
        'Distention Of Abdomen',	
        'History Of Alcohol Consumption',	
        'Fluid Overload',
        'Blood In Sputum',	
        'Prominent Veins On Calf',	
        'Palpitations',	
        'Painful Walking',	
        'Pus Filled Pimples',	
        'Blackheads',	
        'Scurring',	
        'Skin Peeling',	
        'Silver Like Dusting',	
        'Small Dents In Nails',
        'Inflammatory Nails',
        'Blister',	
        'Red Sore Around Nose',	
        'Yellow Crust Ooze'
    ]

    return render_template('home.html, data=symptom_list')

@app.route('/predict',methods=['GET','POST'])
def predict():
    symptom=request.form['symptoms']
    symptom_list=symptom.split(',')
    prediction=pred.predictDisease(symptom_list)
    return render_template("prediction.html",data=prediction)


if __name__=="__main__":
    app.run()	
