from flask import Flask, request, render_template
import db
# import json
import simplejson as json

app = Flask(__name__)


@app.route('/offices/')
def office():
    office_code = request.args.get('id')
    database_in_string = ""
    if office_code is not None:
        database_in_string = json.dumps(db.office_from_database(office_code))
    else:
        database_in_string = json.dumps(db.offices_from_database())
    return database_in_string


@app.route('/employees/')
def employee():
    employee_number = request.args.get('id')
    database_in_string = ""
    if employee_number is not None:
        database_in_string = json.dumps(db.employee_from_database(employee_number))
    else:
        database_in_string = json.dumps(db.employees_from_database())
    return database_in_string


@app.route('/productlines/')
def product_lines():
    database_in_string = ""
    product_code = request.args.get('id')
    if product_code is not None:
        database_in_string = json.dumps(db.product_line_from_database(product_code))
    else:
        database_in_string = json.dumps(db.products_lines_from_database())
    return database_in_string


@app.route('/products/')
def product():
    database_in_string = ""
    product_code = request.args.get('id')
    if product_code is not None:
        database_in_string = json.dumps(db.product_from_database(product_code))
    else:
        database_in_string = json.dumps(db.products_from_database())
    return database_in_string


if __name__ == '__main__':
    app.run()

