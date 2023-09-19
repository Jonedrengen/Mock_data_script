# creating a tuple of data, containing a cpr-number, a gender based on the cpr-number, a region, and a phone number

#importing the classes from the providers
from CPR_provider import CPR_provider
from Gender_provider import gender
from Region_provider import Region_provider
from PhoneNumber_provider import Phone_number

#importing the random module and csv module
import csv
import random

# importing the Faker class from the faker module
from faker import Faker
# importing the BaseProvider class will enable us to create custom providers
from faker.providers import BaseProvider

#creating an instance of the Faker class
fake = Faker()

#creating instances of the classes, so I can use the methods from the classes
CPR_provider_instance = CPR_provider(fake)
Gender_provider_instance = gender()
Region_provider_instance = Region_provider(fake)
PhoneNumber_provider_instance = Phone_number()


def Persons_data_GENERATOR():
    # Generating random data for the persons table
    cpr_number = CPR_provider_instance.cpr()
    Gender = Gender_provider_instance.gender_determination(cpr_number) # <- determines gender based on the cpr number (7th number)
    Region = Region_provider_instance.region()
    Phone_number = PhoneNumber_provider_instance.number()

    #generating a tuple of data
    Persons_tuple = (cpr_number, Gender, Region, Phone_number)
    return Persons_tuple

def create_csv_file():
    #to create a csv file, we need to open the file in write mode
    with open("Persons_data.csv", "w", newline="") as csvfile:
        #to create a csv file, we need to create a writer object
        writer = csv.writer(csvfile)
        # we then need to write the header row
        writer.writerow(["CPR", "Gender", "Region", "Phone_number"])
        # we then create 200 rows of data
        for ele in range(200):
            # we then call the Persons_data_GENERATOR() function to generate the data
            row_data = Persons_data_GENERATOR()
            #then we write the data to the csv file
            writer.writerow(row_data)

# Call the create csv function to create the csv file
create_csv_file()

# #testing the Persons_data_GENERATOR() function
# for ele in range(10):
#     print(Persons_data_GENERATOR())

