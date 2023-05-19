from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.secret_key = "Secret Key_psabenguet011@gmail.com"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Data(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	#PERSONAL INFORMATION
	status_employment = db.Column(db.String(13))
	name_last = db.Column(db.String(50))
	name_first = db.Column(db.String(50))
	name_middle = db.Column(db.String(50))
	name_suffix = db.Column(db.String(50))
	date_birth = db.Column(db.String(50))
	place_birth = db.Column(db.String(100))
	sex = db.Column(db.String(13))
	status_civil = db.Column(db.String(13))
	citizenship = db.Column(db.String(50))
	bloodtype = db.Column(db.String(13))
	place_residential = db.Column(db.String(100))
	no_mobile = db.Column(db.String(13))
	email = db.Column(db.String(50))
	no_gsissss = db.Column(db.String(11))
	no_pagibig_mp1 = db.Column(db.String(13))
	no_philhealth = db.Column(db.String(13))
	no_pagibig_mp2 = db.Column(db.String(13))
	no_employee = db.Column(db.String(7))
	no_tin = db.Column(db.String(10))
	#DEPENDENTS
	name_spouse = db.Column(db.String(50))
	no_spouse = db.Column(db.String(13))
	date_birth_spouse = db.Column(db.String(50))
	name_children1 = db.Column(db.String(50))
	no_children1 = db.Column(db.String(13))
	date_birth_children1 = db.Column(db.String(50))
	name_children2 = db.Column(db.String(50))
	date_birth_children2 = db.Column(db.String(50))
	name_children3 = db.Column(db.String(50))
	date_birth_children3 = db.Column(db.String(50))
	name_children4 = db.Column(db.String(50))
	date_birth_children4 = db.Column(db.String(50))
	#EDUCATIONAL BACKGROUND
	school_primary = db.Column(db.String(50))
	school_secondary = db.Column(db.String(50))
	school_vocational1 = db.Column(db.String(50))
	degree_vocational1 = db.Column(db.String(50))
	school_college1 = db.Column(db.String(50))
	degree_college1 = db.Column(db.String(50))
	school_graduate1 = db.Column(db.String(50))
	degree_graduate1 = db.Column(db.String(50))
	#ELIGIBILITY
	title_eligibility1 = db.Column(db.String(50))
	date_place_eligibility1 = db.Column(db.String(50))
	date_no_eligibility1 = db.Column(db.String(50))
	title_eligibility2 = db.Column(db.String(50))
	date_place_eligibility2 = db.Column(db.String(50))
	date_no_eligibility2 = db.Column(db.String(50))
	#SERVICE RECORD
	designation1 = db.Column(db.String(50))
	place_designation1 = db.Column(db.String(50))
	date_designation1 = db.Column(db.String(50))
	remarks_designation1 = db.Column(db.String(50))
	designation2 = db.Column(db.String(50))
	place_designation2 = db.Column(db.String(50))
	date_designation2 = db.Column(db.String(50))
	remarks_designation2 = db.Column(db.String(50))
	#EMPLOYEE TRAINING & DEVELOPMENT
	title_learning1 = db.Column(db.String(50))
	date_learning1 = db.Column(db.String(50))
	hours_learning1 = db.Column(db.Integer)
	type_learning1 = db.Column(db.String(50))
	conductedby_learning1 = db.Column(db.String(50))
	title_learning2 = db.Column(db.String(50))
	date_learning2 = db.Column(db.String(50))
	hours_learning2 = db.Column(db.Integer)
	type_learning2 = db.Column(db.String(50))
	conductedby_learning2 = db.Column(db.String(50))
	title_learning3 = db.Column(db.String(50))
	date_learning3 = db.Column(db.String(50))
	hours_learning3 = db.Column(db.Integer)
	type_learning3 = db.Column(db.String(50))
	conductedby_learning3 = db.Column(db.String(50))
	title_learning4 = db.Column(db.String(50))
	date_learning4 = db.Column(db.String(50))
	hours_learning4 = db.Column(db.Integer)
	type_learning4 = db.Column(db.String(50))
	conductedby_learning4 = db.Column(db.String(50))
	title_learning5 = db.Column(db.String(50))
	date_learning5 = db.Column(db.String(50))
	hours_learning5 = db.Column(db.Integer)
	type_learning5 = db.Column(db.String(50))
	conductedby_learning5 = db.Column(db.String(50))

	def __init__(self, status_employment, name_last, name_first, name_middle, name_suffix, date_birth, place_birth, sex,
	status_civil, citizenship, bloodtype, place_residential, no_mobile, email, no_gsissss, no_pagibig_mp1, no_philhealth,
	no_pagibig_mp2, no_employee, no_tin, name_spouse, no_spouse, date_birth_spouse, name_children1, no_children1,
	date_birth_children1, name_children2, date_birth_children2, name_children3, date_birth_children3, name_children4,
	date_birth_children4, school_primary, school_secondary, school_vocational1, degree_vocational1, school_college1,
	degree_college1, school_graduate1, degree_graduate1, title_eligibility1, date_place_eligibility1,
	date_no_eligibility1, title_eligibility2, date_place_eligibility2, date_no_eligibility2,
	designation1, place_designation1, date_designation1, remarks_designation1,
	designation2, place_designation2, date_designation2, remarks_designation2,
	title_learning1, date_learning1, hours_learning1, type_learning1, conductedby_learning1,
	title_learning2, date_learning2, hours_learning2, type_learning2, conductedby_learning2,
	title_learning3, date_learning3, hours_learning3, type_learning3, conductedby_learning3,
	title_learning4, date_learning4, hours_learning4, type_learning4, conductedby_learning4,
	title_learning5, date_learning5, hours_learning5, type_learning5, conductedby_learning5):
		#PERSONAL INFORMATION
		self.status_employment = status_employment
		self.name_last = name_last
		self.name_first = name_first
		self.name_middle = name_middle
		self.name_suffix = name_suffix
		self.date_birth = date_birth
		self.place_birth = place_birth
		self.sex = sex
		self.status_civil = status_civil
		self.citizenship = citizenship
		self.bloodtype = bloodtype
		self.place_residential = place_residential
		self.no_mobile = no_mobile
		self.email = email
		self.no_gsissss = no_gsissss
		self.no_pagibig_mp1 = no_pagibig_mp1
		self.no_philhealth = no_philhealth
		self.no_pagibig_mp2 = no_pagibig_mp2
		self.no_employee = no_employee
		self.no_tin = no_tin
		#DEPENDENTS
		self.name_spouse = name_spouse
		self.no_spouse = no_spouse
		self.date_birth_spouse = date_birth_spouse
		self.name_children1 = name_children1
		self.no_children1 = no_children1
		self.date_birth_children1 = date_birth_children1
		self.name_children2 = name_children2
		self.date_birth_children2 = date_birth_children2
		self.name_children3 = name_children3
		self.date_birth_children3 = date_birth_children3
		self.name_children4 = name_children4
		self.date_birth_children4 = date_birth_children4
		#EDUCATIONAL BACKGROUND
		self.school_primary = school_primary
		self.school_secondary = school_secondary
		self.school_vocational1 = school_vocational1
		self.degree_vocational1 = degree_vocational1
		self.school_college1 = school_college1
		self.degree_college1 = degree_college1
		self.school_graduate1 = school_graduate1
		self.degree_graduate1 = degree_graduate1
		#ELIGIBILITY
		self.title_eligibility1 = title_eligibility1
		self.date_place_eligibility1 = date_place_eligibility1
		self.date_no_eligibility1 = date_no_eligibility1
		self.title_eligibility2 = title_eligibility2
		self.date_place_eligibility2 = date_place_eligibility2
		self.date_no_eligibility2 = date_no_eligibility2
		#SERVICE RECORD
		self.designation1 = designation1
		self.place_designation1 = place_designation1
		self.date_designation1 = date_designation1
		self.remarks_designation1 = remarks_designation1
		self.designation2 = designation2
		self.place_designation2 = place_designation2
		self.date_designation2 = date_designation2
		self.remarks_designation2 = remarks_designation2
		#EMPLOYEE TRAINING & DEVELOPMENT
		self.title_learning1 = title_learning1
		self.date_learning1 = date_learning1
		self.hours_learning1 = hours_learning1
		self.type_learning1 = type_learning1
		self.conductedby_learning1 = conductedby_learning1
		self.title_learning2 = title_learning2
		self.date_learning2 = date_learning2
		self.hours_learning2 = hours_learning2
		self.type_learning2 = type_learning2
		self.conductedby_learning2 = conductedby_learning2
		self.title_learning3 = title_learning3
		self.date_learning3 = date_learning3
		self.hours_learning3 = hours_learning3
		self.type_learning3 = type_learning3
		self.conductedby_learning3 = conductedby_learning3
		self.title_learning4 = title_learning4
		self.date_learning4 = date_learning4
		self.hours_learning4 = hours_learning4
		self.type_learning4 = type_learning4
		self.conductedby_learning4 = conductedby_learning4
		self.title_learning5 = title_learning5
		self.date_learning5 = date_learning5
		self.hours_learning5 = hours_learning5
		self.type_learning5 = type_learning5
		self.conductedby_learning5 = conductedby_learning5

class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name_user = db.Column(db.String(50), unique = True)
	password_user = db.Column(db.String(50))

	def __init__(self, name_user, password_user):
		self.name_user = name_user
		self.password_user = password_user

#AFTER CREATING MODEL CLASS, IN YOUR PROJECT RUN IN TERMINAL TO CREATE DATABASE:
#python
#from app import db
#db.create_all()


@app.route('/', methods = ['POST', 'GET'])
@app.route('/login', methods = ['POST', 'GET'])
def login():
	if request.method == 'POST': 
		username = request.form['username']
		password = request.form['password']

		if bool(User.query.filter_by(name_user=username, password_user=password).first()) == False:

			flash("User does not exist.")

			return redirect(url_for('login'))
		else: #if user exists
			flash("Log-in authenticated.")

			session['logged-in'] = True
			session['username'] = username

			return redirect(url_for('index'))

	return render_template('login.html')

@app.route('/home')
@app.route('/index')
def index():
	if 'username' in session:
		data_table = Data.query.all()
		return render_template('index.html', personnel = data_table)
	return render_template('login.html')

@app.route('/insert', methods = ['POST'])
def insert():
	if request.method == 'POST': 
		#USE name="" from HTML
		#PERSONAL INFORMATION
		status_employment = request.form['status_employment']
		name_last = request.form['name_last']
		name_first = request.form['name_first']
		name_middle = request.form['name_middle']
		name_suffix = request.form['name_suffix']
		date_birth = request.form['date_birth']
		place_birth = request.form['place_birth']
		sex = request.form['sex']
		status_civil = request.form['status_civil']
		citizenship = request.form['citizenship']
		bloodtype = request.form['bloodtype']
		place_residential = request.form['place_residential']
		no_mobile = request.form['no_mobile']
		email = request.form['email']
		no_gsissss = request.form['no_gsissss']
		no_pagibig_mp1 = request.form['no_pagibig_mp1']
		no_philhealth = request.form['no_philhealth']
		no_pagibig_mp2 = request.form['no_pagibig_mp2']
		no_employee = request.form['no_employee']
		no_tin = request.form['no_tin']
		#DEPENDENTS
		name_spouse = request.form['name_spouse']
		no_spouse = request.form['no_spouse']
		date_birth_spouse = request.form['date_birth_spouse']
		name_children1 = request.form['name_children1']
		no_children1 = request.form['no_children1']
		date_birth_children1 = request.form['date_birth_children1']
		name_children2 = request.form['name_children2']
		date_birth_children2 = request.form['date_birth_children2']
		name_children3 = request.form['name_children3']
		date_birth_children3 = request.form['date_birth_children3']
		name_children4 = request.form['name_children4']
		date_birth_children4 = request.form['date_birth_children4']
		#EDUCATIONAL BACKGROUND
		school_primary = request.form['school_primary']
		school_secondary = request.form['school_secondary']
		school_vocational1 = request.form['school_vocational1']
		degree_vocational1 = request.form['degree_vocational1']
		school_college1 = request.form['school_college1']
		degree_college1 = request.form['degree_college1']
		school_graduate1 = request.form['school_graduate1']
		degree_graduate1 = request.form['degree_graduate1']
		#ELIGIBILITY
		title_eligibility1 = request.form['title_eligibility1']
		date_place_eligibility1 = request.form['date_place_eligibility1']
		date_no_eligibility1 = request.form['date_no_eligibility1']
		title_eligibility2 = request.form['title_eligibility2']
		date_place_eligibility2 = request.form['date_place_eligibility2']
		date_no_eligibility2 = request.form['date_no_eligibility2']
		#SERVICE RECORD
		designation1 = request.form['designation1']
		place_designation1 = request.form['place_designation1']
		date_designation1 = request.form['date_designation1']
		remarks_designation1 = request.form['remarks_designation1']
		designation2 = request.form['designation2']
		place_designation2 = request.form['place_designation2']
		date_designation2 = request.form['date_designation2']
		remarks_designation2 = request.form['remarks_designation2']
		#EMPLOYEE TRAINING & DEVELOPMENT
		title_learning1 = request.form['title_learning1']
		date_learning1 = request.form['date_learning1']
		hours_learning1 = request.form['hours_learning1']
		type_learning1 = request.form['type_learning1']
		conductedby_learning1 = request.form['conductedby_learning1']
		title_learning2 = request.form['title_learning2']
		date_learning2 = request.form['date_learning2']
		hours_learning2 = request.form['hours_learning2']
		type_learning2 = request.form['type_learning2']
		conductedby_learning2 = request.form['conductedby_learning2']
		title_learning3 = request.form['title_learning3']
		date_learning3 = request.form['date_learning3']
		hours_learning3 = request.form['hours_learning3']
		type_learning3 = request.form['type_learning3']
		conductedby_learning3 = request.form['conductedby_learning3']
		title_learning4 = request.form['title_learning4']
		date_learning4 = request.form['date_learning4']
		hours_learning4 = request.form['hours_learning4']
		type_learning4 = request.form['type_learning4']
		conductedby_learning4 = request.form['conductedby_learning4']
		title_learning5 = request.form['date_learning5']
		date_learning5 = request.form['date_learning5']
		hours_learning5 = request.form['hours_learning5']
		type_learning5 = request.form['type_learning5']
		conductedby_learning5 = request.form['conductedby_learning5']

		data_entries = Data(status_employment, name_last, name_first, name_middle, name_suffix, date_birth, place_birth, sex,
		status_civil, citizenship, bloodtype, place_residential, no_mobile, email, no_gsissss, no_pagibig_mp1, no_philhealth,
		no_pagibig_mp2, no_employee, no_tin, name_spouse, no_spouse, date_birth_spouse, name_children1, no_children1,
		date_birth_children1, name_children2, date_birth_children2, name_children3, date_birth_children3, name_children4,
		date_birth_children4, school_primary, school_secondary, school_vocational1, degree_vocational1, school_college1,
		degree_college1, school_graduate1, degree_graduate1, title_eligibility1, date_place_eligibility1,
		date_no_eligibility1, title_eligibility2, date_place_eligibility2, date_no_eligibility2,
		designation1, place_designation1, date_designation1, remarks_designation1,
		designation2, place_designation2, date_designation2, remarks_designation2,
		title_learning1, date_learning1, hours_learning1, type_learning1, conductedby_learning1,
		title_learning2, date_learning2, hours_learning2, type_learning2, conductedby_learning2,
		title_learning3, date_learning3, hours_learning3, type_learning3, conductedby_learning3,
		title_learning4, date_learning4, hours_learning4, type_learning4, conductedby_learning4,
		title_learning5, date_learning5, hours_learning5, type_learning5, conductedby_learning5)
		db.session.add(data_entries)
		db.session.commit()

		flash("Personnel record added successfully.")

		return redirect(url_for('index')) #def index

@app.route('/update', methods = ['GET','POST'])
def update():
	if request.method == 'POST': 
		data_entries = Data.query.get(request.form.get('id'))

		#USE name="" from HTML
		#PERSONAL INFORMATION
		data_entries.status_employment = request.form['status_employment']
		data_entries.name_last = request.form['name_last']
		data_entries.name_first = request.form['name_first']
		data_entries.name_middle = request.form['name_middle']
		data_entries.name_suffix = request.form['name_suffix']
		data_entries.date_birth = request.form['date_birth']
		data_entries.place_birth = request.form['place_birth']
		data_entries.sex = request.form['sex']
		data_entries.status_civil = request.form['status_civil']
		data_entries.citizenship = request.form['citizenship']
		data_entries.bloodtype = request.form['bloodtype']
		data_entries.place_residential = request.form['place_residential']
		data_entries.no_mobile = request.form['no_mobile']
		data_entries.email = request.form['email']
		data_entries.no_gsissss = request.form['no_gsissss']
		data_entries.no_pagibig_mp1 = request.form['no_pagibig_mp1']
		data_entries.no_philhealth = request.form['no_philhealth']
		data_entries.no_pagibig_mp2 = request.form['no_pagibig_mp2']
		data_entries.no_employee = request.form['no_employee']
		data_entries.no_tin = request.form['no_tin']
		#DEPENDENTS
		data_entries.name_spouse = request.form['name_spouse']
		data_entries.no_spouse = request.form['no_spouse']
		data_entries.date_birth_spouse = request.form['date_birth_spouse']
		data_entries.name_children1 = request.form['name_children1']
		data_entries.no_children1 = request.form['no_children1']
		data_entries.date_birth_children1 = request.form['date_birth_children1']
		data_entries.name_children2 = request.form['name_children2']
		data_entries.date_birth_children2 = request.form['date_birth_children2']
		data_entries.name_children3 = request.form['name_children3']
		data_entries.date_birth_children3 = request.form['date_birth_children3']
		data_entries.name_children4 = request.form['name_children4']
		data_entries.date_birth_children4 = request.form['date_birth_children4']
		#EDUCATIONAL BACKGROUND
		data_entries.school_primary = request.form['school_primary']
		data_entries.school_secondary = request.form['school_secondary']
		data_entries.school_vocational1 = request.form['school_vocational1']
		data_entries.degree_vocational1 = request.form['degree_vocational1']
		data_entries.school_college1 = request.form['school_college1']
		data_entries.degree_college1 = request.form['degree_college1']
		data_entries.school_graduate1 = request.form['school_graduate1']
		data_entries.degree_graduate1 = request.form['degree_graduate1']
		#ELIGIBILITY
		data_entries.title_eligibility1 = request.form['title_eligibility1']
		data_entries.date_place_eligibility1 = request.form['date_place_eligibility1']
		data_entries.date_no_eligibility1 = request.form['date_no_eligibility1']
		data_entries.title_eligibility2 = request.form['title_eligibility2']
		data_entries.date_place_eligibility2 = request.form['date_place_eligibility2']
		data_entries.date_no_eligibility2 = request.form['date_no_eligibility2']
		#SERVICE RECORD
		data_entries.designation1 = request.form['designation1']
		data_entries.place_designation1 = request.form['place_designation1']
		data_entries.date_designation1 = request.form['date_designation1']
		data_entries.remarks_designation1 = request.form['remarks_designation1']
		data_entries.designation2 = request.form['designation2']
		data_entries.place_designation2 = request.form['place_designation2']
		data_entries.date_designation2 = request.form['date_designation2']
		data_entries.remarks_designation2 = request.form['remarks_designation2']
		#EMPLOYEE TRAINING & DEVELOPMENT
		data_entries.title_learning1 = request.form['title_learning1']
		data_entries.date_learning1 = request.form['date_learning1']
		data_entries.hours_learning1 = request.form['hours_learning1']
		data_entries.type_learning1 = request.form['type_learning1']
		data_entries.conductedby_learning1 = request.form['conductedby_learning1']
		data_entries.title_learning2 = request.form['title_learning2']
		data_entries.date_learning2 = request.form['date_learning2']
		data_entries.hours_learning2 = request.form['hours_learning2']
		data_entries.type_learning2 = request.form['type_learning2']
		data_entries.conductedby_learning2 = request.form['conductedby_learning2']
		data_entries.title_learning3 = request.form['title_learning3']
		data_entries.date_learning3 = request.form['date_learning3']
		data_entries.hours_learning3 = request.form['hours_learning3']
		data_entries.type_learning3 = request.form['type_learning3']
		data_entries.conductedby_learning3 = request.form['conductedby_learning3']
		data_entries.title_learning4 = request.form['title_learning4']
		data_entries.date_learning4 = request.form['date_learning4']
		data_entries.hours_learning4 = request.form['hours_learning4']
		data_entries.type_learning4 = request.form['type_learning4']
		data_entries.conductedby_learning4 = request.form['conductedby_learning4']
		data_entries.title_learning5 = request.form['date_learning5']
		data_entries.date_learning5 = request.form['date_learning5']
		data_entries.hours_learning5 = request.form['hours_learning5']
		data_entries.type_learning5 = request.form['type_learning5']
		data_entries.conductedby_learning5 = request.form['conductedby_learning5']

		db.session.commit()

		flash("Personnel record updated successfully.")

		return redirect(url_for('index')) #def index

@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
	data_entries = Data.query.get(id)
	db.session.delete(data_entries)
	db.session.commit()
    
	flash("Personnel record removed successfully.")

	return redirect(url_for('index')) #def index

@app.route('/logout')
def logout():
	session.pop('logged-in', None)
	session.pop('username', None)

	return redirect(url_for('login')) #def login

if __name__ == "__main__":
	app.run(debug=True)
