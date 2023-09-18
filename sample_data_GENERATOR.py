# this file creates randomly generated data for the sample table

#using the faker module to generate more complex random data
from faker import Faker
from faker.providers import BaseProvider

#create instance of the Faker class, to make use of the faker generator
fake = Faker()

# will use the uuid module to generate unique ids for the sample table
class random_id_provider(BaseProvider):
    def create_uuid(self):
        fake_uuid = fake.uuid4(cast_to=None) #using cast_to=None will return a default uuid4() object as a string (which is the standard format for uuids)
        return fake_uuid

#creating an instance of the sample_id_generator class
sample_id = random_id_provider(fake)

#testing the sample_id_generator class
for _ in range(5):
    fake_sample_id = random_id_provider.create_uuid(self=sample_id)
    print(fake_sample_id)

#___Create cpr for the sample table__________________________________________________________________________________________________________
#___Create cpr for the sample table__________________________________________________________________________________________________________
#___Create cpr for the sample table__________________________________________________________________________________________________________

#using CPR_provider.py to generate CPR numbers for the sample table
from CPR_provider import CPR_provider

# creating an instance of the CPR_provider class
CPR_provider_instance = CPR_provider(fake)

#creating random CPR numbers for the sample table (not the same as the CPR numbers for the persons table)
def create_cpr():
    fake_cpr = CPR_provider_instance.cpr()
    return fake_cpr
    
for _ in range(5):
    fake_cpr = create_cpr()
    print(fake_cpr)

#___Create sample date__________________________________________________________________________________________________________
#___Create sample date__________________________________________________________________________________________________________
#___Create sample date__________________________________________________________________________________________________________

# creating a class, that generates a random date for when the sample was taken (from 3 years ago until today)
class random_date_provider(BaseProvider):
    def create_date(self, start_date="-3y", end_date="today"):
        return self.generator.date_between(start_date, end_date)

#create an instance of the sample_date_provider class
sample_instance = random_date_provider(fake)

for ele in range(5):
    fake_date = sample_instance.create_date()
    print(fake_date)

#___Create random host__________________________________________________________________________________________________________
#___Create random host__________________________________________________________________________________________________________
#___Create random host__________________________________________________________________________________________________________

class random_host_provider(BaseProvider):
    def create_host(self):
        fake_hosts = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        fake_host = self.random_element(fake_hosts)
        return "lab " + fake_host

#create an instance of the random_host_provider class
host_instance = random_host_provider(fake)

for ele in range(5):
    fake_ass_host = host_instance.create_host()
    print(fake_ass_host)
