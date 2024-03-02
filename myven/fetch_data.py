# from sql_connection import get_sql_connection
# connection = get_sql_connection()


def get_servicelist(connection,LAUNDRY_ID):
    query = "SELECT DESCRIPTION,PRICE FROM SERVICES WHERE LAUNDRY_ID = {};".format (LAUNDRY_ID)
    print(query)
    cur = connection.cursor()
    cur.execute(query)
    response = []
    for (DESCRIPTION,PRICE) in cur:
        response.append({
            'DESCRIPTION': DESCRIPTION,
            'PRICE': PRICE
        })
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

# b = check_laundryid(connection,'ganesh','13')
# print(b)