# code explanation always above and/or next to the code

# import the Faker class from the faker module
from faker import Faker

# importing the BaseProvider class will enable us to create custom providers
from faker.providers import BaseProvider

#using the CPR_provider class to determine the gender, since it already has a number that refers to the gender
from CPR_provider import CPR_provider

class gender:
    @staticmethod
    def gender_determination(CPR_number):
        # checks the 7'th digit of the CPR number, since that determines the gender of the person
        gender_digit = int(CPR_number[9])

     # this determines whether the gender digit is even or odd. If the 
        if gender_digit % 2 == 0:
            return "F"
        else:
            return "M"




#calling the class to test the method
#result = gender.gender_determination(cpr_provider_instance.cpr())
#print(result)


# # ________TO USE THE gender CLASS________

# # we create an instance of the Faker class, initializing the faker generator
# # -> fake = Faker()

# # we then test the CPR_provider class by creating an instance of it
# # cpr_provider_instance = CPR_provider(fake)

# # we can then call the gender_determination() method on the cpr_provider_instance
# # gender.gender_determination(cpr_provider_instance.cpr())