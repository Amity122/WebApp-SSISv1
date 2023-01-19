from flask_wtf import FlaskForm
from wtforms.validators import Length, DataRequired, Regexp
from wtforms import StringField, SubmitField, SelectField

class add_student_form(FlaskForm):
    id_number = StringField('First Name: ', validators=[
                           DataRequired(), Regexp('[0-9]+-\d\d\d\d'), Length(min=9, max=9)])
    first_name = StringField("First Name: ", validators=[
                               DataRequired(), Length(min=7, max=64)])
    last_name = StringField("Last Name: ", validators=[DataRequired()])
    course = SelectField('Course: ', choices=[])
    college = SelectField('College: ', choices=[])
    year_level = SelectField("Year Level: ", coerce=str, choices=[
        ("1st Year", "1st Year"), ("2nd Year", "2nd Year"), ("3rd Year", "3rd Year"), ("4th Year", "4th Year")], validators=[DataRequired()])
    gender = SelectField('Gender:', choices=[
                        ('M', 'M'), ('F', 'F'), ('Other', 'Other')], validators=[DataRequired()])
    submit = SubmitField("Add Student")

class delete_student_form(FlaskForm):
    student_to_del = StringField("ID Number: ", validators=[DataRequired(), Regexp('[0-9]+-\d\d\d\d'), Length(min=9, max=9)])
    submit = SubmitField("Delete Student")

class update_student_form(FlaskForm):
    new_id_number = StringField('First Name: ', validators=[
                           DataRequired(), Regexp('[0-9]+-\d\d\d\d'), Length(min=9, max=9)])
    new_first_name = StringField("First Name: ", validators=[
                               DataRequired(), Length(min=7, max=64)])
    new_last_name = StringField("Last Name: ", validators=[DataRequired()])
    new_course = SelectField('Course: ', choices=[])
    new_college = SelectField('College: ', choices=[])
    new_year_level = SelectField("Year Level: ", coerce=str, choices=[
        ("1st Year", "1st Year"), ("2nd Year", "2nd Year"), ("3rd Year", "3rd Year"), ("4th Year", "4th Year")], validators=[DataRequired()])
    new_gender = SelectField('Gender:', choices=[
                        ('M', 'M'), ('F', 'F'), ('Other', 'Other')], validators=[DataRequired()])
    submit = SubmitField("Update Student")
