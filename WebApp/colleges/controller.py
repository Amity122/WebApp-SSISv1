from . import colleges
from .forms import add_college_form, delete_college_form, update_college_form
from flask import render_template, request, flash, redirect, url_for
from WebApp.models import Colleges
from WebApp import mysql

@colleges.route('/add-colleges', methods=['GET', 'POST'])
def add_college():
    form = add_college_form()
    add_college = Colleges.query_filter(all=True, order_by='college_code', order='DESC')
    if form.validate_on_submit():
        some_variable = Colleges.query_filter(college_code=form.college_code.data, order_by='college_code', order='DESC')
        if some_variable:
            flash("Error! College code or name already exists!")
            return redirect(url_for('colleges.add_college'))
        else:
            some_variable = Colleges(college_name=form.college_name.data, college_code=form.college_code.data)
            some_variable.add()
            mysql.connection.commit()
            flash("College added successfully!")
            return redirect(url_for('colleges.add_college'))
    return render_template('colleges/add-colleges.html', form=form, add_college=add_college)

@colleges.route('/update-colleges', methods=['GET', 'POST'])
def update_college():
    form = update_college_form()
    updated_college = Colleges.query_filter(all=True, order_by='college_code', order='DESC')
    return render_template('colleges/update-colleges.html', updated_college=updated_college, form=form)

@colleges.route("/home/update-college/<college_code>", methods=['GET', 'POST'])
def update_college_info(college_code):
    form = update_college_form(request.form)
    if request.method == 'POST':
        try:
            new_college_name = request.form['new_college_name'].replace(
                '"', "''")
            new_college_code = request.form['new_college_code'].replace('"',"''")
            Colleges.update_college(college_code, new_college_code, new_college_name)
            mysql.connection.commit()
            flash('College Edited Successfully!')
            return redirect(url_for('colleges.update_college'))
        except:
            flash('College Already Exists!')
            return redirect(url_for('colleges.update_college'))
    return render_template('colleges/update-colleges.html', form=form)

    

@colleges.route('/delete-colleges', methods=['GET', 'POST'])
def delete_colleges():
    college_code_del = None
    form = delete_college_form()
    if form.validate_on_submit():
        some_variable = Colleges.query_get(
            college_code=form.college_code_del.data)
        if some_variable:
            Colleges.delete(some_variable.college_code)
            mysql.connection.commit()
            form.college_code_del.data = ''
            flash("College Removed Successfully!")
        else:
            flash("College does not exist!")
    del_college = Colleges.query_filter(all=True, order_by='college_code', order='DESC')
    return render_template('colleges/delete-colleges.html', college_code_del=college_code_del, del_college=del_college, form=form)
