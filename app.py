from flask import Flask, request
from db import stores, items


app = Flask(__name__)

@app.get("/store")
def get_stores():
    return {"stores": stores}

@app.post("/store")
def create_store():
    request_data = request.get_json()
    newStore = {"name": request_data["name"], "items": []}
    stores.append(newStore)
    
    return newStore, 201

@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            newItem = {"name": request_data["name"], "price":request_data["price"]}
            store["items"].append(newItem)
            return newItem, 201
        
    return {"message":"Store not found"}, 404

@app.get("/store/<string:name>")
def getStoreByName(name):
    for store in stores:
        if store["name"] == name:
            return store
        
    return {"message":"Store not found"}, 404

@app.get("/store/<string:name>/item")
def getStoreItemByName(name):
    for store in stores:
        if store["name"] == name:
            return store["items"]
        
    return {"message":"Store not found"}, 404