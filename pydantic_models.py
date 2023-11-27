# for validation of data
from pydantic import BaseModel

#creating pydantic model for persons data
class Persons_data(BaseModel):
    CPR: str
    Phone_number: str
    Region: str
    Gender: str