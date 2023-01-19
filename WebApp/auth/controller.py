from . import auth
from flask import render_template
from WebApp.models import Colleges


@auth.route('/')
def home_page():
    college_table = Colleges.query_filter(all=True, order_by='college_code', order='DESC')
    return render_template('home/home.html', college_table=college_table)
