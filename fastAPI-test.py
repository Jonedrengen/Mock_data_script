# Import Union from the typing module to allow for type hints that can accept multiple types (basically a parameter can be multiple datatypes, when passing)
from typing import Union

from fastapi import FastAPI

app = FastAPI()

# defining route for root endpoint
# When a get request is made for the root ("/"), the read_root function will be called
@app.get("/")
def read_root():
    # return a dict, that when returned by fastAPI, is converted to a JSON response
    # this is the respone that will be sent back to the client
    return {"Hello": "World"}


@app.get("/items/{item_id}")
# creating a function that takes 2 parameters, where the query "q" can be both str and None, it is set to default None
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "qes": q}

# RUN: uvicorn name_of_file:app --reload == uvicorn fastAPI-test:app --reload