import requests
import json
import psycopg2
from pprint import pprint


db_params = {
    'database': 'oy_5_dars_9_homework',
    'user': 'postgres',
    'password': 'google_0330',
    'host': 'localhost',
    'port': 5432}

class DBConnect:
    def __init__(self, db_params):
        self.db_params = db_params

    def __enter__(self):
        self.conn = psycopg2.connect(**db_params)

        self.cur = self.conn.cursor()
        return self.conn, self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()

        if self.cur:
            self.cur.close()



# --Download from link

def download_file(url, filename):
    response = requests.get(url)
    with open(filename, 'w') as f:
        json.dump(response.json(), f, indent=4)
        print(response.status_code)
download_file("https://dummyjson.com/products", "main.json")



# -- Create Table

# with DBConnect(db_params) as (conn, cur):
#     create_table_book_query = """create table products(
#     id int not null,
#     title varchar(500) not null unique,
#     description varchar(500) not null unique,
#     category varchar(500) not null,
#     price float,
#     weight int);"""
#     cur.execute(create_table_book_query)
#     conn.commit()



# -- Get Data

with open('main.json', 'r') as f:
    data = json.load(f)
    products_info = data['products']



# -- Creat Data
# with DBConnect(db_params) as (conn, cur):
#
#     insert = f"""insert into products(id, title, description, category, price,weight)
#             values (%s, %s, %s, %s, %s, %s)"""
#
#     for products in products_info:
#         values = (products['id'], products['title'], products['description'],
#                products['category'], products['price'], products['weight'])
#
#         cur.execute(insert, values)
#         conn.commit()



# -- Show Data

# with DBConnect(db_params) as (conn, cur):
#     select_data_query = """select * from products"""
#     cur.execute(select_data_query)
#     all_products = cur.fetchall()
#     pprint(all_products)