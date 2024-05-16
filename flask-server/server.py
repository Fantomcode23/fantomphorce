from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_login import login_user, current_user, LoginManager
from models import User, Emission
from database import db
import os

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
        return render_template('calculator.html')
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
        'total_emissions': round(total_emissions / 1000, 2)
    })
    else:
        emission = Emission.query.filter_by(user_id=current_user.id).first()
        if emission:
            print(emission)
            return render_template('calculate.html', emission=emission)
        else:
            return render_template('calculate.html')


if __name__ == '__main__':
    app.run(debug=True)