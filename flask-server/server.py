from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_login import login_user, current_user, LoginManager, login_required
from models import User, Emission
from database import db
import os
import sqlite3
from MLprediction import generate_recommendations, recommend_list
import joblib
import numpy as np


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
app.config['SECRET_KEY'] = 'kar-anshul-gaya-aish'

login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user is None or not user.check_password(request.form['password']):
            return 'Invalid username or password'
        login_user(user)
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        user = User(username=request.form['username'])
        user.set_password(request.form['new_password'])
        db.session.add(user)
        db.session.commit()
        return render_template('login.html')
    return render_template('signup.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/calc')
def calc():
    return render_template('calculator.html')

global_averages = {
    "FourWheeler": 4.7,
    "AirTravel": 1.25,
    "Waste": 0.235,
    "Diet": 1.3,
    "Electricity": 2
}


FACTORS = {
    "US": {
    "Car": 0.19,
    "TwoWheeler": 0.06,
    "AirTravel": 0.13,
    "Electricity": 1.02,
    "Diet": 1.8,
    "Waste": 0.2
    },
    "India": {
        "Car": 0.116,
        "TwoWheeler": 0.041,
        "AirTravel": 0.115,
        "Electricity": 0.82,
        "Diet": 1.25,
        "Waste": 0.1
    }
}

@app.route('/calculate', methods=['GET','POST'])
def calculate_emissions():
    if request.method == 'POST':
        data = request.get_json()
        country = data['country']
        car_distance = float(data['car_distance']) * 365
        two_wheeler_distance = float(data['two_wheeler_distance']) * 365
        air_travel_distance = float(data['air_travel_distance']) 
        electricity = float(data['electricity']) * 12
        meals = float(data['meals']) * 365
        waste = float(data['waste']) * 52

        car_emissions = FACTORS[country]["Car"] * car_distance
        two_wheeler_emissions = FACTORS[country]["TwoWheeler"] * two_wheeler_distance
        air_travel_emissions = FACTORS[country]["AirTravel"] * air_travel_distance
        electricity_emissions = FACTORS[country]["Electricity"] * electricity
        diet_emissions = FACTORS[country]["Diet"] * meals
        waste_emissions = FACTORS[country]["Waste"] * waste

        total_emissions = round(
            car_emissions + two_wheeler_emissions + air_travel_emissions + electricity_emissions + diet_emissions + waste_emissions, 2
        )
        emission = Emission.query.filter_by(user_id=current_user.id).first()
        if emission:
            emission.car_emissions = car_emissions
            emission.two_wheeler_emissions = two_wheeler_emissions
            emission.air_travel_emissions = air_travel_emissions
            emission.electricity_emissions = electricity_emissions
            emission.diet_emissions = diet_emissions
            emission.waste_emissions = waste_emissions
            emission.total_emissions = total_emissions
        else:
            emission = Emission(
                user_id=current_user.id,
                car_emissions=car_emissions,
                two_wheeler_emissions=two_wheeler_emissions,
                air_travel_emissions=air_travel_emissions,
                electricity_emissions=electricity_emissions,
                diet_emissions=diet_emissions,
                waste_emissions=waste_emissions,
                total_emissions=total_emissions
            )
            db.session.add(emission)
        db.session.commit()
       
        return jsonify({
        'car_emissions': round(car_emissions / 1000, 2),
        'two_wheeler_emissions': round(two_wheeler_emissions / 1000, 2),
        'air_travel_emissions': round(air_travel_emissions / 1000, 2),
        'electricity_emissions': round(electricity_emissions / 1000, 2),
        'diet_emissions': round(diet_emissions / 1000, 2),
        'waste_emissions': round(waste_emissions / 1000, 2),
        'total_emissions': round(total_emissions / 1000, 2),

    })
    else:
        emission = Emission.query.filter_by(user_id=current_user.id).first()
        if emission:
            print(emission)
            return render_template('calculate.html', emission=emission)
        else:
            return render_template('calculate.html')

@app.route('/emissionpiechart')
def piechart():
    emission = Emission.query.filter_by(user_id=current_user.id).first()
    if emission:
        return render_template('piechart.html', emission=emission)
    else:
        return 'Emission data not found.'

@app.route('/advice')
def advice():
    return render_template('advice.html')

@app.route('/previous-values', methods=['GET'])
def get_previous_values():
    conn = sqlite3.connect('test.db')

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Emission")

    rows = cursor.fetchall()

    previous_values = {row[0]: row[1] for row in rows}

    conn.close()

    return jsonify(previous_values)

@app.route('/mlprediction')
def mlprediction():
    return render_template('mlprediction.html')

@app.route('/ml_emissions', methods=['POST'])
def process_routes():
    num_routes = int(request.json.get('num_routes'))
    routes_data = []
    for i in range(num_routes):
        distance = float(request.json.get(f'distance_{i}'))
        mileage = float(request.json.get(f'mileage_{i}'))
        v_type = int(request.json.get(f'v_type_{i}'))
        routes_data.append((distance, mileage, v_type))
    sorted_routes = process_and_sort_routes(routes_data)
    return jsonify(sorted_routes)

def preprocess_data(distance, mileage, v_type):
    v_type_4 = 1 if v_type == 4 else 0
    sample = np.array([[mileage, distance, v_type_4]])
    return sample

def generate_recommendations(count, distance, mileage, v_type):
    sample = preprocess_data(distance, mileage, v_type)
    prediction = rf_regressor.predict(sample)[0]

    perturbation = (distance) + (10 / mileage)
    adjusted_prediction = prediction + perturbation
    
    recommend_list.append((adjusted_prediction, count))

def process_and_sort_routes(routes_data):
    global recommend_list
    recommend_list = []
    for count, (distance, mileage, v_type) in enumerate(routes_data):
        generate_recommendations(count, distance, mileage, v_type)
    sorted_routes = sorted(recommend_list, key=lambda x: x[0])
    return sorted_routes

rf_regressor = joblib.load('newpicklefile1.pkl')
recommend_list = []


if __name__ == '__main__':
    app.run(debug=True)
