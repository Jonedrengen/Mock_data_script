# code explanation always above and/or next to the code

# this script is a random (danish) phone number generator

# import random module
import random

class Phone_number:
    def number(self):
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