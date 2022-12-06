from flask import Flask
from flask import render_template, request, redirect, url_for
from db import orders_db as db

app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_new_order', methods=['GET', 'POST'])
def add_new_order():
    if request.method == "GET":
        return render_template('add_new_order.html')
    else: # POST Method
        name = request.form['name']
        phone = request.form['phone']
        address = request.form['address']
        shipment_date = request.form['shipment_date']
        payment_method = request.form['payment_method']
        paid = request.form['paid']
        delivered = request.form['delivered']
        db.insert_new_order(name, phone, address, shipment_date, payment_method, paid, delivered)
        return render_template('add_new_order.html', success="0")
    
    
@app.route('/remove_order', methods=['GET', 'POST'])
def remove_order():
    if request.method == "GET":
        return render_template('remove_order.html')
    else: # POST Method
        phone = request.form['phone']
        db.remove_order(phone)
        return render_template('remove_order.html', success="0")
    
    
@app.route('/is_order_exists', methods=['POST'])
def is_order_exists():
    phone = request.form['phone']
    if db.is_order_exists(phone):
        order_details = db.get_order_details(phone)
        name = order_details[1]
        address = order_details[3]
        shimpent_date = order_details[4]
        payment_method = order_details[5]
        paid = order_details[6]
        delivered = order_details[7]
        return render_template('update_order.html', is_exists="True",name=name, phone=phone, address=address, shimpent_date=shimpent_date, payment_method=payment_method, paid=paid, delivered=delivered)
    else:
        return render_template('update_order.html', is_exists="False")
        
    
@app.route('/update_order', methods=['GET', 'POST'])
def update_order():
    if request.method == "GET":
        return render_template('update_order.html')
    else:
        name = request.form['name']
        phone = request.form['phone']
        address = request.form['address']
        shipment_date = request.form['shipment_date']
        payment_method = request.form['payment_method']
        paid = request.form['paid']
        delivered = request.form['delivered']
        db.update_order(name, phone, address, shipment_date, payment_method, paid, delivered)
        return render_template('update_order.html', success="True")
    
@app.route('/view_all_orders', methods=['GET'])
def view_all_orders():
    order_list = db.get_all_orders()
    headings = ("שם מלא ", "מספר טלפון", "כתובת משלוח", "תאריך משלוח", "דרך תשלום", "האם שולם?",  "האם נמסר?")
    return render_template('view_all_orders.html', headings=headings, data=order_list)


@app.route('/view_next_five_days_orders', methods=['GET'])
def view_next_five_days_orders():
    order_list = db.get_next_five_days_orders()
    headings = ("שם מלא ", "מספר טלפון", "כתובת משלוח", "תאריך משלוח", "דרך תשלום", "האם שולם?", "האם נמסר?")
    return render_template('view_next_five_days_orders.html', headings=headings, data=order_list)


@app.route('/view_all_orders_undelivered', methods=['GET'])
def view_all_orders_undelivered():
    order_list = db.get_undelivered_orders()
    headings = ("שם מלא ", "מספר טלפון", "כתובת משלוח", "תאריך משלוח", "דרך תשלום", "האם שולם?", "האם נמסר?")
    return render_template('view_undelivered_orders.html', headings=headings, data=order_list)

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)