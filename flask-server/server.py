from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
EMISSION_FACTORS = {
    "India": {
        "Transportation": 0.14,
        "Electricity": 0.82,
        "Diet": 1.25,
        "Waste": 0.1
    }
}

@app.route('/')
def home():
    return "Hello, World!"
@app.route('/login')
def login():
    return "Login Page"

@app.route('/signup')
def signup():
    return "Signup Page"

@app.route('/calculate', methods=['POST'])
def calculate_emissions():
    data = request.get_json()
    country = data['country']
    distance = float(data['distance']) * 365
    electricity = float(data['electricity']) * 12
    meals = float(data['meals']) * 365
    waste = float(data['waste']) * 52

    transportation_emissions = EMISSION_FACTORS[country]["Transportation"] * distance
    electricity_emissions = EMISSION_FACTORS[country]["Electricity"] * electricity
    diet_emissions = EMISSION_FACTORS[country]["Diet"] * meals
    waste_emissions = EMISSION_FACTORS[country]["Waste"] * waste

    total_emissions = round(
        transportation_emissions + electricity_emissions + diet_emissions + waste_emissions, 2
    )

    return jsonify({
        'transportation_emissions': round(transportation_emissions / 1000, 2),
        'electricity_emissions': round(electricity_emissions / 1000, 2),
        'diet_emissions': round(diet_emissions / 1000, 2),
        'waste_emissions': round(waste_emissions / 1000, 2),
        'total_emissions': total_emissions
    })


if __name__ == '__main__':
    app.run(debug=True)