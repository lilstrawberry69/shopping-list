from flask import Flask, render_template, request, redirect, session, url_for
import shelve
import Product
import random
app = Flask(__name__)
@app.route('/')
def index():
    product_dict = {}
    db = shelve.open('productStorage', 'r')
    product_dict = db['product']
    product_list =[]
    count = 0
    for i in product_dict:
         product = product_dict[i]
         product_list.append(product)
         count+=1

    db.close()
    return render_template('Home.html',count = count, product_list=product_list)

@app.route('/add_product', methods=['POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']
        required_quantity = request.form['required quantity']
        product_dict = {}
        db = shelve.open('productStorage', 'c')
        product_dict = db['product']
        num_list = ['1','2','3','4','5','6','7','8','9']
        product_id = random.randint(1,1000000)
        product = Product.product(product_id,name,int(quantity),int(required_quantity))
        for i in product_dict:
            while i == product_id:
                product_id = random.randint(1,1000000)
        product_dict[product.get_id()] = product
        db['product'] = product_dict
        db.close()
        return redirect(url_for('index'))

@app.route('/edit_product/<int:id>', methods=['POST'])
def edit_product(id):
    if request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']
        required_quantity = request.form['required quantity']
        product_dict = {}
        db = shelve.open('productStorage', 'c')
        product_dict = db['product']
        product_id = id
        product = product_dict[id]
        product.set_name(name)
        product.set_quantity(int(quantity))
        product.set_required_quantity(int(required_quantity))
        db['product'] = product_dict
        db.close()
        return redirect(url_for('index'))
@app.route('/delete_product/<int:id>', methods=['POST'])
def delete_product(id):
    if request.method == 'POST':
        product_dict = {}
        db = shelve.open('productStorage', 'c')
        product_dict = db['product']
        product_dict.pop(id)
        db['product'] = product_dict
        db.close()
        return redirect(url_for('index'))

@app.route('/clear_balance', methods=['POST'])
def clear_balance():
    if request.method == 'POST':
        product_dict = {}
        db = shelve.open('productStorage', 'c')
        product_dict = db['product']
        for i in product_dict:
            product = product_dict[i]
            product.set_quantity(0)
        db['product'] = product_dict
        db.close()
        return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=False,host ='0.0.0.0')
