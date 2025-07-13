from flask import Flask, request, render_template
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

app = Flask(__name__)

# Dummy dataset
data = pd.DataFrame([
    [1, 1, 1, 1, 1, 'Flu'],
    [1, 1, 1, 0, 0, 'Common Cold'],
    [0, 0, 1, 1, 0, 'Migraine'],
    [0, 0, 1, 0, 1, 'Food Poisoning'],
    [0, 0, 0, 1, 1, 'Dengue'],
], columns=['fever', 'cough', 'fatigue', 'headache', 'nausea', 'disease'])

X = data.drop('disease', axis=1)
y = data['disease']

model = DecisionTreeClassifier()
model.fit(X, y)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_data = {
        'fever': int(request.form.get('fever', 0)),
        'cough': int(request.form.get('cough', 0)),
        'fatigue': int(request.form.get('fatigue', 0)),
        'headache': int(request.form.get('headache', 0)),
        'nausea': int(request.form.get('nausea', 0)),
    }
    
    if all(value == 0 for value in input_data.values()):
        prediction = 'You are fit!'
    else:
        df = pd.DataFrame([input_data])
        prediction = model.predict(df)[0]
    
    return render_template('index.html', prediction_text=f'Predicted Disease: {prediction}')

if __name__ == '__main__':
    print("Flask app is abt to start...")
    app.run(debug=True)
