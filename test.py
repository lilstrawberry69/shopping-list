import shelve
import uuid
import Product
product_dict = {}
db = shelve.open('productStorage', 'c')
product_id = 1
db['product'] = Product.product(uuid.uuid1(),'1',2,3)
db['product'] = product_dict
db.close()
