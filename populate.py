from faker import Faker
import django
import os
import decimal
import random
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ServoMap.settings")

django.setup()

from apps.locations.models import Location, LocationType

# 54.405392, 18.657749
# 54.318575, 18.470982
MIN_LATITUDE = 54.318575
MAX_LATITUDE = 54.405392
MIN_LONGITUDE = 18.470982
MAX_LONGITUDE = 18.657749
NUM_OF_LOCATIONS = 100

fake = Faker()

LOCATION_TYPES = [
    {
        "name": "Bookstore",
        "icon": "fa-solid fa-book"
    },
    {
        "name": "Mechanic",
        "icon": "fa-solid fa-car"
    },
    {
        "name": "Cafe",
        "icon": "fa-solid fa-mug-hot"
    },
    {
        "name": "Fastfood",
        "icon": "fa-solid fa-burger"
    },
    {
        "name": "Bakery",
        "icon": "fa-solid fa-plate-wheat"
    },
    {
        "name": "Restaurant",
        "icon": "fa-solid fa-utensils"
    },
    {
        "name": "Grocery",
        "icon": "fa-solid fa-carrot"
    },
    {
        "name": "Bar",
        "icon": "fa-solid fa-martini-glass-citrus"
    },
    {
        "name": "Florist",
        "icon": "fa-solid fa-fan"
    },
    {
        "name": "Pharmacist",
        "icon": "fa-solid fa-prescription-bottle-medical"
    },
]


def random_longitude():
    longitude = random.uniform(MIN_LONGITUDE, MAX_LONGITUDE)
    return decimal.Decimal(longitude)


def random_latitude():
    latitude = random.uniform(MIN_LATITUDE, MAX_LATITUDE)
    return decimal.Decimal(latitude)


def get_or_create_types():
    types = []
    for location_type in LOCATION_TYPES:
        type = LocationType.objects.get_or_create(**location_type)
        types.append(type[0])
    return types


if __name__ == "__main__":
    types = get_or_create_types()
    for i in range(NUM_OF_LOCATIONS):
        location = Location.objects.create(
            name=fake.company(),
            type=random.choice(types),
            latitude=random_latitude(),
            longitude=random_longitude(),
            address=fake.street_address(),
            city="Gdańsk",
            postal_code=fake.postcode(),
        )
        print(location.name)
