# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Visitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    check_in_time = db.Column(db.DateTime, nullable=False)


# app.py
from flask import Flask, render_template, request, redirect, url_for
from models import db, Visitor
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///visitors.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_visitor', methods=['POST'])
def add_visitor():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    check_in_time = datetime.now()

    new_visitor = Visitor(name=name, email=email, phone=phone, check_in_time=check_in_time)
    db.session.add(new_visitor)
    db.session.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

