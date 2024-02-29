from flask import Flask, jsonify, request, render_template, redirect, url_for
from sql_connection import get_sql_connection
from add_to_db import insert_SERVICE,insert_customer,insert_laundry,insert_REVIEW,MAKE_ORDER
from fetch_data import get_servicelist
import json

connection = get_sql_connection()
# MAKE_ORDER(connection,CUSTOMER_ID,LAUNDRY_ID,ORDER_DATE,AMOUNT)
# insert_REVIEW(connection,CUSTOMER_ID,LAUNDRY_ID,REVIEW)
# insert_laundry(connection,LAUNDRY_NAME,STREET_NAME,VILLAGE,CITY,STATE,PHNO,PASSWORD)
# insert_customer(connection,CUSTOMER_NAME,STREET_NAME,VILLAGE,CITY,STATE,PHNO,PASSWORD)
# insert_SERVICE(connection,LAUNDRY_ID,DEC,PRICE)
    

app = Flask(__name__)

def register_user(user_id, password, name, street_name, village, city, state, phone_no):
    print(user_id, password, name, street_name, village, city, state, phone_no)

def authenticate_user(user_id, password):
    # Implement the logic to check user credentials in your database
    # Return True if authentication is successful, otherwise return False
    # Example logic: (replace this with your database query)
    if user_id == "anush" and password == "123":
        return True
    else:
        return False
    

@app.route('/')   
def landing_page():
    return render_template('landing.html')
   
@app.route('/userauthentication')
def userauthentication():
    return render_template('userauthentication.html')

@app.route('/laundryauthentication')
def laundryauthentication():
    return render_template('laundryauthentication.html')

@app.route('/userregister')
def userregistration():
    return render_template('userregistration.html')

@app.route('/laundryregister')
def laundryregistration():
    return render_template('laundryregister.html')

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/userauthenticate', methods=['POST'])
def userauthenticate():
    try:
        request_data = request.get_json()
        user_id = request_data.get('user_id')
        password = request_data.get('password')

        if not user_id or not password:
            return jsonify({'status': 'failure', 'message': 'User ID and password are required'}), 400

        if authenticate_user(user_id, password):
            # Redirect to home page if authentication is successful
            return jsonify({'status': 'success', 'message': 'Authentication successful'}), 200
        else:
            return jsonify({'status': 'failure', 'message': 'Authentication failed'}), 401

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/laundryauthenticate', methods=['POST'])
def laundryauthenticate():
    try:
        request_data = request.get_json()
        user_id = request_data.get('laundry_id')
        password = request_data.get('password')

        if not user_id or not password:
            return jsonify({'status': 'failure', 'message': 'User ID and password are required'}), 400

        if authenticate_user(user_id, password):
            # Redirect to home page if authentication is successful
            return jsonify({'status': 'success', 'message': 'Authentication successful'}), 200
        else:
            return jsonify({'status': 'failure', 'message': 'Authentication failed'}), 401

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/userregister', methods=['POST'])
def user_registration():
    try:
        request_data = request.get_json()
        user_id = request_data.get('user_id')
        password = request_data.get('password')
        name = request_data.get('name')
        street_name = request_data.get('street_name')
        village = request_data.get('village')
        city = request_data.get('city')
        state = request_data.get('state')
        phone_no = request_data.get('phone_no')

        if not user_id or not password or not name or not street_name or not village or not city or not state or not phone_no:
            return jsonify({'status': 'failure', 'message': 'All fields are required'}), 400

        # Check if the user ID is already taken (you need to implement this logic)

        # Register the user
        register_user(user_id, password, name, street_name, village, city, state, phone_no)

        return jsonify({'status': 'success', 'message': 'Registration successful'}), 200

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500
    
    
@app.route('/laundryregister', methods=['POST'])
def laundry_registration():
    try:
        request_data = request.get_json()
        laundry_id = request_data.get('laundry_id')
        password = request_data.get('password')
        name = request_data.get('name')
        street_name = request_data.get('street_name')
        village = request_data.get('village')
        city = request_data.get('city')
        state = request_data.get('state')
        phone_no = request_data.get('phone_no')

        if not laundry_id or not password or not name or not street_name or not village or not city or not state or not phone_no:
            return jsonify({'status': 'failure', 'message': 'All fields are required'}), 400

        # Check if the user ID is already taken (you need to implement this logic)

        # Register the user
        register_user(laundry_id, password, name, street_name, village, city, state, phone_no)

        return jsonify({'status': 'success', 'message': 'Registration successful'}), 200

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500
    


if __name__ == '__main__':
    app.run(debug=True)

# @app.route('/insertcustomer', methods=['POST'])
# def insert_order():
#     request_payload = json.loads(request.form['data'])
#     CUSTOMER_ID = insert_customer(connection, request_payload)
#     response = jsonify({
#         'CUSTOMER_ID': CUSTOMER_ID
#     })
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response