#importing libraries
from faker import Faker
from faker.providers import BaseProvider
import csv
import random
from HelperFunctions import Fetch_column_from_csv

#creating fake instance
fake = Faker()

# Docstring for Saureus data generation

#_____________________________________________

#SaureusID column
class SaureusID_Provider(BaseProvider):
    def SaureusID(self) -> list:
        fetched_IDs = Fetch_column_from_csv("SequencedSample_data.csv", "OrganismID")
        Saureus_IDs = [ele for ele in fetched_IDs if ele.startswith("SAURE-")] # get all Saureus IDs
        return Saureus_IDs
fake.add_provider(SaureusID_Provider)

#_____________________________________________

#Genotype column
class SaureGenoType_Provider(BaseProvider):
    def gen_SaureGenoType(self) -> str:
        Genotypes = ["Aa", "Ab", "Ac"]
        return random.choice(Genotypes)
fake.add_provider(SaureGenoType_Provider)

#_____________________________________________

# Disease column

class SaureDisease_Provider(BaseProvider):
    def gen_SaureDisease(self) -> str:
        Disease = ["Y", "N"]
        return random.choice(Disease)
fake.add_provider(SaureDisease_Provider)

#_____________________________________________

# Disease Phenotype column

class SaurePhenotype_Provider(BaseProvider):
    def gen_SaurePhenotype(self) -> str:
        Phenotype = ["Boils", "Osteomyelitis", "NULL"]
        return random.choice(Phenotype)
fake.add_provider(SaurePhenotype_Provider)

#_____________________________________________

# Location (Foreign or danish)

class SaureLocation_Provider(BaseProvider):
    def gen_SaureLocation(self):
        danish_location = random.choice(["Sjælland", "Jylland", "Fyn", "NULL"])
        if danish_location == "NULL":
            foreign_location = "Sweden"
        else:
            foreign_location = "NULL"
        return danish_location, foreign_location
fake.add_provider(SaureLocation_Provider)

#_____________________________________________

# Aquired hospital class 

class AquiredHospital_Provider(BaseProvider):
    def gen_hospital(self) -> str:
        hospital = random.choice(["HosA", "HosB", "ForeignHos"])
        return hospital
fake.add_provider(AquiredHospital_Provider)

#_____________________________________________

# Aquired surgery class 

class AquiredSurgery_Provider(BaseProvider):
    def gen_surgery(self) -> str:
        surgery = random.choice(["Y", "N"])
        return surgery
fake.add_provider(AquiredSurgery_Provider)

#_____________________________________________

# infection location class

class InfectionLocation_Provider(BaseProvider):
    def gen_infection(self) -> str:
        infection = random.choice(["Skin", "Bones"])
        return infection
fake.add_provider(InfectionLocation_Provider)

#_____________________________________________

# function to create csvfile (tuple created inside)

def create_Saureus_csv(name="Saureus_data.csv"):

    # getting the Saureus ids
    SaureusIDs = fake.SaureusID()

    with open(name, "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["AreusID", "Genotype", "Disease", "DiseasePhenotype", "DanishLocation", "ForeignLocation", "AcquiredHospital", "AcquiredSurgery", "Infectionlocation"])
        for SaureusID in SaureusIDs:
            Genotype = fake.gen_SaureGenoType()
            Disease = fake.gen_SaureDisease()
            DiseasePhenotype = fake.gen_SaurePhenotype()
            danish_location, foreign_location = fake.gen_SaureLocation()
            AcquiredHospital = fake.gen_hospital()
            AcquiredSurgery = fake.gen_surgery()
            Infectionlocation = fake.gen_infection()
            data_tuple = (SaureusID, Genotype, Disease, DiseasePhenotype, danish_location, foreign_location, AcquiredHospital, AcquiredSurgery, Infectionlocation)
            writer.writerow(data_tuple)
    #print("file gen succes")
#create_Legio_csv()
