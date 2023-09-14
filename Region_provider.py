# code explanation always above and/or next to the code

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
        return region

# ________TO USE THE Region_provider CLASS________

# we create an instance of the Faker class, initializing the faker generator
fake = Faker()
# we then test the Region_provider class by creating an instance of it
fake.add_provider(Region_provider)

print(fake.region())