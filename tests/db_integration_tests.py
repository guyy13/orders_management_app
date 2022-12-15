import datetime
import sys
sys.path.insert(0, '../backend/')

import orders_db as db

def test_add_new_order():
    db.insert_new_order('pytesting', 99999999, 'pytesting address', datetime.datetime.now(), 'paid', 'bit', 'delivered', 5)
    assert db.is_order_exists(99999999) == True, "Didnt insert order to database"
    if db.is_order_exists(99999999) == True:
        db.remove_order(99999999)
        

    




