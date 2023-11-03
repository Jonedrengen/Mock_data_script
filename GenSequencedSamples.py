import csv
import random
from datetime import datetime, timedelta
from faker import Faker
from faker.providers import BaseProvider
from HelperFunctions import Fetch_column_from_csv

fake = Faker()

# Class to generate SequencedSampleID
class SequencedSampleProvider(BaseProvider):
    def seq_sample_id(self) -> str:
        rand_let = fake.random_letter().upper()
        rand_numbers = str(fake.random_number(digits=10)).zfill(10)
        return f'SequencedSampleID-{rand_let}{rand_numbers}'
        
fake.add_provider(SequencedSampleProvider)

# Class to generate SampleContent
class GenSampleContent(BaseProvider):
    def SampleContent(self):
        """Generates a sample content value. Currently supports only "RNA"."""
        return "RNA"
        
fake.add_provider(GenSampleContent)

# Class to generate SequenceDate based on BatchDate
class SequenceDate(BaseProvider):
    def gen_SeqDate(self):
        BatchDate = Fetch_column_from_csv("Batch_data.csv", "BatchDate")
        return random.choice(BatchDate)
        
fake.add_provider(SequenceDate)

# Class to generate Quality
class Quality(BaseProvider):
    def gen_Quality(self) -> str:
        return str(random.choice(["Fail", "LQ", "MQ", "HQ"]))
        
fake.add_provider(Quality)

# Class to generate Organism and OrganismID
class Org_and_OrgID(BaseProvider):
    organism_map = {
        "Covid" : "COVID",
        "Legionella" : "LEGIO",
        "S.Aureus" : "SAURE",
        "S.Epidermidis" : "SEPID"
    }

    def gen_Org_and_OrgID(self) -> tuple:
        # first we find a random organism
        organism = random.choice(list(self.organism_map.keys())) #getting the key of the dictionary and converting it to a list
        # then we find the corresponding organismID
        ID_name = self.organism_map[organism] #getting the value of the key

        Random_letters = "".join(fake.random_letters(length=5)).upper() #generating 5 random letters in upper case
        Random_numbers = str(fake.random_number(digits=5)).zfill(5) #generating 5 random numbers and filling them with zeros on the left side and converting them to string from int

        organismID = f'{ID_name}-{Random_letters}{Random_numbers}'
        return organism, organismID
fake.add_provider(Org_and_OrgID) # add the provider to our faker object

# Function to generate data for the SequencedSample.csv file

def GenSequencedSample() -> tuple:
    SequencedSampleID = fake.seq_sample_id()
    SampleContent = fake.SampleContent()
    SeqDate = fake.gen_SeqDate()
    Quality = fake.gen_Quality()
    Organism, OrganismID = fake.gen_Org_and_OrgID()
    data_tuple = (SequencedSampleID, SampleContent, SeqDate, Quality, Organism, OrganismID)
    return data_tuple

# Function to generate sequenced samples from the original dataset
def generate_SequencedSample_csv(sample_file, batch_file, name="SequencedSample.csv"):
    SampleIDS = Fetch_column_from_csv(sample_file, "SampleID")
    BatchIDS = Fetch_column_from_csv(batch_file, "BatchID")
    
    with open(name, "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["SequencedSampleID", "SampleContent", "DateSequencing", "Quality", "Organism", "OrganismID", "SampleID", "BatchID"])
        
        for sample_ID in SampleIDS:
            data_tuple = GenSequencedSample()
            writer.writerow(data_tuple + (sample_ID, random.choice(BatchIDS)))
            
    #print(f'{name} file generated successfully')

#generate_SequencedSample_csv("Sample_data.csv", "Batch.csv", "SequencedSample.csv")
