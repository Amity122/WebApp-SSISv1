from WebApp import mysql


# ZIPS CURSOR.FETCHALL() SO WE CAN INDEX IT LIKE A DICTIONARY
def result_zip(cursor):
    columns = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    result = []
    for row in rows:
        row = dict(zip(columns, row))
        result.append(row)
    if result:
        return result
    return []

# FOR ALL TRANSACTIONS, COMMIT MUST NOT BE CALLED IN HERE TO ALLOW THE USE OF ROLLBACK
# IN THE BACKEND DURING ERRORS


class Colleges():
    def __init__(self, college_code=None,
                 college_name=None):
        self.college_code = college_code
        self.college_name = college_name

    @classmethod
    def convert_to_object(cls, rows):
        if not rows:
            return []
        object_results = []
        for row in rows:
            new_obj = Colleges(
                college_code=row['college_code'],
                college_name=row['college_name']
            )
            object_results.append(new_obj)
        return object_results

    def add(self):  # must first create a user object then use add
        cursor = mysql.connection.cursor()
        sql = f"INSERT INTO colleges(college_code, college_name) VALUES('{self.college_code}', '{self.college_name}')"
        cursor.execute(sql)

    @classmethod
    def query_get(cls, college_code):  # takes a tag, returns a user object
        cursor = mysql.connection.cursor()
        sql = f"SELECT * FROM colleges where college_code = '{college_code}'"
        cursor.execute(sql)
        result = result_zip(cursor)
        if result:
            result = Colleges.convert_to_object(result)
            return result[0]
        return []

    # query with filter, use True exact match for exact match duh
    # RETURNS A LIST OF ROWS SO IT NEEDS TO BE INDEXED
    def query_filter(all=False, college_code=None, college_name=None, order_by='college_code', order='DESC'):
        cursor = mysql.connection.cursor()
        sql = ''
        if college_code:
            sql = f"SELECT * FROM colleges where college_code LIKE '%{college_code}%'"
        if college_name:
            sql = f"SELECT * FROM colleges where college_name LIKE '%{college_name}%'"
        order = f" ORDER BY {order_by} {order};"
        if all:
            sql = f"SELECT * FROM colleges"
        sql = sql+order
        cursor.execute(sql)
        result = result_zip(cursor)
        result = Colleges.convert_to_object(result)
        if college_name:
            return result[0]
        return result

    # to update user, just call Users.update_user(<params here>)
    @classmethod
    def update_college(cls, target_college, new_college_code=None, new_college_name=None):
        cursor = mysql.connection.cursor()
        if new_college_code:
            sql = f"UPDATE colleges SET college_code = '{new_college_code}' WHERE college_code ='{target_college}'"
            cursor.execute(sql)
        if new_college_name:
            sql = f"UPDATE colleges SET college_name = '{new_college_name}' WHERE college_code ='{target_college}'"
            cursor.execute(sql)


    # pass only the target_tag
    @classmethod
    def delete(cls, target_college):
        cursor = mysql.connection.cursor()
        sql = f"DELETE FROM colleges WHERE college_code = '{target_college}';"
        cursor.execute(sql)



class Courses():
    def __init__(self, course_code=None,
                 course_name=None, resp_college=None):
        self.course_code = course_code
        self.course_name = course_name
        self.resp_college = resp_college

    @classmethod
    def convert_to_object(cls, rows):
        if not rows:
            return []
        object_results = []
        for row in rows:
            new_obj = Courses(
                course_code=row['course_code'],
                course_name=row['course_name'],
                resp_college=row['resp_college']
            )
            object_results.append(new_obj)
        return object_results

    def add(self): 
        cursor = mysql.connection.cursor()
        sql = f"INSERT INTO courses(course_code, course_name, resp_college) VALUES('{self.course_code}', '{self.course_name}', '{self.resp_college}')"
        cursor.execute(sql)

    @classmethod
    def query_get(cls, course_code):
        cursor = mysql.connection.cursor()
        sql = f"SELECT * FROM courses where course_code = '{course_code}'"
        cursor.execute(sql)
        result = result_zip(cursor)
        if result:
            result = Courses.convert_to_object(result)
            return result[0]
        return []

    # query with filter, use True exact match for exact match duh
    # RETURNS A LIST OF ROWS SO IT NEEDS TO BE INDEXED
    def query_filter(all=False, course_code=None, course_name=None, resp_college=None, order_by='resp_college', order='DESC'):
        cursor = mysql.connection.cursor()
        sql = ''
        if course_code:
            sql = f"SELECT * FROM courses where course_code LIKE '%{course_code}%'"
        if course_name:
            sql = f"SELECT * FROM courses where course_name LIKE '%{course_name}%'"
        if resp_college:
            sql = f"SELECT * FROM courses where resp_college LIKE '%{resp_college}%'"
        order = f" ORDER BY {order_by} {order};"
        if all:
            sql = f"SELECT * FROM courses"
        sql = sql+order
        cursor.execute(sql)
        result = result_zip(cursor)
        result = Courses.convert_to_object(result)
        if course_name:
            return result[0]
        return result


    @classmethod
    def update_course(cls, target_course, new_course_code=None, new_course_name=None, resp_college=None):
        cursor = mysql.connection.cursor()
        if new_course_code:
            sql = f"UPDATE courses SET course_code = '{new_course_code}' WHERE course_code ='{target_course}'"
        if new_course_name:
            sql = f"UPDATE courses SET course_name = '{new_course_name}' WHERE course_code ='{target_course}'"
        if resp_college:
            sql = f"UPDATE courses SET resp_college = '{resp_college}' WHERE course_code='{target_course}'"
        cursor.execute(sql)


    @classmethod
    def delete(cls, target_course):
        cursor = mysql.connection.cursor()
        sql = f"DELETE FROM courses WHERE course_code = '{target_course}';"
        cursor.execute(sql)

