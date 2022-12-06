import mysql.connector

try:
    connection = mysql.connector.connect(host = 'localhost', user = 'root', password = '12345678', port=3306, auth_plugin='mysql_native_password', database='orders_management')
    cursor = connection.cursor()
    print("db Connected")

except mysql.connector.Error as err:
    print(err)
    input()
    exit
    

def insert_new_order(name, phone, address, shipment_date, payment_method, paid):
        sql = ("INSERT INTO orders "
        "(name, phone, address, shipment_date, payment_method, paid) "
        "VALUES (%s, %s, %s, %s, %s, %s)")
        execute(sql, False, [name, phone, address, shipment_date, payment_method, paid], True)

        
def remove_order(phone):
    sql = ("SELECT * FROM orders WHERE phone=%s")
    execute(sql, True, [phone])
    row_count = cursor.rowcount
    if row_count > 0:
        sql = ("DELETE FROM orders WHERE phone=%s")
        execute(sql, False, [phone], True)
        return True
    else:
        return False

    
def get_all_orders():
    sql = ("SELECT name, phone, address, shipment_date, payment_method, paid FROM orders ORDER BY shipment_date")
    results = execute(sql)
    return results


def get_next_five_days_orders():
    sql = ("SELECT name, phone, address, shipment_date, payment_method, paid FROM orders WHERE shipment_date <= DATE_ADD(CURDATE(), INTERVAL 5 DAY) AND shipment_date >= CURDATE() ORDER BY shipment_date")
    results = execute(sql)
    return results


def execute(tuple, single = False, args = {}, commit = False):
    cursor.execute(tuple, args)
    if commit == True:
        connection.commit()
    else:
        if single == True:
            return cursor.fetchone()
        else:
            return cursor.fetchall()

def lastrowid():
    return cursor.lastrowid

def close():
    connection.close()