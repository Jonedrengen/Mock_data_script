from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR, NVARCHAR, Date
from sqlalchemy.ext.declarative import declarative_base
#creating a Base class for declerative class definitions. 
#this Base class will serve as a foundation for all ORM mappings to database tables.
#it allows us to define classes in a way that SQLAlchemy can interpret and translate into database tables.
Base = declarative_base() 

# defining a class that inherits from Base (the class will function in a way SQLalchemy understands)
# The class is a mapping of the table in the db (ORM concept)
class Persons(Base):
    __tablename__ = "Persons" #name of table the class maps to
    __table_args__ = {'schema': 'QC'} #name of Schema

    # the actual "map": Defining the columns of the table
    CPR = Column("CPR", NVARCHAR(10), primary_key=True)
    Phone_number = Column("Phone_number", NVARCHAR(50))
    Region = Column("Region", NVARCHAR(50), nullable=True)
    Gender = Column("Gender", CHAR(1))
    
    # contructer of the person class
    # it initializes a new instance of the Persons class, with specific values for the attributes (attributes match columns in table)
    # When creating a new instance of a class, you have to add the values specified in the constructer
    # so new_class_instance = Person(CPR="xxxx", Phone_number="xxxx", and so on)
    def __init__(self, CPR, Phone_number, Region, Gender):
        self.CPR = CPR
        self.Phone_number = Phone_number
        self.Region = Region
        self.Gender = Gender

    # just a specification on how it should print a person
    def __repr__(self): #function that allows us to specify how we would like to print a person
        return f"({self.CPR}) {self.Phone_number} {self.Region} {self.Gender}"
    

# Repeat of Persons class
class Sample(Base): #inherits from Base class
    __tablename__ = "Sample"
    __table_args__ = {'schema': 'QC'}

    SampleID = Column("SampleID", NVARCHAR(50), primary_key=True)
    CPR = Column("CPR", NVARCHAR(20), nullable=True)
    SampleDate = Column("SampleDate", Date)
    Host = Column("Host", NVARCHAR(50), nullable=True)
    Ct = Column("Ct", NVARCHAR(50), nullable=True)

    def __init__(self, SampleID, CPR, SampleDate, Host, Ct): #self references its own class (so Sample class)
        self.SampleID = SampleID
        self.CPR = CPR
        self.SampleDate = SampleDate
        self.Host = Host
        self.Ct = Ct

    def __repr__(self):
        return f"{self.SampleID}, {self.CPR}, {self.SampleDate}, {self.Host}, {self.Ct}"

