from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash
import pickle
import numpy as np
import pandas as pd
import os
import json
import warnings
from functools import wraps

warnings.simplefilter('ignore')

app = Flask(__name__)
app.secret_key = 'aeromind_secure_key'

# Mock user database
users = {"admin": "password123"}

# Load model and encoders
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model', 'flight_delay_model.pkl')

def load_resources():
    if os.path.exists(MODEL_PATH):
        with open(MODEL_PATH, 'rb') as f:
            return pickle.load(f)
    return None, None, None, None

model, le_carrier, le_origin, le_dest = load_resources()

# Login required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def home():
    if 'user' in session:
        return redirect(url_for('index'))
    return redirect(url_for('login'))

@app.route('/index')
@login_required
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username in users and users[username] == password:
            session['user'] = username
            return redirect(url_for('index'))
        flash('Invalid username or password', 'error')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username in users:
            flash('Username already exists', 'error')
        else:
            users[username] = password
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/predict', methods=['POST'])
@login_required
def predict():
    if not model:
        return jsonify({'error': 'Model not loaded.'}), 500
    
    try:
        data = request.form
        month = int(data['month'])
        day_of_month = int(data['day_of_month'])
        day_of_week = int(data['day_of_week'])
        crs_dep_time = int(data['crs_dep_time'])
        carrier = data['carrier']
        origin = data['origin']
        dest = data['dest']
        weather_severity = int(data.get('weather_severity', 0))

        def safe_encode(le, val):
            try:
                return le.transform([val])[0]
            except:
                return -1

        carrier_enc = safe_encode(le_carrier, carrier)
        origin_enc = safe_encode(le_origin, origin)
        dest_enc = safe_encode(le_dest, dest)

        feature_names = getattr(model, 'feature_names_in_', ['Month', 'DayofMonth', 'DayOfWeek', 'CRSDepTime', 'UniqueCarrier', 'Origin', 'Dest', 'Distance'])
        features = pd.DataFrame([[month, day_of_month, day_of_week, crs_dep_time, carrier_enc, origin_enc, dest_enc, 500]], columns=feature_names)
        prob = model.predict_proba(features)[0][1]

        weather_boost = weather_severity * 0.20
        final_prob = min(prob + weather_boost, 1.0)
        final_prediction = 1 if final_prob > 0.6 else 0

        result = {
            'prediction': 'High Delay Risk' if final_prediction == 1 else 'Low Delay Risk',
            'probability': f"{final_prob * 100:.2f}%",
            'status': final_prediction,
            'weather_impact': "Critical" if weather_severity >= 2 else ("Elevated" if weather_severity == 1 else "Normal")
        }
        
        return render_template('index.html', result=result, input_data=data)
    
    except Exception as e:
        return render_template('index.html', error=str(e))

@app.route('/analysis')
@login_required
def analysis():
    stats_path = os.path.join(os.path.dirname(__file__), 'data', 'analysis_stats.json')
    stats_data = {}
    if os.path.exists(stats_path):
        with open(stats_path, 'r') as f:
            stats_data = json.load(f)
    return render_template('analysis.html', stats=stats_data)

@app.route('/heatmap')
@login_required
def heatmap():
    stats_path = os.path.join(os.path.dirname(__file__), 'data', 'analysis_stats.json')
    heatmap_data = {}
    if os.path.exists(stats_path):
        with open(stats_path, 'r') as f:
            stats_data = json.load(f)
            heatmap_data = stats_data.get('heatmap_origins', {})
    return render_template('heatmap.html', heatmap_data=heatmap_data)

@app.route('/tips')
@login_required
def tips():
    return render_template('tips.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
