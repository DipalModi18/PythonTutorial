# Flask maps HTTP requests to Python functions.
from flask import Flask
from flask_restful import Resource, Api
import pymysql

db = pymysql.connect("localhost", "root", "root", "TESTDB")
cursor = db.cursor()

# “__name__” is a Python special variable which gives Python file a unique name,
#       in this case, we are telling the app to run in this specific place.
app = Flask(__name__)  # app = flask.Flask(__name__)
# Creates the Flask application object,
#           which contains data about the application and also methods (object functions)
#           that tell the application to do certain actions. The last line, app.run(), is one such method.

api = Api(app)


class Employees(Resource):
    def get(self):
        sql = """select * from employee"""
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            print("Results: ", results)
            return {'employees': [i[0] for i in results]}
        except pymysql.DatabaseError:
            db.rollback()

    # def get(self, id):
    #     sql = """select * from employee where id=""" + id
    #     try:
    #         cursor.execute(sql)
    #         results = cursor.fetchall()
    #         return {'employee': results}
    #     except pymysql.DatabaseError:
    #         db.rollback()
    #
    def post(self, employee):
        sql = """insert into employee values(""" + employee + """,'dipal','modi', 30, 'F', 500000)"""
        try:
            cursor.execute(sql)
            status = db.commit()
        except pymysql.DatabaseError:
            db.rollback()
        return {'Insert status': status}


api.add_resource(Employees, '/employees')
# api.add_resource(Employees, '/employee/<int:id>')

if __name__ == '__main__':
    # app.run(host, port, debug, options)
     app.run(port='8080')
    # While running a flask application using the docker container,  you should be binding host to 0.0.0.0
    # if you want the container to be accessible from outside. i.e. app.run(host='0.0.0.0')

