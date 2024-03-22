from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Set the URI for the SQLite database file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# Suppress deprecation warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Flask-SQLAlchemy
db = SQLAlchemy(app)


# Define database models
class Administrator(db.Model):
    __tablename__ = 'administrator'
    AdminID = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(50), unique=True)
    Email = db.Column(db.String(100), unique=True)
    Password = db.Column(db.String(100))
    FirstName = db.Column(db.String(50))
    LastName = db.Column(db.String(50))
    RegistrationDate = db.Column(db.Date, server_default=db.func.current_date())
    LastLoginDate = db.Column(db.Date)


class User(db.Model):
    __tablename__ = 'user'
    UserID = db.Column(db.Integer, primary_key=True)
    AdminID = db.Column(db.Integer, db.ForeignKey('administrator.AdminID'))
    Username = db.Column(db.String(50), unique=True)
    Email = db.Column(db.String(100), unique=True)
    Password = db.Column(db.String(100))
    FirstName = db.Column(db.String(50))
    LastName = db.Column(db.String(50))
    RegistrationDate = db.Column(db.Date, server_default=db.func.current_date())
    LastLoginDate = db.Column(db.Date)
    admin = db.relationship('Administrator', backref='users')


class Flight(db.Model):
    __tablename__ = 'flight'
    FlightID = db.Column(db.Integer, primary_key=True)
    Airline = db.Column(db.String(100))
    DepartureAirport = db.Column(db.String(100))
    ArrivalAirport = db.Column(db.String(100))
    DepartureDateTime = db.Column(db.DateTime)
    ArrivalDateTime = db.Column(db.DateTime)
    Price = db.Column(db.Numeric(10, 2))
    AvailableSeats = db.Column(db.Integer)


class Booking(db.Model):
    __tablename__ = 'booking'
    BookingID = db.Column(db.Integer, primary_key=True)
    UserID = db.Column(db.Integer, db.ForeignKey('user.UserID'))
    FlightID = db.Column(db.Integer, db.ForeignKey('flight.FlightID'))
    BookingDate = db.Column(db.Date, server_default=db.func.current_date())
    Status = db.Column(db.String(20), default='Pending')
    user = db.relationship('User', backref='bookings')
    flight = db.relationship('Flight', backref='bookings')


# Define routes
@app.route('/')
def index():
    return render_template('index.html')


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
