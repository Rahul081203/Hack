import pandas as pd
import pickle
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras

data=pd.read_csv("C:\\Users\\rahul\\OneDrive\\Documents\\All Programming\\The Coding Mavericks\\ML\\dataset\\Training.csv")
data.drop('Unnamed: 133',axis=1,inplace=True)

from sklearn.preprocessing import LabelEncoder
encoder=LabelEncoder()

encoder.fit(data['prognosis'])
data['prognosis']=encoder.transform(data['prognosis'])

features=data.iloc[:,:-1]
target=data.iloc[:,-1]

data_test=pd.read_csv("C:\\Users\\rahul\\OneDrive\\Documents\\All Programming\\The Coding Mavericks\\ML\\dataset\\Testing.csv")
data_test.head()
data_test['prognosis']=encoder.fit_transform(data_test['prognosis'])

x_test=data_test.iloc[:,:-1]
y_test=data_test.iloc[:,-1]

from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.svm import SVC

svm_model = SVC()
svm_model.fit(features, target)
# pickle.dump(svm_model,open('model.pkl','wb'))
# model=pickle.load(open('model.pkl','rb'))
# preds = svm_model.predict(x_test)

symptoms = features.columns.values
 

symptom_index = {}
for index, value in enumerate(symptoms):
    symptom = " ".join([i.capitalize() for i in value.split("_")])
    symptom_index[symptom] = index
 
data_dict = {
    "symptom_index":symptom_index,
    "predictions_classes":encoder.classes_
}
# print(data_dict)
def predictDisease(symptoms):
    input_data = [0] * len(data_dict["symptom_index"])
    for symptom in symptoms:
        index = data_dict["symptom_index"][symptom]
        input_data[index] = 1
         
    input_data = np.array(input_data).reshape(1,-1)
    svm_prediction = data_dict["predictions_classes"][svm_model.predict(input_data)[0]]
    return svm_prediction

# symptoms=str(input("Enter the symptoms separated by comma: "))
# disease=predictDisease(symptoms)
# print(disease)