from flask import Flask
from config import DB_USERNAME, DB_PASSWORD, DB_NAME, DB_HOST, SECRET_KEY
from WebApp.sql_init import create_db
from flask_mysql_connector import MySQL

mysql = MySQL()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['MYSQL_HOST'] = DB_HOST
    app.config['MYSQL_USER'] = DB_USERNAME
    app.config['MYSQL_PASSWORD'] = DB_PASSWORD
    app.config['MYSQL_DATABASE'] = DB_NAME
    create_db()
    mysql.init_app(app)

    from .auth import auth
    from .colleges import colleges
    from .courses import courses
    from .students import students


    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(colleges, url_prefix='/')
    app.register_blueprint(courses, url_prefix='/')
    app.register_blueprint(students, url_prefix='/')


    return app


def get_error_items(form):
    errors = {}
    for fieldName, errorMessages in form.errors.items():
        errors[fieldName] = errorMessages
    return errors


def get_form_fields(form):
    fields = []
    for keys in form.data.keys():
        fields.append(keys)
    return fields
