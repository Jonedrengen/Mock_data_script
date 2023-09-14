# code explanation always above and/or next to the code

# import the Faker class from the faker module
from faker import Faker 
# importing the BaseProvider class will enable us to create custom providers
from faker.providers import BaseProvider
# importing the random module will enable us to use the random.choice() method
import random

# the first task is to create a random CPR number generator

# we create a new class that inherits from the BaseProvider class
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

        # I then create the CPR by combining these 3 variables
        CPR_number = f"{dob}{gender_digit}{unique_digits}"
        
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

#testing the class
fake = Faker()
fake.add_provider(CPR_provider)

print(fake.cpr())