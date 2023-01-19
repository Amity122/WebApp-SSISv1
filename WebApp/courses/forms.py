from flask_wtf import FlaskForm
from wtforms.validators import Length, DataRequired
from wtforms import StringField, SubmitField, SelectField

class add_courses_form(FlaskForm):
    course_code = StringField("Course Code:", validators=[DataRequired()])
    course_name = StringField("Course Name:", validators=[
                              DataRequired(), Length(min=7, max=64)])
    respective_college = SelectField('On which college will this course belong to?', choices=[])
    submit = SubmitField("Add Course")


class delete_courses_form(FlaskForm):
    course_code_del = StringField("Course Code: ", validators=[DataRequired()])
    submit = SubmitField("Delete Course")


class update_courses_form(FlaskForm):
    new_course_name = StringField(
        "Update Course Name:", validators=[DataRequired(), Length(min=7, max=64)])
    new_course_code = StringField(
        "Update Course Code:", validators=[DataRequired()])
    new_resp_college = SelectField("On which college will this course belong to?", choices=[])
    submit = SubmitField("Update Course")