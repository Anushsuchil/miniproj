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