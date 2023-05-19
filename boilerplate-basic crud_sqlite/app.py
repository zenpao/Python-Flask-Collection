from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.secret_key = "Secret Key_qroize@gmail.com"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Data(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	#CONTACT INFORMATION
	name_last = db.Column(db.String(50))
	name_first = db.Column(db.String(50))
	name_middle = db.Column(db.String(50))
	name_suffix = db.Column(db.String(50))
	date_birth = db.Column(db.String(50))
	place_birth = db.Column(db.String(100))
	place_residential = db.Column(db.String(100))
	no_mobile = db.Column(db.String(13))
	email = db.Column(db.String(50))

	def __init__(self, name_last, name_first, name_middle, name_suffix, date_birth, place_birth, place_residential, no_mobile, email):
		#CONTACT INFORMATION
		self.name_last = name_last
		self.name_first = name_first
		self.name_middle = name_middle
		self.name_suffix = name_suffix
		self.date_birth = date_birth
		self.place_birth = place_birth
		self.place_residential = place_residential
		self.no_mobile = no_mobile
		self.email = email

#AFTER CREATING MODEL CLASS, IN YOUR PROJECT RUN IN TERMINAL TO CREATE DATABASE:
#python
#from app import db
#db.create_all()

@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
	data_table = Data.query.all()
	return render_template('index.html', read = data_table)

@app.route('/insert', methods = ['POST'])
def insert():
	if request.method == 'POST': 
		#USE name="" from HTML
		#CONTACT INFORMATION
		name_last = request.form['name_last']
		name_first = request.form['name_first']
		name_middle = request.form['name_middle']
		name_suffix = request.form['name_suffix']
		date_birth = request.form['date_birth']
		place_birth = request.form['place_birth']
		place_residential = request.form['place_residential']
		no_mobile = request.form['no_mobile']
		email = request.form['email']

		data_entries = Data(name_last, name_first, name_middle, name_suffix, date_birth, place_birth, place_residential, no_mobile, email)
		db.session.add(data_entries)
		db.session.commit()

		flash("Contact record added successfully.")

		return redirect(url_for('index')) #def index

@app.route('/update', methods = ['GET','POST'])
def update():
	if request.method == 'POST': 
		data_entries = Data.query.get(request.form.get('id'))

		#USE name="" from HTML
		#CONTACT INFORMATION
		data_entries.name_last = request.form['name_last']
		data_entries.name_first = request.form['name_first']
		data_entries.name_middle = request.form['name_middle']
		data_entries.name_suffix = request.form['name_suffix']
		data_entries.date_birth = request.form['date_birth']
		data_entries.place_birth = request.form['place_birth']
		data_entries.place_residential = request.form['place_residential']
		data_entries.no_mobile = request.form['no_mobile']
		data_entries.email = request.form['email']

		db.session.commit()

		flash("Contact record updated successfully.")

		return redirect(url_for('index')) #def index

@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
	data_entries = Data.query.get(id)
	db.session.delete(data_entries)
	db.session.commit()
    
	flash("Contact record removed successfully.")

	return redirect(url_for('index')) #def index

if __name__ == "__main__":
	app.run(debug=True)
