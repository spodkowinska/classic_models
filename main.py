from flask import Flask, request, render_template
import db
# import json
import simplejson as json

app = Flask(__name__)


@app.route('/offices')
def offices():
    database_in_string = ""
    database_in_string = json.dumps(db.offices_from_database())
    return database_in_string


@app.route('/offices/')
def office():
    office_code = request.args.get('id')
    database_in_string = ""
    database_in_string = json.dumps(db.office_from_database(office_code))
    return database_in_string


@app.route('/employees')
def employees():
    database_in_string = ""
    database_in_string = json.dumps(db.employees_from_database())
    return database_in_string


@app.route('/employees/')
def employee():
    employee_number = request.args.get('id')
    database_in_string = ""
    database_in_string = json.dumps(db.employee_from_database(employee_number))
    return database_in_string


@app.route('/productlines')
def product_lines():
    database_in_string = ""
    database_in_string = json.dumps(db.product_lines_from_database())
    return database_in_string


@app.route('/productlines/')
def product_line():
    product_code = request.args.get('id')
    database_in_string = ""
    database_in_string = json.dumps(db.product_line_from_database(product_code))
    return database_in_string


@app.route('/products')
def product():
    database_in_string = ""
    database_in_string = json.dumps(db.products_from_database())
    return database_in_string


@app.route('/products/')
def products():
    product_code = request.args.get('id')
    database_in_string = ""
    database_in_string = json.dumps(db.product_from_database(product_code))
    return database_in_string


if __name__ == '__main__':
    # print(db.employees_urls_list())
    print(db.offices_from_database())
    app.run()

