# app.py
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Import database models
from models import Administrator, User, Flight, Booking

# Routes for CRUD operations
@app.route('/')
def index():
    return render_template('index.html')

# Other routes...

if __name__ == '__main__':
    app.run(debug=True)
