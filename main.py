from fastapi import FastAPI
from indb import generate_products
from product import Product
from json_db import JsonDB
app = FastAPI()

productDB = JsonDB(path="./data/products.json")

@app.get("/products")
def get_products():
    products = productDB.read()
    return { "products": products}

@app.post("/products")
def create_products(product: Product):
    
    print("new product", product)
    
    productDB.insert(product)
    
    return { "status": "inserted", "product": product}