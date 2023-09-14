# code explanation always above and/or next to the code

#importing random module
import random

#using the CPR_provider class to determine the gender
from CPR_provider import CPR_provider

def determine_gender(CPR_number):
    # checks the 7'th digit of the CPR number, since that determines the gender of the person
    gender_digit = int(CPR_number[6])

    if gender_digit % 2 == 0:
        return "M"
    else:
        return "F"
    
#________