from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_login import login_user
#from models import User

app = Flask(__name__)


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
        return 'Logged in successfully'
    return render_template('login.html')

@app.route('/signup')
def signup():
    return "Signup Page"

@app.route('/calc')
def calc():
    return render_template('calculator.html')

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

@app.route('/calculate', methods=['POST'])
def calculate_emissions():
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

    return jsonify({
        'car_emissions': round(car_emissions / 1000, 2),
        'two_wheeler_emissions': round(two_wheeler_emissions / 1000, 2),
        'air_travel_emissions': round(air_travel_emissions / 1000, 2),
        'electricity_emissions': round(electricity_emissions / 1000, 2),
        'diet_emissions': round(diet_emissions / 1000, 2),
        'waste_emissions': round(waste_emissions / 1000, 2),
        'total_emissions': round(total_emissions / 1000, 2)
    })

if __name__ == '__main__':
    app.run(debug=True)