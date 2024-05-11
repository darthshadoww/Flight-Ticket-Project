import csv
import os
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Load Data
airports = pd.read_csv('data/airports.csv')
flights = pd.read_csv('data/flights.csv')

# Dosyanın içeriğini temizleme işlevi
def clear_user_info_csv():
    with open('user_info.csv', mode='w', newline='') as file:
        pass
# Fonksiyon kullanıcı bilgilerini CSV dosyasına kaydedecek
def save_user_info_to_csv(user_info, flight_info):
    file_exists = os.path.isfile('user_info.csv')
    with open('user_info.csv', mode='a', newline='') as file:
        fieldnames = list(user_info.keys()) + list(flight_info.keys())
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Dosya boşsa başlık satırını yaz
        if not file_exists:
            writer.writeheader()

        # Kullanıcı ve uçuş bilgilerini yaz
        row = {**user_info, **flight_info}
        writer.writerow(row)


# Flask uygulaması başladığında dosyanın içeriğini temizleyin
clear_user_info_csv()

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
    selected_flight_id = request.form.get('flight_id')

    # Find the specific flight details
    selected_flight = flights[flights['id'] == int(selected_flight_id)]

    return render_template('book.html', flight=selected_flight.to_dict(orient='records')[0])



@app.route('/congrats', methods=['POST'])
def congrats():
    # Kullanıcı tarafından girilen bilgileri al
    name = request.form['name']
    surname = request.form['surname']
    card_number = request.form['card_number']
    expiry_date = request.form['expiry_date']
    cvv = request.form['cvv']
    email = request.form['email']

    # Uçuş bilgilerini al
    origin = request.form['origin']
    destination = request.form['destination']
    company = request.form['company']
    id = request.form['id']
    price = request.form['price']

    # Kullanıcı ve uçuş bilgilerini birleştir
    user_info = {
        'Name': name,
        'Surname': surname,
        'Card Number': card_number,
        'Expiry Date': expiry_date,
        'CVV': cvv,
        'Email': email
    }
    flight_info = {
        'Origin': origin,
        'Destination': destination,
        'Company': company,
        'Flight Id': id,
        'Price': price
    }

    # CSV dosyasına kullanıcı ve uçuş bilgilerini kaydet
    save_user_info_to_csv(user_info,flight_info)

    return render_template('congrats.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True,port=8080)
