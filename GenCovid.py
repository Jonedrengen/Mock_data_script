# generating covidID
from faker import Faker
from faker.providers import BaseProvider
import random
from HelperFunctions import *

fake = Faker()

#Class for generating covidID, based on the OrganismID column in the SequencedSample_data.csv
class CovidIDProvider(BaseProvider):
    def covidID(self):
        fetched_IDs = Fetch_column_from_csv("SequencedSample_data.csv", "OrganismID")
        Covid_IDs = [ele for ele in fetched_IDs if ele.startswith("COVID-")] # get all covid IDs
        return Covid_IDs
fake.add_provider(CovidIDProvider)

#_______________________________________________________________________________

# generating pango_designation and who_variant
class PangoDesignation_WHO_Provider(BaseProvider):
    """
    Provides a method to generate a random Pango lineage designation and its corresponding WHO variant name.
    
    Methods:
    - pango_designation_and_WHOVariant: Returns a tuple with a Pango designation and its associated WHO variant.
    """
    def pango_designation_and_WHOVariant(self) -> tuple:
        """
        Generates and returns a random Pango lineage designation and its associated WHO variant name.
        
        Returns:
        - tuple: (Pango designation, WHO variant name)
        """
        variant_dict = {
            "B.1.1.7" : "Alpha",
            "B.1.617.2" : "Delta",
            "BA.1" : "Omicron"
        } 
        designation = random.choice(list(variant_dict)) 
        return designation, variant_dict[designation]
fake.add_provider(PangoDesignation_WHO_Provider)

#_______________________________________________________________________________

# generating QCscore

class QCscoreProvider(BaseProvider):
    def QCscore(self):
        return random.choice(["Mid", "High"])
fake.add_provider(QCscoreProvider)

#_______________________________________________________________________________

#generating csv (and tuple of data)

#generating csv file with covid data
import csv
from HelperFunctions import * # to get the column with organismIDs from SequencedSample_data.csv
# here we generate the tuple inside the function and write it to the csv file, because it dont fucking work otherwise


def generate_covid_data_csv(name = "Covid_data.csv"):
    
    Covid_IDs = fake.covidID()

    with open(name, 'w') as csvfile:
        writer = csv.writer(csvfile) #create writer object on csvfile
        writer.writerow(["CovidID", "Pango_designation", "WhoVariant", "QcScore"])
        for covid_id in Covid_IDs:
            pango_designation, who_variant = fake.pango_designation_and_WHOVariant() #pango_designation and who_variant are dependent on each other
            QCscore = fake.QCscore()
            data_tuple = (covid_id, pango_designation, who_variant, QCscore)
            writer.writerow(data_tuple)

    #print(f'{name} file generated successfully')

#generate_covid_data_csv()