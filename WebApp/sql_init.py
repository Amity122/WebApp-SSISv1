from config import DB_HOST, DB_PASSWORD, DB_USERNAME, DB_NAME
import mysql.connector

db = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USERNAME,
    password=DB_PASSWORD
)

cursor = db.cursor()


def create_db():
    cursor.execute(f"""
    CREATE DATABASE IF NOT EXISTS {DB_NAME};
    USE {DB_NAME};

    CREATE TABLE IF NOT EXISTS colleges (
        college_code VARCHAR(25) NOT NULL,
        college_name VARCHAR(150) NULL DEFAULT NULL,
        PRIMARY KEY (college_code),
        UNIQUE(college_name)
    );

    CREATE TABLE IF NOT EXISTS courses (
        course_name VARCHAR(150) NOT NULL,
        course_code VARCHAR(25),
        resp_college VARCHAR(25),
        PRIMARY KEY (course_code) ,
        CONSTRAINT `courses_ibfk_1` FOREIGN KEY (resp_college) REFERENCES colleges(college_code) ON UPDATE CASCADE ON DELETE SET NULL
    );

    CREATE TABLE IF NOT EXISTS students (
        id VARCHAR(20) NOT NULL,
        first_name VARCHAR(150) NOT NULL,
        course VARCHAR(25),
        college VARCHAR(25),
        last_name VARCHAR(150) NOT NULL,
        gender VARCHAR(15) NOT NULL,
        year_lvl VARCHAR(80) NOT NULL,
        PRIMARY KEY (id) ,
        CONSTRAINT `students_ibfk_1` FOREIGN KEY(course) REFERENCES courses(course_code) ON UPDATE CASCADE ON DELETE SET NULL,
        CONSTRAINT `students_ibfk_2` FOREIGN KEY(college) REFERENCES colleges(college_code) ON UPDATE CASCADE ON DELETE SET NULL

    );""")
