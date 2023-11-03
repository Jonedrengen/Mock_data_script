# code explanation always above and/or next to the code

# import the Faker class from the faker module
from faker import Faker 
# importing the BaseProvider class will enable us to create custom providers
from faker.providers import BaseProvider
# importing the random module will enable us to use the random.choice() method
import random
# for creating csv files
import csv

# creating instance of Faker class (so I can use the methods of the class)
fake = Faker()

#_______________________________________________________________________________
#_______________________________________________________________________________
#_______________________________________________________________________________

# CPR

# import the Faker class from the faker module
from faker import Faker 
# importing the BaseProvider class will enable us to create custom providers
from faker.providers import BaseProvider
# importing the random module will enable us to use the random.choice() method
import random

class CPR_provider(BaseProvider): # -> CPRprovider class inherits from BaseProvider, which is a class from the faker module, that enables us to create custom providers
    def cpr(self): # -> we create a method (function inside a class) called cpr() that takes in the self parameter.
        
        # creating a date of birth (dob) for the first 6 digits of the CPR number
        # tzinfo refers to the timezone information, which we don't need in this case
        # generator is a method from the faker module that generates random data, in this case a date of birth
        dob = self.generator.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=95).strftime("%d%m%y") # -> strftime() is a method from that formats the date of birth to the format we want, in this case dd/mm/yy

        # creating the last 4 digits of the CPR number, where the first represents the gender
        gender_digit = int
        
        # should be easy to read, but if not: if random.choice chooses True, then it will choose a random number from the list [0, 2, 4, 6, 8], else it will choose a random number from the list [1, 3, 5, 7, 9]
        if random.choice([True, False]) == True: 
            gender_digit = random.choice([0, 2, 4, 6, 8])
        else:
            gender_digit = random.choice([1, 3, 5, 7, 9])

        #then create the last 3 digits of the CPR number with the random.randint() method
        unique_digits = random.randint(100, 999)

        # then create the CPR by combining these 3 variables
        CPR_number = f"{dob}{unique_digits}{gender_digit}"
        
        # then I return the CPR number
        return str(CPR_number)
    
# ________TO USE THE CPRprovider CLASS________
# we create an instance of the Faker class, initializing the faker generator
# -> fake = Faker()

# we then test the CPRprovider class by creating an instance of it
# -> fake.add_provider(CPR_provider)

# we can print a single CPR number by calling the cpr() method
# -> print(fake.cpr())

# we can also print multiple CPR numbers by using a for loop
# -> for ele in range(10):
# ->     print(fake.cpr())


#_______________________________________________________________________________
#_______________________________________________________________________________
#_______________________________________________________________________________

# Gender

# import the Faker class from the faker module
from faker import Faker

# importing the BaseProvider class will enable us to create custom providers
class gender:
    # writing @staticmethod above the method, will make it a static method, which means that it can be called without creating an instance of the class
    # you call it by writing the class name, followed by a dot, and then the method name (see line 31 in Persons_data_GENERATOR.py)
    @staticmethod
    def gender_determination(CPR_number):
        # checks the 10'th digit of the CPR number, since that determines the gender of the person
        gender_digit = int(CPR_number[9])

     # this determines whether the gender digit is even or odd. If the 
        if gender_digit % 2 == 0:
            return "F"
        else:
            return "M"
        
# # ________TO USE THE gender CLASS________ 
# # IS DEPENDANT ON THE CPRprovider CLASS!

# # we create an instance of the Faker class, initializing the faker generator
# # -> fake = Faker()

# # we then test the CPR_provider class by creating an instance of it
# # cpr_provider_instance = CPR_provider(fake)

# # we can then call the gender_determination() method on the cpr_provider_instance
# # gender.gender_determination(cpr_provider_instance.cpr())


#_______________________________________________________________________________
#_______________________________________________________________________________
#_______________________________________________________________________________

# Phone number (danish Phone numbers only)

# import random module
import random

class Phone_number:
    @staticmethod
    def number():
        number = random.randint(10000000, 99999999)
        return str(number)
    
#________TO USE THE Phone_number CLASS________

#testing the class
# -> result = Phone_number()

# printing a single phone number
# -> print(result.number())

# printing multiple phone numbers
# -> for ele in range(10):
# ->    print(result.number())


#_______________________________________________________________________________
#_______________________________________________________________________________
#_______________________________________________________________________________

# Region

# import the Faker class from the faker module
from faker import Faker
# importing the BaseProvider class will enable us to create custom providers
from faker.providers import BaseProvider

class Region_provider(BaseProvider):
    def region(self):
        # creating the list of regions
        regions = ["Hovedstaden", "Sjælland", "Syddanmark", "Midtjylland", "Nordjylland"]
        # using the random_element() method to choose a random region from the list
        region = self.random_element(regions)
        return str(region)

# ________TO USE THE Region_provider CLASS________

# we create an instance of the Faker class, initializing the faker generator
# -> fake = Faker()

# we then test the Region_provider class by creating an instance of it
# -> fake.add_provider(Region_provider)

# we can print a single region by calling the region() method
# -> print(fake.region())