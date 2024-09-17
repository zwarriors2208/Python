from flask import Flask, render_template, request, redirect, url_for, session

Shop = Flask(__name__)
Shop.secret_key = 'secret'
@Shop.route('/')
def home():
    return render_template('home3.html')

@Shop.route('/shipping', methods=['POST'])
def shipping():
    # product = request.form['product']
    # quantity = request.form['quantity']
    session['goods'] = request.form['product']
    session['number'] = request.form['quantity']
    return render_template('shipping.html')

@Shop.route('/summary', methods=['POST'])
def summary():
    name = request.form['f_name']
    p_number = request.form['p_n']
    pincode = request.form['pincode']
    address = request.form['address']
    city = request.form['city']
    goods  = session.get('goods')
    number = session.get('number')
    return render_template('summary.html', name = name, p_number = p_number, pincode = pincode, address = address, city = city, goods = goods, number = number)

@Shop.route('/confirm')
def confirm():
    return render_template('order.html')

if __name__ == '__main__':
    Shop.run(debug=True)