class Students():
    def __init__(self, id=None, first_name=None, course=None, last_name = None, gender=None, year_lvl=None, college=None):
        self.id = id
        self.first_name = first_name
        self.course = course
        self.last_name = last_name
        self.gender = gender
        self.year_lvl = year_lvl
        self.college = college

    @classmethod
    def convert_to_object(cls, rows):
        if not rows:
            return []
        object_results = []
        for row in rows:
            new_obj = Students(
                id=row['id'],
                first_name=row['first_name'],
                course=row['course'],
                college=row['college'],
                last_name=row['last_name'],
                gender=row['gender'],
                year_lvl=row['year_lvl']
            )
            object_results.append(new_obj)
        return object_results

    def add(self): 
        cursor = mysql.connection.cursor()
        sql = f"INSERT INTO students(id, first_name, course, college, last_name, gender, year_lvl) VALUES('{self.id}', '{self.first_name}', '{self.course}','{self.college}', '{self.last_name}', '{self.gender}', '{self.year_lvl}')"
        cursor.execute(sql)

    @classmethod
    def query_get(cls, id):
        cursor = mysql.connection.cursor()
        sql = f"SELECT * FROM students where id = '{id}'"
        cursor.execute(sql)
        result = result_zip(cursor)
        if result:
            result = Students.convert_to_object(result)
            return result[0]
        return []

    # query with filter, use True exact match for exact match duh
    # RETURNS A LIST OF ROWS SO IT NEEDS TO BE INDEXED
    def query_filter(all=False, id=None, first_name=None, course=None, college=None, last_name=None, gender=None, year_lvl=None, order_by='id', order='DESC'):
        cursor = mysql.connection.cursor()
        sql = ''
        if id:
            sql = f"SELECT * FROM students where id LIKE '%{id}%'"
        if first_name:
            sql = f"SELECT * FROM students where first_name LIKE '%{first_name}%'"
        if course:
            sql = f"SELECT * FROM students where course LIKE %'{course}'%"
        if college:
            sql = f"SELECT * FROM students where college LIKE %'{college}'%"
        if last_name:
            sql = f"SELECT * FROM students where last_name LIKE %'{last_name}'%"
        if gender:
            sql = f"SELECT * FROM students where gender LIKE %'{gender}'%"
        if year_lvl:
            sql = f"SELECT * FROM students where year_lvl LIKE %'{year_lvl}'%"
        order = f" ORDER BY {order_by} {order};"
        if all:
            sql = f"SELECT * FROM students"
        sql = sql+order
        cursor.execute(sql)
        result = result_zip(cursor)
        result = Students.convert_to_object(result)
        if id:
            return result[0]
        return result


    @classmethod
    def update_student(cls, target_student, new_id=None, new_first_name=None, new_course=None, new_college=None, new_last_name=None, new_gender=None, new_year_lvl=None):
        cursor = mysql.connection.cursor()
        if new_id:
            sql = f"UPDATE students SET id = '{new_id}' WHERE id ='{target_student}'"
        if new_first_name:
            sql = f"UPDATE students SET first_name = '{new_first_name}' WHERE id ='{target_student}'"
        if new_course:
            sql = f"UPDATE students SET course = '{new_course}' WHERE id ='{target_student}'"
        if new_college:
            sql = f"UPDATE students SET college = '{new_college}' WHERE id ='{target_student}'"
        if new_last_name:
            sql = f"UPDATE students SET last_name = '{new_last_name}' WHERE id ='{target_student}'"
        if new_gender:
            sql = f"UPDATE students SET gender = '{new_gender}' WHERE id ='{target_student}'"
        if new_year_lvl:
            sql = f"UPDATE students SET year_lvl = '{new_year_lvl}' WHERE id ='{target_student}'"
        cursor.execute(sql)


    @classmethod
    def delete(cls, target_student):
        cursor = mysql.connection.cursor()
        sql = f"DELETE FROM students WHERE id = '{target_student}';"
        cursor.execute(sql)