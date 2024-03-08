from sql_connection import get_sql_connection

connection = get_sql_connection()

def insert_customer(connection,CUSTOMER_ID,CUSTOMER_NAME,STREET_NAME,VILLAGE,CITY,STATE,PHNO,PASSWORD):
    query = "INSERT INTO customer (CUSTOMER_ID,CUSTOMER_NAME,STREET_NAME,VILLAGE,CITY,STATE,PHNO,PASSWORD) VALUES ('{}','{}','{}','{}','{}','{}',{},'{}');".format (CUSTOMER_ID,CUSTOMER_NAME,STREET_NAME,VILLAGE,CITY,STATE,PHNO,PASSWORD)
    print(query)
    cur = connection.cursor()
    cur.execute(query)
    connection.commit()
    return cur.lastrowid

def insert_laundry(connection,LAUNDRY_ID,LAUNDRY_NAME,STREET_NAME,VILLAGE,CITY,STATE,PHNO,PASSWORD):
    query = "INSERT INTO laundry (LAUNDRY_ID,LAUNDRY_NAME,STREET_NAME,VILLAGE,CITY,STATE,PHNO,PASSWORD) VALUES ('{}','{}','{}','{}','{}','{}',{},'{}');".format (LAUNDRY_ID,LAUNDRY_NAME,STREET_NAME,VILLAGE,CITY,STATE,PHNO,PASSWORD)
    print(query)
    cur = connection.cursor()
    cur.execute(query)
    connection.commit()

def insert_SERVICE(connection,LAUNDRY_ID,DEC,PRICE):
    query = "INSERT INTO SERVICES (LAUNDRY_ID,DESCRIPTION,PRICE) VALUES ('{}','{}',{});".format (LAUNDRY_ID,DEC,PRICE)
    print(query)
    cur = connection.cursor()
    cur.execute(query)
    connection.commit()

def insert_REVIEW(connection,CUSTOMER_ID,LAUNDRY_ID,REVIEW):
    query = "INSERT INTO RATINGS (CUSTOMER_ID,LAUNDRY_ID,REVIEWS) VALUES ('{}','{}','{}');".format (CUSTOMER_ID,LAUNDRY_ID,REVIEW)
    print(query)
    cur = connection.cursor()
    cur.execute(query)
    connection.commit()

def MAKE_ORDER(connection,CUSTOMER_ID,LAUNDRY_ID,ORDER_DATE,AMOUNT):
    query = "INSERT INTO ORDERS (CUSTOMER_ID,LAUNDRY_ID,ORDER_DATE,AMOUNT) VALUES ({},{},'{}',{});".format (CUSTOMER_ID,LAUNDRY_ID,ORDER_DATE,AMOUNT)
    print(query)
    cur = connection.cursor()
    cur.execute(query)
    connection.commit()

def insert_order(connection,user_id,laundry_id,current_date,total_amount):
    query = "INSERT INTO ORDERS (CUSTOMER_ID,LAUNDRY_ID,ORDER_DATE,AMOUNT) VALUES ('{}','{}','{}',{});".format (user_id,laundry_id,current_date,total_amount)
    print(query)
    cur = connection.cursor()
    cur.execute(query)
    connection.commit()

def delete_order(connection,order_id):
    query = "DELETE FROM ORDERS WHERE ORDER_ID = {};".format (order_id)
    print(query)
    cur = connection.cursor()
    cur.execute(query)
    connection.commit()

delete_order(connection,3)
    

