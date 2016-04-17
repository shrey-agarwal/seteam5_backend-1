from flask import Flask, request, jsonify, render_template

import cloud_messaging
import database_driver
import util

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello world!', 201


@app.route('/userinfo/', methods=['POST'])
def post_userinfo():
    if 'phonenumber' not in request.form:
        return 'Missing phonenumber', 400
    current_info = database_driver.get_userinfo(request.form['phonenumber'])
    if current_info:
        return 'Data exist! make put request to entirely replace', 409
    result = database_driver.post_userinfo(request.form)
    if not result:
        return 'Illegal request', 400
    else:
        return 'Success', 201


@app.route('/userinfo/<phonenumber>', methods=['GET'])
def get_userinfo(phonenumber):
    info = database_driver.get_userinfo(phonenumber)
    if not phonenumber or not info:
        return 'Not found', 404
    return jsonify(info)


@app.route('/admin/login')
def admin_login():
    return render_template("admin_login.html")


@app.route('/admin_student_status.html', methods=['GET'])
def admin_student_status():
    pending = database_driver.get_students_info({"status": {"$exists": False}})
    approoved = database_driver.get_students_info({"status": "aproove"})
    declined = database_driver.get_students_info({"status": "decline"})
    return render_template('admin_student_status.html', pending=pending,
                           approoved=approoved, declined=declined)


@app.route('/admin_student_status.html', methods=['POST'])
def admin_student_status_update():
    update = {"phonenumber": request.form['phonenumber'],
              "status": request.form['status'],
              }
    database_driver.update_student_info(update)
    return '', 200


@app.route('/route_manage.html')
def manage_route_html():
    unassigned_students = database_driver.get_unassigned_students()
    routes = {'A': [],
              'B': [],
              'C': [],
              }
    for student in database_driver.get_assigned_students():
        routes[student['route']].append(student)
    return render_template('route_manage.html',
                           unassigned_students=unassigned_students,
                           routes=routes)


@app.route('/register_token/', methods=['POST'])
def register_token():
    phonenumber = request.form.get('phonenumber')
    token = request.form.get('token')
    database_driver.register_token(phonenumber, token)
    return 'registered successfully', 200


@app.route('/send_message/', methods=['POST'])
def send_message():
    from_ = request.form.get('phonenumber')
    message = request.form.get('message')
    cloud_messaging.send_message(from_, '', message)
    return jsonify(request.form)


@app.route('/google95f9878b0eb7c516.html')
def verify():
    return render_template('google94f9878b0eb7c516.html')


@app.route('/update_user_location/', methods=['POST'])
def update_user_location():
    if 'phonenumber' not in request.form:
        return 'Missing phonenumber', 400
    info = database_driver.get_userinfo(request.form['phonenumber'])
    if not info:
        return 'user does not exist. register first', 409
    if 'location' not in request.form:
        return 'location does not exist', 409
    phonenumber = request.form.get('phonenumber')
    location = request.form.get('location')
    if database_driver.update_user_location(phonenumber, location):
        return 'updated successfully', 200


@app.route('/emergency/', methods=['POST'])
def send_emergency_update():
    for guardian in util.get_guardian_phonenumbers():
        cloud_messaging.send_sms(guardian,
                                 request.form.get('message'))

    return 'sent', 200


@app.route('/add_student_route/', methods=['POST'])
def add_student_route():
    phonenumber = request.form.get('phonenumber')
    route = request.form.get('route')
    updated_info = {'phonenumber': phonenumber,
                    'route': route,
                    }
    database_driver.update_student_route(updated_info)
    return ''

@app.route('/guardianLogin', methods=['POST'])
def add_guardinfo():
    if 'phonenumber' not in request.form:
        return 'Missing phonenumber', 400
    if 'name' not in request.form:
        return 'Missing name', 400
    if 'password' not in request.form:
        return 'Missing password', 400
    current_info = database_driver.get_userinfo(request.form['phonenumber'])
    if current_info:
    	data = request.form
    	result = database_driver.add_guardinfo(data)
    else:
    	return 'Invalid phonenumber', 400
    if not result:
    	return 'Illegal request', 400
    else:
    	return 'Success', 201


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
