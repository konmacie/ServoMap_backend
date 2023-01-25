from faker import Faker
import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ServoMap.settings")

django.setup()

from apps.locations.models import Location, LocationType


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


def get_or_create_types():
    types = []
    for location_type in LOCATION_TYPES:
        type = LocationType.objects.get_or_create(**location_type)
        types.append(type[0])
    return types


if __name__ == "__main__":
    types = get_or_create_types()
    print(types)
