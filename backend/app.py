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
        db.insert_new_order(name, phone, address, shipment_date, payment_method, paid)
        return render_template('add_new_order.html', success="0")
    
    
@app.route('/remove_order', methods=['GET', 'POST'])
def remove_order():
    if request.method == "GET":
        return render_template('remove_order.html')
    else: # POST Method
        phone = request.form['phone']
        db.remove_order(phone)
        return render_template('remove_order.html', success="0")
    
    
@app.route('/view_all_orders', methods=['GET'])
def view_all_orders():
    order_list = db.get_all_orders()
    headings = ("שם מלא ", "מספר טלפון", "כתובת משלוח", "תאריך משלוח", "דרך תשלום", "האם שולם?")
    return render_template('view_all_orders.html', headings=headings, data=order_list)


@app.route('/view_next_five_days_orders', methods=['GET'])
def view_next_five_days_orders():
    order_list = db.get_next_five_days_orders()
    headings = ("שם מלא ", "מספר טלפון", "כתובת משלוח", "תאריך משלוח", "דרך תשלום", "האם שולם?")
    return render_template('view_next_five_days_orders.html', headings=headings, data=order_list)

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)