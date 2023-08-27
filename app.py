# main.py
import numpy as np
import pandas as pd
from flask import Flask, jsonify, request, render_template
import pickle

app = Flask(__name__)

preprocessor_path = 'preprocessing_pipeline.pkl'
model_path = 'model.pkl'

with open(model_path, "rb") as file_obj:
    model = pickle.load(file_obj)

print(model)

labels_ordered = {'Houston': 0, 'Los Angeles': 1,
                  'Chicago': 2, 'Miami': 3, 'New York': 4}


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "GET":
        return render_template('index.html', Locations=['Los Angeles', 'New York', 'Miami', 'Chicago', 'Houston'])

    else:
        print("submitted")

        try:

            age = int(request.form.get('selected_age')),

        except:
            return render_template('home.html', Locations=['Los Angeles', 'New York', 'Miami', 'Chicago', 'Houston'], result="Please make sure that the input is in correct format")

        try:
            location = request.form.get('selected_Location'),

        except:
            return render_template('home.html', Locations=['Los Angeles', 'New York', 'Miami', 'Chicago', 'Houston'], result="Please make sure that the input is in correct format")

        try:
            M_Bill = float(request.form.get('selected_M_Bill')),

        except:
            return render_template('home.html', Locations=['Los Angeles', 'New York', 'Miami', 'Chicago', 'Houston'], result="Please make sure that the input is in correct format")

        print(age[0], location[0], M_Bill[0])

        print("Before Prediction")

        fea_df = pd.DataFrame([[age[0], location[0], M_Bill[0]]], columns=[
                              'Age', 'Location', 'Monthly_Bill'])

        fea_df['Location'] = fea_df['Location'].map(labels_ordered)

        print(fea_df.info())

        pred = model.predict(fea_df)

        print(pred[0])

        def display_string(digit):
            if digit == 0:
                return 'NO (0)'

            else:
                return 'YES (1)'

        result = display_string(pred[0])

        return render_template('home.html', Locations=['Los Angeles', 'New York', 'Miami', 'Chicago', 'Houston'], result=result)


if __name__ == '__main__':
    app.run(host="0.0.0.0", threaded=True, debug=True)
