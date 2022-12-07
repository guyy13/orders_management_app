import mysql.connector

try:
    connection = mysql.connector.connect(host = 'localhost', user = 'root', password = '12345678', port=3306, auth_plugin='mysql_native_password', database='orders_management')
    cursor = connection.cursor()
    print("db Connected")

except mysql.connector.Error as err:
    print(err)
    input()
    exit
    

def insert_new_order(name, phone, address, shipment_date, payment_method, paid, delivered):
        sql = ("INSERT INTO orders " "(name, phone, address, shipment_date, payment_method, paid, delivered) " "VALUES (%s, %s, %s, %s, %s, %s, %s)")
        execute(sql, False, [name, phone, address, shipment_date, payment_method, paid, delivered], True)

        
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
    
    
def is_order_exists(phone):
    sql = ("SELECT * FROM orders WHERE phone=%s")
    execute(sql, True, [phone])
    row_count = cursor.rowcount
    if row_count > 0:
        return True
    return False

def get_order_details(phone):
    sql = ("SELECT * FROM orders WHERE phone=%s")
    order_details = execute(sql, True, [phone])
    return order_details

    
def update_order(name, phone, address, shipment_date, payment_method, paid, delivered):
    sql = ("""UPDATE orders SET name = %s, phone = %s, address = %s, shipment_date = %s, payment_method = %s, paid = %s, delivered = %s WHERE phone = %s""")
    execute(sql, False, [name, phone, address, shipment_date, payment_method, paid, delivered, phone], True)
        
    
def get_all_orders():
    sql = ("SELECT name, phone, address, shipment_date, payment_method, paid, delivered FROM orders ORDER BY shipment_date")
    results = execute(sql)
    return results


def get_next_five_days_orders():
    sql = ("SELECT name, phone, address, shipment_date, payment_method, paid, delivered FROM orders WHERE shipment_date <= DATE_ADD(CURDATE(), INTERVAL 5 DAY) AND shipment_date >= CURDATE() AND delivered = 'לא נמסר' ORDER BY shipment_date;")
    results = execute(sql)
    return results

def get_undelivered_orders():
        sql = ("SELECT name, phone, address, shipment_date, payment_method, paid, delivered FROM orders WHERE delivered = %s ORDER BY shipment_date")
        results = execute(sql, False, ['לא נמסר'], False)
        return results
    
def get_units_delivered():
    sql = ("SELECT COUNT(*) FROM orders WHERE delivered = %s")
    results = execute(sql, False, ['נמסר'], False)
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