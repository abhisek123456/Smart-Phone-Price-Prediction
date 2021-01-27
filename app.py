from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
knn = pickle.load(open('KNN_hyper_14.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')



@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        ram = int(request.form['ram'])
        battery_power = int(request.form['battery_power'])
        #px_height = int(request.form['px_height'])
        #mobile_wt  = int(request.form['mobile_wt'])
        int_memory = int(request.form['int_memory'])
        n_cores = int(request.form['n_cores'])
        #fc = int(request.form['fc'])
        
        data =[ram,battery_power,int_memory,n_cores]
        data= np.array(data)
        data =data.reshape(1,-1)
        my_prediction = knn.predict(data)
        output=my_prediction
        if output==0:
         return render_template('index.html',prediction_text="Mobile price range is under Rs 5000" )
        elif output==1:
         return render_template('index.html',prediction_text="Mobile price range is under Rs 7000" )
        elif output==2:
         return render_template('index.html',prediction_text="Mobile price range is under Rs 10000")
        else:
         return render_template('index.html',prediction_text="Mobile price range is under Rs 15000")
    else:
        return render_template('index.html')
        
     
if __name__=="__main__":
    app.run(debug=True)
