from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):

    name = StringField('Name of the Employee')
    team = StringField('Team Name------------')
    skills = StringField('Skills Learning---------')
    learning_status = StringField('Learning Status--------')
    submit = SubmitField('Add Employee')

class DelForm(FlaskForm):

    id = IntegerField('Id Number of Employee to Remove:')
    submit = SubmitField('Remove Employee')

class UpdForm(FlaskForm):

    id = IntegerField('Id Number of Employee to Update')
    learning_status = StringField('Updated learning status------------')
    submit = SubmitField('Update Skill')
