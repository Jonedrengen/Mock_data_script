from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR, VARCHAR
from sqlalchemy.orm import sessionmaker

#importing Base and mappings from ORMmodels.py
from ORMmodels import Base, Persons, Sample

#db stuff to connect with
server = "localhost"
database = "mydb"
username = "sa"
password = r'N\VHs8*DJV' # bad practice - but only for testing
driver = "/opt/homebrew/lib/libmsodbcsql.18.dylib" # direct location, because for some reason the standard does not work for me
connection_string = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}&TrustServerCertificate=yes"

#Creating the engine, that needs the DB specifications. It uses the connections string to determine the spcifics of the DB (such as db type, like mssql, SQLServer or whatever)
# the create_engine function is a factory method. Essentially it means that it is a OOP method that return an object, without specifying the exact class of the object
engine = create_engine(connection_string)

# Base: acts as a template for the table. It keeps track of all classes that represent the tables in the db
# metadata has all the information about these tables. (has all the blueprints)
# create_all() looks through the collection of data in metadata and builds any table that is missing (it uses the blueprints)
# the bind=engine just tells the builder "create_all()" which db to build the tables in
Base.metadata.create_all(bind=engine)

#creating a session. A temporary database workspace, where I can interact with the database
# autocommit=False: do not commit changes unless i tell you to
# autoflush=False: do not update my db when i modify my objects, unless i use session.flush()
# bind=engine: connect to engine db
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# functions for getting data from the db
def get_all_Persons():
    #giving SessionLocal() temp name session
    with SessionLocal() as session: 
        # session.query(Persons): tells SQLAlchemy to prepare a query that will select records from the DB, matching the Persons class
        # all(): return all the results
        return session.query(Persons).all()


def get_all_Sample():
    with SessionLocal() as session:
        return session.query(Sample).all()

