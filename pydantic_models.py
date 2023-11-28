# for validation of data
from pydantic import BaseModel

#for specifying dates in the pydantic models
from datetime import date

#Pydantic models: used to define response and requests data in the API
#ORM models: used to directly interact with the database (querying)


#creating pydantic models. They are to validate the data received from the database
class Persons_Pyd_model(BaseModel):
    CPR: str
    Phone_number: str
    Region: str
    Gender: str

class Sample_Pyd_model(BaseModel):
    SampleID: str
    CPR: str
    SampleDate: date
    Host: str
    Ct: str

class Batch_Pyd_model(BaseModel):
    BatchID: str
    BatchDate: date
    Platform: str
    BatchSource: str

class COVID19_Pyd_model(BaseModel):
    CovidID: str
    Pango_designation: str
    WhoVariant: str
    QcScore: str

class Legionella_Pyd_model(BaseModel):
    LegionellaID: str
    Genotype: str
    Disease: str
    DiseasePhenotype: str
    DanishLocation: str
    ForeignLocation: str
    AcquiredFood: str

class SequencedSample_Pyd_model(BaseModel):
    SequencedSampleID: str
    SampleContent: str
    DateSequencing: str
    Quality: str
    Organism: str
    OrganismID: str
    SampleID: str
    BatchID: str

class S_aureus_Pyd_model(BaseModel):
    AreusID: str
    Genotype: str
    Disease: str
    DiseasePhenotype: str
    DanishLocation: str
    ForeignLocation: str
    AcquiredHospital: str
    AcquiredSurgery: str
    Infectionlocation: str

class S_epidermidis_Pyd_model(BaseModel):
    EpidermidesID: str
    Genotype: str
    Disease: str
    DiseasePhenotype: str
    DanishLocation: str
    ForeignLocation: str
    AcquiredHospital: str
    AcquiredSurgery: str
    Infectionlocation: str


#creating the API response model: Handles the automatic JSON conversion (when used in the API endpoint) as well as validating the data
class API_Response(BaseModel):
    persons: list[Persons_Pyd_model]
    samples: list[Sample_Pyd_model]
    batches: list[Batch_Pyd_model]
    covid19: list[COVID19_Pyd_model]
    legionella: list[Legionella_Pyd_model]
    sequencedsample: list[SequencedSample_Pyd_model]
    s_aureus: list[S_aureus_Pyd_model]
    s_epidermidis: list[S_epidermidis_Pyd_model]