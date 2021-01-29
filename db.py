import mysql.connector


connection = mysql.connector.connect(host='localhost', port='3306', user='root', password='root', database='classic_models')


def create_url(extention, id):
    return f"http://localhost:5000/{extention}/?id={id}"


def employees_urls_list(officeCode):
    query = ("SELECT employeeNumber FROM employees WHERE officeCode = %s")
    cursor = connection.cursor()
    cursor.execute(query,(officeCode,))
    employees_ids = cursor.fetchall()
    employees_urls = []
    for employee in employees_ids:
        stripped_employee = (str(employee)).removeprefix('(').removesuffix(',)')
        employees_urls.append(create_url("employees", stripped_employee))
    return employees_urls


def offices_from_database():
    select_query = ("SELECT * FROM offices")

    cursor = connection.cursor(dictionary=True)
    cursor.execute(select_query)
    result = cursor.fetchall()
    for row in result:
        employees_ids_list = employees_urls_list(row.get('officeCode'))
        row["employeees"]= employees_ids_list
    return result


def office_from_database(id):
    select_query = ("SELECT * FROM offices WHERE officeCode = %s")

    cursor = connection.cursor(dictionary=True)
    cursor.execute(select_query, (id,))
    result = cursor.fetchall()
    employees_ids_list = employees_urls_list(id)
    result[0]["employees"]= employees_ids_list
    return result


def employees_from_database():
    select_query = ("SELECT * FROM employees")

    cursor = connection.cursor(dictionary=True)
    cursor.execute(select_query)
    result = cursor.fetchall()
    for row in result:
        if row['reportsTo'] is None:
            row.pop('reportsTo')
        else:
            row['reportsTo']= create_url("employees", row['reportsTo'])

    return result


def employee_from_database(employeeNumber):
    select_query = ("SELECT * FROM employees WHERE employeeNumber = %s")
    cursor = connection.cursor(dictionary=True)
    cursor.execute(select_query, (employeeNumber,))
    result = cursor.fetchall()
    result[0]['reportsTo']= create_url("employee", result[0]['reportsTo'])

    return result


def product_urls_list(product_line):
    query = ("SELECT productCode FROM products WHERE productLine = %s")
    cursor = connection.cursor()
    cursor.execute(query,(product_line,))
    product_ids = cursor.fetchall()
    product_urls = []
    for id in product_ids:
        stripped_product = (str(id)).removeprefix("(\'").removesuffix("\',)")
        product_urls.append(create_url("productline", stripped_product))
    return product_urls


def products_lines_from_database():
    select_query = ("SELECT * FROM productlines")

    cursor = connection.cursor(dictionary=True)
    cursor.execute(select_query)
    result = cursor.fetchall()
    for row in result:
        products_ids_list = product_urls_list(row.get('productLine'))
        row["products"]= products_ids_list
    return result


def product_line_from_database(productline):
    select_query = ("SELECT * FROM productlines WHERE productLine = %s")
    cursor = connection.cursor(dictionary=True)
    cursor.execute(select_query, (productline,))
    result = cursor.fetchall()
    urls_list = product_urls_list(productline)
    result[0]["products"] = urls_list

    return result


def products_from_database():
    select_query = ("SELECT * FROM products")

    cursor = connection.cursor(dictionary=True)
    cursor.execute(select_query)
    result = cursor.fetchall()
    for row in result:
        row['productLine'] = create_url("productline", row['productLine'])
    print(result)
    return result


def product_from_database(productCode):
    select_query = ("SELECT * FROM products WHERE productCode = %s")
    cursor = connection.cursor(dictionary=True)
    cursor.execute(select_query, (productCode,))
    result = cursor.fetchall()
    result[0]['productLine']= create_url("productline", result[0]['productLine'])

    return result
