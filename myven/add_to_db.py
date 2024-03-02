# from sql_connection import get_sql_connection

# connection = get_sql_connection()

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
    query = "INSERT INTO SERVICES (LAUNDRY_ID,DESCRIPTION,PRICE) VALUES ({},'{}',{});".format (LAUNDRY_ID,DEC,PRICE)
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

# insert_SERVICE(connection,1,"iron",10)
    

