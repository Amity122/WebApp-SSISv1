from . import courses
from flask import Blueprint, render_template, request, flash, redirect, url_for, Response
from WebApp.models import Courses, Colleges
from WebApp import mysql
from .forms import add_courses_form, delete_courses_form, update_courses_form       

@courses.route('/add-courses', methods=['GET','POST'])
def add_courses():
    form = add_courses_form()
    add_course = Courses.query_filter(all=True, order_by='resp_college', order='DESC')
    form.respective_college.choices = [(college.college_code, college.college_name) for college in Colleges.query_filter(all=True)]
    if form.validate_on_submit():
        try:
            some_variable = Courses(course_name=form.course_name.data,
                                    course_code=form.course_code.data, resp_college=form.respective_college.data)
            some_variable.add()
            mysql.connection.commit()
            flash('Course added successfully!')
            return redirect(url_for('courses.add_courses'))
        except:
            flash("Error! Course already exists!")
            return render_template("courses/add-courses.html", add_course=add_course, form=form)
    return render_template("courses/add-courses.html", form=form, add_course=add_course)

@courses.route('/update-courses', methods=['GET', 'POST'])
def update_course():
    form = update_courses_form()
    form.new_resp_college.choices = [(college.college_code, college.college_name) for college in Colleges.query_filter(all=True)]
    updated_course = Courses.query_filter(all=True, order_by='resp_college', order='DESC')
    return render_template('courses/update-courses.html', updated_course=updated_course, form=form)


@courses.route("/home/update-course/<course_code>", methods=['GET', 'POST'])
def update_course_info(course_code):
    form = update_courses_form(request.form)
    form.new_resp_college.choices = [(college.college_code, college.college_name) for college in Colleges.query_filter(all=True)]
    if request.method == 'POST':
        try:
            new_course_name = form.new_course_name.data
            new_course_code = form.new_course_code.data
            new_resp_college = form.new_resp_college.data
            Courses.update_course(course_code, new_course_code, new_course_name, new_resp_college)
            mysql.connection.commit()
            flash('Course Edited Successfully!')
            return redirect(url_for('courses.update_course'))
        except:
            flash('Course Already Exists!')
            return redirect(url_for('courses.update_course'))
    return render_template('courses/update-courses.html', form=form)

@courses.route('/delete-courses', methods=['GET','POST'])
def delete_courses():
    course_code_del = None
    form = delete_courses_form()
    if form.validate_on_submit():
        some_variable = Courses.query_get(
            course_code=form.course_code_del.data)
        if some_variable:
            Courses.delete(some_variable.course_code)
            mysql.connection.commit()
            form.course_code_del.data = ''
            flash("Course Removed Successfully!")
        else:
            flash("Course does not exist!")
    del_course = Courses.query_filter(all=True, order_by='resp_college', order='DESC')
    return render_template('courses/delete-courses.html', course_code_del=course_code_del, del_course=del_course, form=form)
