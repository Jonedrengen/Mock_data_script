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

