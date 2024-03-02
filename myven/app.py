from flask import Flask, jsonify, request, render_template, redirect, url_for
from sql_connection import get_sql_connection
from add_to_db import insert_SERVICE,insert_customer,insert_laundry,insert_REVIEW,MAKE_ORDER
from fetch_data import get_servicelist,check_userid,check_laundryid
import json

connection = get_sql_connection()
# MAKE_ORDER(connection,CUSTOMER_ID,LAUNDRY_ID,ORDER_DATE,AMOUNT)
# insert_REVIEW(connection,CUSTOMER_ID,LAUNDRY_ID,REVIEW)
# insert_laundry(connection,LAUNDRY_NAME,STREET_NAME,VILLAGE,CITY,STATE,PHNO,PASSWORD)
# insert_customer(connection,CUSTOMER_NAME,STREET_NAME,VILLAGE,CITY,STATE,PHNO,PASSWORD)
# insert_SERVICE(connection,LAUNDRY_ID,DEC,PRICE)
    

app = Flask(__name__)


def register_user(user_id, name, street_name, village, city, state, phone_no, password):
    global connection
    insert_customer(connection,user_id, name, street_name, village, city, state, phone_no, password)

def register_laundry(laundry_id, name, street_name, village, city, state, phone_no, password):
    global connection
    insert_laundry(connection,laundry_id, name, street_name, village, city, state, phone_no, password)

# def authenticate_user(user_id, password):
#     # Implement the logic to check user credentials in your database
#     # Return True if authentication is successful, otherwise return False
#     # Example logic: (replace this with your database query)
#     if user_id == "anush" and password == "123":
#         return True
#     else:
#         return False
    

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
    user_id = request.args.get('user_id')  # Retrieve user_id from query parameter
    return render_template('home.html', user_id=user_id)

@app.route('/laundryhome')
def laundryhome():
    return render_template('laundryhome.html')

@app.route('/placeorder')
def placeorder():
    user_id = request.args.get('user_id')
    laundry_id = request.args.get('laundry_id')
    return render_template('placeorder.html', user_id=user_id, laundry_id=laundry_id)

# @app.route('/home')
# def home():
#     return render_template('home.html')


@app.route('/userauthenticate', methods=['POST'])
def userauthenticate():
    global connection
    try:
        request_data = request.get_json()
        user_id = request_data.get('user_id')
        password = request_data.get('password')

        if not user_id or not password:
            return jsonify({'status': 'failure', 'message': 'User ID and password are required'}), 400

        if check_userid(connection,user_id,password) == True:    
            # Redirect to home page if authentication is successful
            return jsonify({'status': 'success', 'message': 'Authentication successful', 'user_id': user_id}), 200
        else:
            return jsonify({'status': 'failure', 'message': 'Authentication failed'}), 401

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/laundryauthenticate', methods=['POST'])
def laundryauthenticate():
    global connection
    try:
        request_data = request.get_json()
        laundry_id = request_data.get('laundry_id')
        password = request_data.get('password')
        print(laundry_id,password)

        if not laundry_id or not password:
            return jsonify({'status': 'failure', 'message': 'User ID and password are required'}), 400

        if check_laundryid(connection,laundry_id,password) == True:
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
        register_user(user_id, name, street_name, village, city, state, phone_no, password)

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
        register_laundry(laundry_id, name, street_name, village, city, state, phone_no, password)

        return jsonify({'status': 'success', 'message': 'Registration successful'}), 200

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

    
@app.route('/get_laundry_list', methods=['POST'])
def get_laundry_list():
    try:
        print("Received request to get laundry list")
        
        request_data = request.get_json()
        user_id = request_data.get('user_id')
        location = request_data.get('location')

        print(f"User ID: {user_id}, Location: {location}")

        # Implement logic to generate multidimensional array based on the location
        # Example: laundry_list = [[1, 'Laundry A'], [2, 'Laundry B'], ...]

        laundry_list = [
            [1, 'Laundry A'],
            [2, 'Laundry B'],
            [3,'aanush ']
            # Add more laundry entries as needed
        ]

        print(f"Generated Laundry List: {laundry_list}")

        return jsonify({'status': 'success', 'laundry_list': laundry_list})
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/get_services')
def get_services():
    laundry_id = request.args.get('laundry_id')

    # Use laundry_id to fetch services from the database or any other source
    # Replace the following line with your actual logic to get services
    if laundry_id == '2':
        services_list = [['Service A', 10], ['Service B', 15], ['Service C', 20]]
    else:
        services_list = [['Service A', 10], ['Service B', 15]]

    return jsonify({'status': 'success', 'services_list': services_list})

@app.route('/place_order', methods=['POST'])
def place_order():
    try:
        request_data = request.get_json()
        user_id = request_data.get('user_id')
        laundry_id = request_data.get('laundry_id')
        total_amount = request_data.get('total_amount')

        # Process the order details, e.g., save to the database
        # Replace the following lines with your actual logic
        print(f"Received order from User ID: {user_id}, Laundry ID: {laundry_id}")
        print(f"Total Amount: {total_amount}")

        return jsonify({'status': 'success', 'message': 'Order confirmed'})
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