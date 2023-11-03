#importing libraries
from faker import Faker
from faker.providers import BaseProvider
import csv
import random
from HelperFunctions import Fetch_column_from_csv

#creating fake instance
fake = Faker()

# Docstring for Legionella data generation

#_____________________________________________

#LegionellaID column
class LegionellaID_Provider(BaseProvider):
    def LegionellaID(self) -> list:
        fetched_IDs = Fetch_column_from_csv("SequencedSample_data.csv", "OrganismID")
        Legionella_IDs = [ele for ele in fetched_IDs if ele.startswith("LEGIO-")] # get all Legionella IDs
        return Legionella_IDs
fake.add_provider(LegionellaID_Provider)

#_____________________________________________

#Genotype column
class LegioGenoType_Provider(BaseProvider):
    def gen_LegioGenoType(self) -> str:
        Genotypes = ["La", "Lb", "Lb"]
        return random.choice(Genotypes)
fake.add_provider(LegioGenoType_Provider)

#_____________________________________________

# Disease column

class LegioDisease_Provider(BaseProvider):
    def gen_LegioDisease(self) -> str:
        Disease = ["Y", "N"]
        return random.choice(Disease)
fake.add_provider(LegioDisease_Provider)

#_____________________________________________

# Disease Phenotype column

class LegioPhenotype_Provider(BaseProvider):
    def gen_LegioPhenotype(self) -> str:
        Phenotype = ["Pneumonia", "Cough, fever", "Cough", "NULL"]
        return random.choice(Phenotype)
fake.add_provider(LegioPhenotype_Provider)

#_____________________________________________

# Location (Foreign or danish)

class LegioLocation_Provider(BaseProvider):
    def gen_LegioLocation(self):
        danish_location = random.choice(["Sjælland", "Jylland", "Fyn", "NULL"])
        if danish_location == "NULL":
            foreign_location = "Greece"
        else:
            foreign_location = "NULL"
        return danish_location, foreign_location
fake.add_provider(LegioLocation_Provider)

#_____________________________________________

# Aquired food class (aquired from this type of consumable)

class LegioFood_Provider(BaseProvider):
    def gen_LegioFood(self) -> str:
        food_type = random.choice(["Water", "Beef"])
        return food_type
fake.add_provider(LegioFood_Provider)

#_____________________________________________

# function to create csvfile (tuple created inside)

def create_Legio_csv(name="Legionella_data.csv"):

    # getting the Legionella ids
    LegioIDs = fake.LegionellaID()

    with open(name, "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["LegionellaID", "Genotype", "Disease", "DiseasePhenotype", "DanishLocation", "ForeignLocation", "AcquiredFood"])
        for LegioID in LegioIDs:
            Genotype = fake.gen_LegioGenoType()
            Disease = fake.gen_LegioDisease()
            DiseasePhenotype = fake.gen_LegioPhenotype()
            danish_location, foreign_location = fake.gen_LegioLocation()
            AcquiredFood = fake.gen_LegioFood()
            data_tuple = (LegioID, Genotype, Disease, DiseasePhenotype, danish_location, foreign_location, AcquiredFood)
            writer.writerow(data_tuple)
    #print("file gen succes")
#create_Legio_csv()
