from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():

    city_list = ["İstanbul", "Ankara", "İzmir", "Bursa", "Antalya","Tokat","Amasya","Adana","Samsun"]
    

    return render_template('index.html',city_list = city_list)

@app.route('/book', methods=['POST'])
def book():
    # Bilet bilgilerini içeren bir liste oluşturun
    tickets = [
        {'from': 'İstanbul', 'arrival': 'Ankara', 'time': '13:00', 'date': '12.11.24', 'fee': '150 TL'},
        {'from': 'İzmir', 'arrival': 'Antalya', 'time': '14:30','date':'12.11.24','fee': '200 TL'},
        {'from': 'İzmir', 'arrival': 'Antalya', 'time': '14:30','date':'12.11.24','fee': '200 TL'},
        {'from': 'İzmir', 'arrival': 'Antalya', 'time': '14:30','date':'12.11.24','fee': '200 TL'},
        {'from': 'İzmir', 'arrival': 'Antalya', 'time': '14:30','date':'12.11.24','fee': '200 TL'},
        {'from': 'İstanbul', 'arrival': 'Ankara', 'time': '13:00','date':'12.11.24', 'fee': '150 TL'},
        {'from': 'İzmir', 'arrival': 'Antalya', 'time': '14:30','date':'12.11.24', 'fee': '200 TL'},
        {'from': 'İzmir', 'arrival': 'Antalya', 'time': '14:30','date':'12.11.24', 'fee': '200 TL'},
        {'from': 'İzmir', 'arrival': 'Antalya', 'time': '14:30','date':'12.11.24', 'fee': '200 TL'},
        {'from': 'İzmir', 'arrival': 'Antalya', 'time': '14:30','date':'12.11.24', 'fee': '200 TL'},
        {'from': 'İstanbul', 'arrival': 'Ankara', 'time': '13:00', 'date':'12.11.24','fee': '150 TL'},
        {'from': 'İzmir', 'arrival': 'Antalya', 'time': '14:30','date':'12.11.24','fee': '200 TL'},
        {'from': 'İzmir', 'arrival': 'Antalya', 'time': '14:30','date':'12.11.24','fee': '200 TL'},
        {'from': 'İzmir', 'arrival': 'Antalya', 'time': '14:30','date':'12.11.24','fee': '200 TL'},
        {'from': 'İzmir', 'arrival': 'Antalya', 'time': '14:30','date':'12.11.24','fee': '200 TL'},
    
    ]
    return render_template('book.html', tickets=tickets)

if __name__ == '__main__':
    app.run(debug=True)
