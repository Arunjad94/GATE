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

@app.route('/view_visitors')
def view_visitors():
    visitors = Visitor.query.all()
    return render_template('view_visitors.html', visitors=visitors)

if __name__ == '__main__':
    app.run(debug=True)
