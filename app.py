from flask import Flask
from flask import request

app=Flask(__name__)
stores=[
    {"name":"vishal Mega Mart",
     "items":[
         {
     "name": "chair",
     "price": 780    
     }
     ]
}, 
{"name":"pantaloons",
 "items":[
     {
         "name": "jeans",
         "price": 1600
     }
 ]
},
    {"name": "Bigbaazar",
    "items":[
       {
        "name": "rice",
        "price": 1000
       }
   ]
   }, {"name":'easyday',
       "items":[
           {
               "name": "oil",
               "price":100
           }
       ]
   }
   ]


states=['New Delhi','Punjab','Haryana','Uttar Pardesh']

@app.get("/store")
def get_stores():
    return stores

@app.get("/states")
def get_states():
    return states

@app.post("/store")
def add_store():
    store=request.get_json()
    storname={"name":store["name"],"items":[]}
    stores.append(storname)
    return storname, 201


@app.post("/store/<string:name>/item")
def add_items(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name":request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message": "store not found"}, 404

@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store
    return {"message": "store not found"}, 404

@app.get("/store/<string:name>/items")
def get_store_items(name):
    for store in stores:
        if store["name"] == name:
            return store["items"]
    return {"message": "store not found"}, 404

if __name__== "__main__":
    app.run()