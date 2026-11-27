import json
import hashlib
import secret
database = json.loads(open("database.json", 'r',encoding='utf-8').read())

def check_name_in_db(name):
    for name_indb in database:
        if name == name_indb:
            return True
        else:
            return False


def add_to_database(name):
    if check_name_in_db(name):
        return False
    if check_name_in_db(name) == False:
        database.update({name:{'role':'user','заказы':{}}})
        print(database)
        json.dump(database,open('database.json','w',encoding='utf-8'),ensure_ascii=False)
        return True

def if_admin(name):
    for ids in database:
        if name == ids:
            if database[ids]['role'] == 'admin':
                return True
def check_adminpass():
    admpass = input('Введите пароль от admin')
    if hashlib.md5(bytes(admpass,'utf-8')).hexdigest() == secret.admin_pass:
        return True
    else:
        return False



def set_order_status(name,order,status):
    if status == 'making' or status == 'completed':
        database[name]['заказы'][order]['status'] = status
        json.dump(database,open('database.json','w',encoding='utf-8'),ensure_ascii=False)
def get_last_order(name):
    default_last = 0
    last = default_last
    for order_id in database[name]['заказы']:
        last +=1
    return last

def create_order(name,last_order):
    order_id = last_order + 1
    database.update({name: {'заказы':{order_id:{'status':'making'}}}})
    json.dump(database,open('database.json','w',encoding='utf-8'),ensure_ascii=False)
    return order_id
def get_orders(name):
    orders = database[name]['заказы']
    number_orders = []
    for order_id in orders:
        number_orders.append(order_id)
    return number_orders

def get_order_status(name,order_id):
    order = database[name]['заказы'][order_id]
    order_status = order['status']
    return order_status



