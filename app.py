import pandas as pd
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Load Data
airports = pd.read_csv('data/airports.csv')
flights = pd.read_csv('data/flights.csv')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        origin = request.form['origin']
        destination = request.form['destination']

        available_flights = flights[(flights['origin'] == origin) &
                                    (flights['destination'] == destination)]

        return render_template('pick-flights.html', flights=available_flights.to_dict(orient='records'))

    return render_template('index.html', airports=airports.to_dict(orient='records'), flight=None)


@app.route('/book', methods=['POST'])
def book():
    selected_flight_id = request.form.get('id')

    # Find the specific flight details
    selected_flight = flights[flights['id'] == selected_flight_id]

    return render_template('book.html', flight=selected_flight.to_dict(orient='records'))


@app.route('/congrats', methods=['POST'])
def congrats():
    # Extract booking details from request.form 

    # ... (Validation, payment processing, email would happen here)

    return render_template('congrats.html')


if __name__ == '__main__':
    app.run(debug=True,port=8080)
