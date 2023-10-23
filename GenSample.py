# this file creates randomly generated data for the sample table
import csv

#using the faker module to generate more complex random data
from faker import Faker
from faker.providers import BaseProvider

#using CPR_provider.py to generate CPR numbers for the sample table
from GenPersons import CPR_provider

#create instance of the Faker class, to make use of the faker generator
fake = Faker()

#___Create SampleID for the sample table__________________________________________________________________________________________________________
#___Create SampleID for the sample table__________________________________________________________________________________________________________
#___Create SampleID for the sample table__________________________________________________________________________________________________________


# will use the uuid4() method from the faker library to generate random uuids
class random_id_provider(BaseProvider):
    def create_uuid(self):
        #using cast_to=None will return a default uuid4() object as a string (which is the standard format for uuids)
        fake_uuid = fake.uuid4(cast_to=None)
        return fake_uuid

#___Create cpr for the sample table__________________________________________________________________________________________________________
#___Create cpr for the sample table__________________________________________________________________________________________________________
#___Create cpr for the sample table__________________________________________________________________________________________________________

# will be reusing the method from the CPR_provider() class

#___Create sample date__________________________________________________________________________________________________________
#___Create sample date__________________________________________________________________________________________________________
#___Create sample date__________________________________________________________________________________________________________

# creating a class, that generates a random date for when the sample was taken (from 3 years ago until today)
class random_date_provider(BaseProvider):
    #self refers to the instance of this class (random_date_provider) and since it inherits from the BaseProvider class, it can use the faker generator
    # 3 arguments, self, start_date, end_date, where start_date and end_date are optional, since they have default values
    def create_date(self, start_date="-3y", end_date="today"):
        # self refers to random_date_provider, which inherits from the BaseProvider class, which has a generator attribute
        # the generator attribute is an instance of the Generator class, which has a date_between method
        return self.generator.date_between(start_date, end_date)



#___Create random host__________________________________________________________________________________________________________
#___Create random host__________________________________________________________________________________________________________
#___Create random host__________________________________________________________________________________________________________

class random_host_provider(BaseProvider):
    #self refers to the instance of this class (random_host_provider)
    def create_host(self):
        # written like this to make human 70%, Mink 20% and Cow 10%
        fake_hosts = ["Human", "Human", "Human", "Human", "Human", "Human", "Human", "Mink", "Mink", "Cow"]
        # the random_element method picks any random value from a list, or any other iterable (tuple, set, etc..)
        fake_host = self.random_element(fake_hosts)
        return fake_host


#___Create random Ct value__________________________________________________________________________________________________________
#___Create random Ct value__________________________________________________________________________________________________________
#___Create random Ct value__________________________________________________________________________________________________________

# creating the random_Ct_value_provider class. 
# It inherits from the faker librarys BaseProvider class.
class random_Ct_value_provider(BaseProvider):
    # self refers to the instance of this class (random_Ct_value_provider)
    def create_Ct_val(self):
        #list of fake Cts
        fake_Cts = ["27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40"]
        # the random_element method picks any random value from a list, or any other iterable (tuple, set, etc..)
        fake_Ct = self.random_element(fake_Cts)
        return fake_Ct


#___creating the fake data__________________________________________________________________________________________________________
#___creating the fake data__________________________________________________________________________________________________________
#___creating the fake data__________________________________________________________________________________________________________

# creating an instance of the sample_id_generator class, using the fake instance of the Faker class
# the fake argument is used to allow my instance of the sample_id_generator class to use the faker generator
sample_id_instance = random_id_provider(fake)
# repeat for all others
random_date_instance = random_date_provider(fake)
host_instance = random_host_provider(fake)
Ct_instance = random_Ct_value_provider(fake)
# This instance is created from the CPR_provider class (reused from creating the Persons table data). This means you can't find the class in this file
CPR_provider_instance = CPR_provider(fake)

def Sample_data_GENERATOR():
    random_uuid = sample_id_instance.create_uuid()
    random_date = random_date_instance.create_date()
    random_host = host_instance.create_host()
    random_Ct = Ct_instance.create_Ct_val()
    random_CPR = CPR_provider_instance.cpr()

    #creating a tuple to store the data, in the correct order matching the database
    Sample_tuple = (random_CPR, random_uuid, random_date, random_host, random_Ct)
    return Sample_tuple

#___creating the Sample_data.csv__________________________________________________________________________________________________________
#___creating the Sample_date.csv__________________________________________________________________________________________________________
#___creating the Sample_date.csv__________________________________________________________________________________________________________

def create_csv_file():
    #to create a csv file, we need to open the file in write mode
    with open("Sample.csv", "w", newline="") as csvfile:
        #to create a csv file, we need to create a writer object
        writer = csv.writer(csvfile)
        # we then need to write the header row
        writer.writerow(["CPR", "SampleID", "SampleDate", "Host", "Ct"])
        # we then create 200 rows of data
        for ele in range(200):
            # we then call the Sample_data_GENERATOR() function to create the data
            row_data = Sample_data_GENERATOR()
            #then we write the data to the csv file
            writer.writerow(row_data)

# calling the function to creating the csv file!
create_csv_file()
