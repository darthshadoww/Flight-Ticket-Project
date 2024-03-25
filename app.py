# app.py
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Import database models
from models import Administrator, User, Flight, Booking
from forms import RegistrationForm, LoginForm

# Routes for CRUD operations
# ... other imports

@app.route('/')
def index():
    city_list = City.query.all()
    return render_template('index.html', city_list=city_list)

@app.route('/search_flights', methods=['POST'])
def search_flights():
    # Get search parameters from the form...
    # Query the database for flights...
    # (Example with dummy data for now)
    flights = [
        # ... add your flight data ...
    ]
    return render_template('book.html', tickets=flights)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Create a new user object...
        # Hash the password...
        # Add user to the database and commit...
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Find the user by username or email...
        # Check the password hash...
        # Create a user session...
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))


@app.route('/book/<int:flight_id>')
def book_flight(flight_id):
    flight = Flight.query.get_or_404(flight_id)  # Get selected flight by ID
    return render_template('booking_form.html', flight=flight)



if __name__ == '__app__':
    app.run(debug=True)
