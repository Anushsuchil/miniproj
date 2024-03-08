from flask import Flask, jsonify, request, render_template, redirect, url_for
from sql_connection import get_sql_connection
from add_to_db import insert_SERVICE,insert_customer,insert_laundry,insert_REVIEW,insert_order,delete_order
from fetch_data import check_userid,check_laundryid,get_laundry,fetch_services_list,get_pending_order,get_laundry_review,get_completed_order
import json
from datetime import datetime

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

def register_service(LAUNDRY_ID,DEC,PRICE):
    global connection
    insert_SERVICE(connection,LAUNDRY_ID,DEC,PRICE)

def get_laundry_items(location):
    global connection
    b = get_laundry(connection,location)
    return b

def get_services_list(laundry_id):
    global connection
    b = fetch_services_list(connection,laundry_id)
    return b 

def update_order(user_id,laundry_id,current_date,total_amount):
    global connection
    b = insert_order(connection,user_id,laundry_id,current_date,total_amount)
    return b

def get_orders_list(laundry_id):
    global connection
    b = get_pending_order(connection,laundry_id)
    return b

def add_review(CUSTOMER_ID,LAUNDRY_ID,REVIEW):
    insert_REVIEW(connection,CUSTOMER_ID,LAUNDRY_ID,REVIEW)
    
def get_review(LAUNDRY_ID):
    b = get_laundry_review(connection,LAUNDRY_ID)
    return b

def get_completed_orders(LAUNDRYID):
    b = get_completed_order(connection, LAUNDRYID)
    return b


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
def laundry_home():
    return render_template('laundryhome.html')

@app.route('/placeorder')
def placeorder():
    user_id = request.args.get('user_id')
    laundry_id = request.args.get('laundry_id')
    return render_template('placeorder.html', user_id=user_id, laundry_id=laundry_id)

@app.route('/review')
def review():
    return render_template('review.html')

# @app.route('/home')
# def home():
#     return render_template('home.html')
@app.route('/completed_orders')
def completed_orders():
    # Retrieve the laundry id from the query parameters
    laundry_id = request.args.get('laundry_id')
    completed_orders_data = get_completed_orders(laundry_id)
    # Fetch completed orders data based on the laundry id
    # laundry_completed_orders = [order for order in completed_orders_data if order[2] == int(laundry_id)]

    return render_template('completedorders.html', completed_orders=completed_orders_data)

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
        laundry_list = get_laundry_items(location)

        # laundry_list = [
        #     [1, 'Laundry A'],
        #     [2, 'Laundry B'],
        #     [3,'aanush ']
        #     # Add more laundry entries as needed
        # ]

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
    services_list = get_services_list(laundry_id)
    # if laundry_id == '2':
    #     services_list = [['Service A', 10], ['Service B', 15], ['Service C', 20]]
    # else:
    #     services_list = [['Service A', 10], ['Service B', 15]]

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
        current_date = datetime.now().date()
        update_order(user_id,laundry_id,current_date,total_amount)
        return jsonify({'status': 'success', 'message': 'Order confirmed'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500
    

@app.route('/get_orders')
def get_orders():
    laundry_id = request.args.get('laundry_id')

    # Use laundry_id to fetch orders from the database or any other source
    # Replace the following line with your actual logic to get orders
    orders_list = get_orders_list(laundry_id)
    # orders_list = [[1, '2024-03-01', 50, 'Customer A', '1234567890'],
    #                [2, '2024-03-02', 75, 'Customer B', '9876543210']]

    return jsonify({'status': 'success', 'orders_list': orders_list})

@app.route('/mark_order_completed')
def mark_order_completed():
    order_id = request.args.get('order_id')
    delete_order(connection,order_id)

    # Use order_id to mark the order as completed in the database or any other source
    # Replace the following line with your actual logic to mark order as completed
    # Simulating a success response
    return jsonify({'status': 'success'})

@app.route('/get_reviews', methods=['GET'])
def get_reviews():
    laundry_id = request.args.get('laundry_id')
    # Fetch reviews from the database or any other source based on the laundry_id
    # Replace the following line with your actual logic to fetch reviews
    reviews_list = get_review(laundry_id)
    return jsonify({'status': 'success', 'reviews_list': reviews_list})

@app.route('/submit_review', methods=['POST'])
def submit_review():
    data = request.get_json()
    user_id = data.get('user_id')
    laundry_id = data.get('laundry_id')
    review = data.get('review')
    add_review(user_id,laundry_id,review)

    # Add logic to store the review in the database or any other source
    # Replace the following line with your actual logic to store reviews
    # Simulating a success response
    return jsonify({'status': 'success'})

@app.route('/add_service', methods=['POST'])
def add_service():
    try:
        # Get service details from the request
        service_data = request.json

        # Extract data from the request
        laundry_id = service_data.get('laundry_id')
        description = service_data.get('description')
        price = service_data.get('price')

        # Validate data (you may want to add more validation)
        if laundry_id is None or description is None or price is None:
            return jsonify({'status': 'error', 'message': 'Invalid data'})

        # Add service to the database
        register_service(laundry_id,description,price)
        # Return success response
        return jsonify({'status': 'success', 'message': 'Service added successfully'})

    except Exception as e:
        # Handle exceptions (log them or return an error response)
        print(f"Error adding service: {str(e)}")
        return jsonify({'status': 'error', 'message': 'Internal Server Error'})

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