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

#SepidID column
class SepidID_Provider(BaseProvider):
    def SepidID(self) -> list:
        fetched_IDs = Fetch_column_from_csv("SequencedSample_data.csv", "OrganismID")
        Sepid_IDs = [ele for ele in fetched_IDs if ele.startswith("SEPID-")] # get all S. Epidermidis IDs
        return Sepid_IDs
fake.add_provider(SepidID_Provider)

#_____________________________________________

#Genotype column
class SepidGenoType_Provider(BaseProvider):
    def gen_SepidGenoType(self) -> str:
        Genotypes = ["Ea", "Eb", "Ec"]
        return random.choice(Genotypes)
fake.add_provider(SepidGenoType_Provider)

#_____________________________________________

# Disease column

class SepidDisease_Provider(BaseProvider):
    def gen_SepidDisease(self) -> str:
        Disease = ["Y", "N"]
        return random.choice(Disease)
fake.add_provider(SepidDisease_Provider)

#_____________________________________________

# Disease Phenotype column

class SepidPhenotype_Provider(BaseProvider):
    def gen_SepidPhenotype(self) -> str:
        Phenotype = ["EyeInfection", "Bones", "NULL"]
        return random.choice(Phenotype)
fake.add_provider(SepidPhenotype_Provider)

#_____________________________________________

# Location (Foreign or danish)

class SepidLocation_Provider(BaseProvider):
    def gen_SepidLocation(self):
        danish_location = random.choice(["Sjælland", "Jylland", "Fyn", "NULL"])
        if danish_location == "NULL":
            foreign_location = "Sweden"
        else:
            foreign_location = "NULL"
        return danish_location, foreign_location
fake.add_provider(SepidLocation_Provider)

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
        infection = random.choice(["Eye", "Bones"])
        return infection
fake.add_provider(InfectionLocation_Provider)

#_____________________________________________

# function to create csvfile (tuple created inside)

def create_SEpidermidis_csv(name="Epidermidis_data.csv"):

    # getting the Saureus ids
    SepidIDs = fake.SepidID()

    with open(name, "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["EpidermidisID", "Genotype", "Disease", "DiseasePhenotype", "DanishLocation", "ForeignLocation", "AcquiredHospital", "AcquiredSurgery", "Infectionlocation"])
        for SepidID in SepidIDs:
            Genotype = fake.gen_SepidGenoType()
            Disease = fake.gen_SepidDisease()
            DiseasePhenotype = fake.gen_SepidPhenotype()
            danish_location, foreign_location = fake.gen_SepidLocation()
            AcquiredHospital = fake.gen_hospital()
            AcquiredSurgery = fake.gen_surgery()
            Infectionlocation = fake.gen_infection()
            data_tuple = (SepidID, Genotype, Disease, DiseasePhenotype, danish_location, foreign_location, AcquiredHospital, AcquiredSurgery, Infectionlocation)
            writer.writerow(data_tuple)
    #print("file gen succes")
#create_Legio_csv()
