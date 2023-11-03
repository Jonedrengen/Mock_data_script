# this file creates randomly generated data for the sample table
import csv

#using the faker module to generate more complex random data
from faker import Faker
from faker.providers import BaseProvider
import random

fake = Faker()


# generating a random BatchID in format: Batch-xxxxxx
# 1 random uppercase letter, x random numbers

class BatchIDProvider(BaseProvider):
    def batch_id(self) -> str:
        rand_let = fake.random_letter().upper()
        rand_numbers = str(fake.random_number(digits=10)).zfill(10) #zfill() is a method that fills the string with zeros on the left side, until it reaches the specified length
        return f'Batch-{rand_let}{rand_numbers}'
fake.add_provider(BatchIDProvider)



# generating a Batchdate in format: yyyy-mm-dd
# should generate a list of 12 dates, 1 for each month of the year

#importing datetime, because I want to specify that It should only return a date that is the last day of the month
from datetime import datetime, timedelta

class BatchDateProvider(BaseProvider):
    def batch_date(self, size=36) -> list:
        # if there is no start year provided, it will default to 3 years ago from today
        current_date = datetime.now()
        dates = [(current_date - timedelta(days=30 * ele)).replace(day=1) for ele in range(size)]
        dates.sort()
        return [str(date.date()) for date in dates]    
fake.add_provider(BatchDateProvider)



# generating a random platform (only 1 for now, but created like this for future expansion)

class PlatformProvider(BaseProvider):
    def platform(self) -> str:
        platform = "Illumina"
        return platform

fake.add_provider(PlatformProvider)



# generating random batch source (only 3 for now, but created like this for future expansion)

class BatchSource(BaseProvider):
    def batch_source(self) -> str:
        source = random.choice(["Lab A", "Lab B", "Lab C"])
        return source
    

fake.add_provider(BatchSource)


#generating data
#generating data
#generating data


#creating a tuple of tuples, where each tuple represents a row in the table. Based on the generated dates from the BatchDateProvider class

def generate_batches(size=36) -> list: # -> the size parameter is optional, and will default to 36 if no size is provided
    batch_data = []
    for date in fake.batch_date(size):
        batch_data.append((fake.batch_id(), date, fake.platform(), fake.batch_source()))
    return batch_data



# writing the data to a csv file

def write_batches_to_csv(size=36) -> None:
    with open("Batch.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["BatchID", "BatchDate", "Platform", "BatchSource"])
        for row in generate_batches(size):
            writer.writerow(row)

#write_batches_to_csv(12)
