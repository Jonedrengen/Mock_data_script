# this file creates randomly generated data for the sample table

#using the faker module to generate more complex random data
from faker import Faker

#create instance of the Faker class, to make use of the faker generator
fake = Faker()

# will use the uuid module to generate unique ids for the sample table
class sample_id_generator():
    def create_uuid():
        fake_uuid = fake.uuid4(cast_to=None)
        return fake_uuid

#testing the sample_id_generator class
for _ in range(5):
    print(sample_id_generator.create_uuid())

#___NEXT CLASS__________________________________________________________________________________________________________
#___NEXT CLASS__________________________________________________________________________________________________________
#___NEXT CLASS__________________________________________________________________________________________________________

