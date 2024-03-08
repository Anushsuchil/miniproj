# from sql_connection import get_sql_connection
# connection = get_sql_connection()


def fetch_services_list(connection,laundry_id):
    query = "SELECT DESCRIPTION,PRICE FROM SERVICES WHERE LAUNDRY_ID = '{}';".format (laundry_id)
    print(query)
    cur = connection.cursor()
    cur.execute(query)
    response = []
    for (DESCRIPTION,PRICE) in cur:
        response.append([DESCRIPTION,PRICE])
    return response

def check_userid(connection,USER_ID,PASSWORD):
    query = "SELECT CUSTOMER_ID FROM CUSTOMER WHERE CUSTOMER_ID = '{}' AND PASSWORD = '{}';".format (USER_ID,PASSWORD)
    cur = connection.cursor()
    cur.execute(query)
    response = cur.fetchone()
    print(response)
    if response == None:
        a = False
    else:
        a = True
    return a

def check_laundryid(connection,LAUNDRY_ID,PASSWORD):
    query = "SELECT LAUNDRY_ID FROM LAUNDRY WHERE LAUNDRY_ID = '{}' AND PASSWORD = '{}';".format (LAUNDRY_ID,PASSWORD)
    cur = connection.cursor()
    cur.execute(query)
    response = cur.fetchone()
    print(response)
    if response == None:
        a = False
    else:
        a = True
    return a

def get_laundry(connection,location):
    query = "SELECT LAUNDRY_ID,LAUNDRY_NAME FROM LAUNDRY WHERE CITY = '{}';".format (location)
    cur = connection.cursor()
    cur.execute(query)
    response = []
    for (LAUNDRY_ID,LAUNDRY_NAME) in cur:
        response.append([LAUNDRY_ID,LAUNDRY_NAME])
    return response

def get_laundry_review(connection,LAUNDRY_ID):
    query = "SELECT CUSTOMER_ID,REVIEWS FROM RATINGS WHERE LAUNDRY_ID = '{}';".format (LAUNDRY_ID)
    cur = connection.cursor()
    cur.execute(query)
    response = []
    for (CUSTOMER_ID,REVIEWS) in cur:
        response.append([CUSTOMER_ID,REVIEWS])
    return response

def get_completed_order(connection, LAUNDRYID):
        cur = connection.cursor()

        # Assuming your stored procedure takes one parameter, adjust accordingly
        cur.callproc("get_order_perday", (LAUNDRYID,))

        # If your stored procedure returns a result set, you can fetch it
        results = cur.stored_results()

        response = []
        
        for result in results:
            data = result.fetchall()
            response.extend(data)
        res = []
        for x in response:
            m = []
            for y in x:
                m.append(y)
            res.append(m)
        formatted_data = []

        for item in res:
            # Format the date as 'YYYY-M-D'
            formatted_date = item[3].strftime('%Y-%m-%d').lstrip('0')
                
            # Create a new list with the formatted date
            new_item = [item[0],item[1],item[2], formatted_date, item[4]]
                
            # Append the new item to the formatted_data list
            formatted_data.append(new_item)
        return formatted_data

def get_pending_order(connection,laundry_id):
    query = """SELECT O.ORDER_ID,O.ORDER_DATE,O.AMOUNT,C.CUSTOMER_NAME,C.PHNO 
                FROM LAUNDRY L,ORDERS O,CUSTOMER C
                WHERE L.LAUNDRY_ID = O.LAUNDRY_ID AND O.CUSTOMER_ID = C.CUSTOMER_ID AND L.LAUNDRY_ID = '{}';""".format (laundry_id)
    cur = connection.cursor()
    cur.execute(query)
    response = []
    for (ORDER_ID,ORDER_DATE,AMOUNT,CUSTOMER_NAME,PHNO) in cur:
        response.append([ORDER_ID,ORDER_DATE,AMOUNT,CUSTOMER_NAME,PHNO])
    
    formatted_data = []

    for item in response:
        # Format the date as 'YYYY-M-D'
        formatted_date = item[1].strftime('%Y-%m-%d').lstrip('0')
            
        # Create a new list with the formatted date
        new_item = [item[0], formatted_date] + item[2:]
            
        # Append the new item to the formatted_data list
        formatted_data.append(new_item)
    return formatted_data

# DELETE FROM `laundry_database`.`orders` WHERE (`ORDER_ID` = '3') and (`CUSTOMER_ID` = 'nik') and (`LAUNDRY_ID` = 'ganesh');

# b = get_completed_order(connection,'ganesh')
# print(b)