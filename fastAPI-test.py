#this is a test file, where I test how an api works on a very basic level


# Import Union from the typing module to allow for type hints that can accept multiple types (basically a parameter can be multiple datatypes, when passing)
from typing import Union

# for creating the api and handling HTTPExceptions
from fastapi import FastAPI, HTTPException

# for validation of data
from pydantic import BaseModel

# used to specify values (see class Category for example)
from enum import Enum

#creating an intance, where I will be connection all the routes to 
app = FastAPI()

# Defining an enumeration class. This enumeration specifies the valid values that the 'category' field can take.
class Category(Enum): # <-- helper class
    TOOLS = "tools"
    CONSUMABLES = "consumables"

# defining a pydantic model. This model specifies the structure and types of data for items in the application.
class Item(BaseModel): # <-- helper class
    name: str
    price: float
    count: int
    id: int
    # category can only be tools or consumables
    category: Category

# simple dictionary that
items = {
    0: Item(name="Hammer", price=9.99, count=55, id=0, category=Category.TOOLS),
    1: Item(name="Cannon", price=499.99, count=6, id=1, category=Category.TOOLS),
    2: Item(name="Nails", price=4.99, count=1000, id=2, category=Category.CONSUMABLES)
}

# Fastapi handles JSON serialization and deserialization for us
# we simply use built-in python and pydantic types, in this case dict[int, item]
@app.get("/")
def index() -> dict[str, dict[int, Item]]:
    return {"items" : items}

#@app.get("/items/{item_id}")
def get_item_by_id(item_id: int) -> Item:
    if item_id not in items:
        raise HTTPException(
            status_code=404, detail=f"following item {item_id=} does not exist"
            )
    return items[item_id]

#helper dict for no_id items: This is a dictionary, where the key is a string and the value can be any of the types declared by the Union class. (list[Item] means it can be a list of Items)
selection_types = dict[str, Union[str, float, int, Category, list[Item], None]]

@app.get("/items/")
def get_item_no_id(name: Union[str, None] = None, 
                   price: Union[float, None] = None,
                   count: Union[int, None] = None,
                   category: Union[Category, None] = None) -> dict[str, selection_types]:
    def check_item(item: Item) -> bool:
        # the all() function return true if all statements are true
        return all(
            (
                name is None or item.name == name,
                price is None or item.price == price,
                count is None or item.count == count,
                category is None or item.category is category,
            )
        )
    # what happens here is 
    selection = [item for item in items.values() if check_item(item)]
    return {
        "query": {"name": name, "price": price, "count": count, "category": category, "selection": selection}
    }
# RUN: uvicorn name_of_file:app --reload ======== uvicorn fastAPI-test:app --reload