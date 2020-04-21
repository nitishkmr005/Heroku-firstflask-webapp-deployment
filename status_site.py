import os
from forms import  AddForm , DelForm, UpdForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)
# Key for Forms
app.config['SECRET_KEY'] = 'mysecretkey'

############################################

        # SQL DATABASE AND MODELS

##########################################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

class Emp(db.Model):

    __tablename__ = 'emps'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    team = db.Column(db.Text)
    skills = db.Column(db.Text)
    learning_status = db.Column(db.Text)

    def __init__(self,name,team,skills,learning_status):
        self.name = name
        self.team = team
        self.skills = skills
        self.learning_status = learning_status

    def __repr__(self):
        return f"Id : {self.id} | Employee : {self.name} |  Team : {self.team} | Skills : {self.skills} | Status : {self.learning_status}."

############################################

        # VIEWS WITH FORMS

##########################################
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_emp():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        team = form.team.data
        skills = form.skills.data
        learning_status = form.learning_status.data

        # Add new Emp to database
        new_emp = Emp(name,team,skills,learning_status)
        db.session.add(new_emp)
        db.session.commit()

        return redirect(url_for('list_emp'))

    return render_template('add.html',form=form)

@app.route('/update', methods=['GET', 'POST'])
def upd_emp():

    form = UpdForm()

    if form.validate_on_submit():
        id = form.id.data
        emp_u = Emp.query.get(id)
        emp_u.learning_status = form.learning_status.data
        db.session.add(emp_u)
        db.session.commit()

        return redirect(url_for('list_emp'))
    return render_template('update.html',form=form)

@app.route('/list')
def list_emp():
    # Grab a list of employess from database.
    employees = Emp.query.all()
    return render_template('list.html', employees=employees)

@app.route('/delete', methods=['GET', 'POST'])
def del_emp():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        emp_d = Emp.query.get(id)
        db.session.delete(emp_d)
        db.session.commit()

        return redirect(url_for('list_emp'))
    return render_template('delete.html',form=form)

if __name__ == '__main__':
    app.run()
