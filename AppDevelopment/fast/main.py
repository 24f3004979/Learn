from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Base data flow structure with the application
class Item(BaseModel):
    item_id : int
    name : str
    price : float
    is_offer : bool | None = None

'''
Designing End points with fast api is bless
    With intuitive structure for declaring the end point with just logical words

    With pydantic we have made a structure js to follow for making the request into the put endpoint
'''

@app.get('/')
def root():
    return "Hello world"

@app.get("/items/{item_id}")
def item(item_id:int, q:str | None = None):
    return {"item_id":item_id, "q":q}

@app.put("/items/{item_id}")
def into_server(item_id:int, item:Item):
    return {"item_name" : item.name,  "item_id" : item.item_id}


