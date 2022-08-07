from flask import Flask, render_template, request, session, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = 'any random string'


@app.route('/')
def home_page():
    return render_template("home.html")


@app.route('/login')
def login_page():
    return render_template("login.html")


@app.route('/register')
def register_page():
    return render_template("register.html")


@app.route('/employee_home')
def employee_home():
    from DB_connection.customer_request import get_request_employee
    employee_id = session["user_id"]
    request_data=get_request_employee(employee_id)
    print(request_data)
    return render_template("employee_home.html",request_data=request_data)


@app.route('/new_service_request')
def new_service_request():
    from DB_connection.user_registration import get_employee_list
    employee_list = get_employee_list()
    print(employee_list)
    return render_template("new_service_request.html", employee_list=employee_list)


@app.route('/customer_home')
def customer_home():
    from DB_connection.customer_request import get_request
    customer_id = session["user_id"]
    request_data = get_request(customer_id)
    print(request_data)
    return render_template("customer_home.html", request_data=request_data)


@app.route('/customer_request_submit')
def customer_request_submit():
    return render_template("customer_request_submit.html")


@app.route('/api/register_user', methods=["post"])
def api_register_user():
    name = request.form.get('name')
    phone_number = request.form.get('phone_number')
    username = request.form.get('username')
    password = request.form.get('password')
    address = request.form.get('address')
    service_type = request.form.get('service_type')
    type = request.form.get('type')
    print(name)
    print(phone_number)
    print(username)
    print(password)
    print(address)
    print(type)
    print(service_type)
    from DB_connection.user_registration import insert_user
    insert_user(name, phone_number, username, password, address, type, service_type)
    return render_template("register.html")


@app.route('/api/login', methods=["post"])
def api_login():
    username = request.form.get('username')
    password = request.form.get('password')
    print(username)
    print(password)
    from DB_connection.user_registration import validate_user
    is_valid_user, role, user_id = validate_user(username, password)
    if is_valid_user == True:
        session["user_id"] = user_id
        if role == "customer":
            return redirect(url_for('customer_home'))
        else:
            return redirect(url_for("employee_home"))
    return render_template("login.html")


@app.route('/api/new_service_request', methods=["post"])
def api_new_service_request():
    service_type = request.form.get('service_type')
    employee_id = request.form.get('select_employee')
    created_date = request.form.get('date')
    request_time = request.form.get('time')
    customer_id = session["user_id"]
    is_complete = False
    print(service_type)
    print(employee_id)
    print(created_date)
    print(request_time)
    from DB_connection.customer_request import insert_request
    insert_request(employee_id, customer_id, is_complete, created_date, request_time, service_type)
    return render_template("new_service_request.html")

if __name__ == '__main__':
   if 'PORT' in os.environ:
      port = os.environ['PORT']
   else:
      port= 5000
   app.run(debug=False,host="0.0.0.0",port=port)
