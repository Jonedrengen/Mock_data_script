import pyodbc

# Import Union from the typing module to allow for type hints that can accept multiple types (basically a parameter can be multiple datatypes, when passing)
from typing import Union

# for creating the api and handling HTTPExceptions
from fastapi import FastAPI, HTTPException

# for validation of data
from pydantic import BaseModel

# importing the db engine created with SQLAlchemy
from database_SQLAlchemy_calls import engine, get_all_Batch, get_all_COVID19, get_all_Legionella, get_all_Persons, get_all_S_aureus, get_all_S_epidermidis, get_all_Sample, get_all_SequencedSample
from sqlalchemy.orm import Session

#creating an intance, where I will be connection all the routes to 
app = FastAPI()
# RUN: uvicorn name_of_file:app --reload ======== uvicorn fastAPI-main:app --reload

# ERROR WHEN RUNNING UVICORN: when running it normally "uvicorn fastAPI-main:app --reload" an error arises, likely because a wring environment is used to receive packages
# the solution I came up with wah to specify the path to the environment before starting the program "/Users/jonsztukslotved/anaconda3/envs/env/bin/python -m uvicorn fastAPI-main:app --reload"
# I must say that I am unsure if this is a sustainable solution for future iterations


#this might be redundant, since I call functions, where the db already is specified
def get_db():
    #creating a new session, which is bound to the engine imported from another file (engine=db connection)
    db = Session(bind=engine)
    try:
        yield db
    except Exception as e:
        print(f'an error occurred {e}')
        raise HTTPException(status_code=500, detail='Database connection error')
    finally:
        # no matter if the try block or except block runs, the db will be closed for ressource management
        db.close()


#I decide to use split sessions here because of its simplicity
#using a single session might be better for data integrity (ask GPT if you dont understand)
@app.get("/fakedata", response_model=None)
def read_data() -> dict:
    Person_data = get_all_Persons()
    Batch_data = get_all_Batch()
    Sample_data = get_all_Sample()
    Covid_data = get_all_COVID19()
    Legio_data = get_all_Legionella()
    Areus_data = get_all_S_aureus()
    Epider_data = get_all_S_epidermidis()
    Sequence_data = get_all_SequencedSample()
    return {'persons' : Person_data, 'batch' : Batch_data, 'sample' : Sample_data, 'covid' : Covid_data,
            'legio' : Legio_data, 'areus' : Areus_data, 'epidermidis' : Epider_data, 'sequence' : Sequence_data}

#result = read_data()
#print(type(result)) -> dict