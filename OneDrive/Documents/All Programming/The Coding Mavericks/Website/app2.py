from flask import Flask,render_template,request
import pickle
import numpy as np
import predictor as pred
app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def index():
    symptom-list = [
        'itching'	
        skin_rash
        nodal_skin_eruptions	
        continuous_sneezing	
        shivering	
        chills	
        joint_pain	
        stomach_pain	
        acidity	ulcers_on_tongue	
        muscle_wasting	
        vomiting	
        burning_micturition	
        spotting_ urination	
        fatigue	
        weight_gain	
        anxiety	
        cold_hands_and_feets	
        mood_swings	
        weight_loss	
        restlessness	
        lethargy	
        patches_in_throat	
        irregular_sugar_level	
        cough	
        high_fever	
        sunken_eyes	
        breathlessness	
        sweating	
        dehydration	
        indigestion	
        headache	
        yellowish_skin	
        dark_urine	
        nausea	
        loss_of_appetite	
        pain_behind_the_eyes	
        back_pain	
        constipation	
        abdominal_pain	
        diarrhoea	
        mild_fever	
        yellow_urine	
        yellowing_of_eyes	
        acute_liver_failure	
        fluid_overload	
        swelling_of_stomach	
        swelled_lymph_nodes	
        malaise	
        blurred_and_distorted_vision	
        phlegm	
        throat_irritation	
        redness_of_eyes	
        sinus_pressure	
        runny_nose	
        congestion	
        chest_pain	
        weakness_in_limbs	
        fast_heart_rate	
        pain_during_bowel_movements	
        pain_in_anal_region	
        bloody_stool	
        irritation_in_anus	
        neck_pain	
        dizziness	
        cramps	
        bruising	
        obesity	
        swollen_legs	
        swollen_blood_vessels	
        puffy_face_and_eyes	
        enlarged_thyroid	
        brittle_nails	
        swollen_extremeties	
        excessive_hunger	
        extra_marital_contacts	
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
        'Yellow Crust Ooze',	








    ]

    return render_template('home.html, data=symptom-list')

@app.route('/predict',methods=['GET','POST'])
def predict():
    symptom=request.form['symptoms']
    symptom_list=symptom.split(',')
    prediction=pred.predictDisease(symptom_list)
    return render_template("prediction.html",data=prediction)


if __name__=="__main__":
    app.run()
