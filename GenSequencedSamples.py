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
        BatchDate = Fetch_column_from_csv("Batch.csv", "BatchDate")
        return random.choice(BatchDate)
        
fake.add_provider(SequenceDate)

# Class to generate Quality
class Quality(BaseProvider):
    def gen_Quality(self) -> str:
        return str(random.choice(["Fail", "LQ", "MQ", "HQ"]))
        
fake.add_provider(Quality)

# Class to generate Organism
class Organism(BaseProvider):
    def gen_Organism(self) -> str:
        return str(random.choice(["Covid", "Legionella", "S.Aureus", "S.Epidermidis"]))
        
fake.add_provider(Organism)

# Class to generate OrganismID
class OrganismID(BaseProvider):
    def gen_OrganismID(self) -> str:
        choice_prefix = random.choice(["COVID", "LEGIO", "SAURE", "SEPID"])
        random_letters = "".join(fake.random_letters(length=5)).upper()
        random_numbers = str(fake.random_number(digits=5)).zfill(5)
        return f'{choice_prefix}-{random_letters}{random_numbers}'
        
fake.add_provider(OrganismID)

# Function to generate data for the SequencedSample.csv file
def GenSequencedSample() -> tuple:
    return (
        fake.seq_sample_id(),
        fake.SampleContent(),
        fake.gen_SeqDate(),
        fake.gen_Quality(),
        fake.gen_Organism(),
        fake.gen_OrganismID()
    )

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
            
    print(f'{name} file generated successfully')

#generate_SequencedSample_csv("Sample_data.csv", "Batch.csv", "SequencedSample.csv")
