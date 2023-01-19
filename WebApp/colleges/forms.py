from flask_wtf import FlaskForm
from wtforms.validators import Length, DataRequired
from wtforms import StringField, SubmitField

class add_college_form(FlaskForm):
    college_name = StringField("College Name: ", validators=[
                               DataRequired(), Length(min=7, max=64)])
    college_code = StringField("College Code: ", validators=[DataRequired()])
    submit = SubmitField("Add College")

class delete_college_form(FlaskForm):
    college_code_del = StringField(
        "College Code to delete: ", validators=[DataRequired()])
    submit = SubmitField("Delete College")

class update_college_form(FlaskForm):
    new_college_name = StringField(
        "Update College Name:", validators=[DataRequired(), Length(min=7, max=64)])
    new_college_code = StringField(
        "Update College Code:", validators=[DataRequired()])
    submit = SubmitField("Update College")