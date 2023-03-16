from faker import Faker
import django
import os
import decimal
import random
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ServoMap.settings")

django.setup()

from django.contrib.auth import get_user_model
from apps.locations.models import Location, LocationType, Review


# 54.405392, 18.657749
# 54.318575, 18.470982
MIN_LATITUDE = 53.9
MAX_LATITUDE = 54.3999999
MIN_LONGITUDE = 17.60
MAX_LONGITUDE = 18.599999
NUM_OF_LOCATIONS = 2000


USERS_NUM = 20

REVIEW_COUNT_PER_USER = 400
REVIEW_MAX_LOCATION_ID = 2000
REVIEW_MAX_LENGTH = 500
REVIEW_MIN_RATING = 1
REVIEW_MAX_RATING = 5


fake = Faker()
UserModel = get_user_model()

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


def create_user():
    user_data = {
        'username': fake.user_name(),
        'email': fake.email(),
        'password': fake.password(),
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
    }
    return UserModel.objects.create_user(**user_data)


def create_review(location, user):
    text = fake.text(max_nb_chars=REVIEW_MAX_LENGTH)
    rating = random.randint(REVIEW_MIN_RATING, REVIEW_MAX_RATING)
    return Review.objects.create(
        text=text,
        rating=rating,
        location=location,
        user=user,
    )


def create_reviews(user):
    locations = random.sample(
        range(REVIEW_MAX_LOCATION_ID), 
        REVIEW_COUNT_PER_USER
    )
    for j in range(REVIEW_COUNT_PER_USER):
        try:
            location = Location.objects.get(id=locations[j])
            review = create_review(location=location, user=user)
            print(review)
        except Location.DoesNotExist:
            pass


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

    
    for i in range(USERS_NUM):
        user = create_user()
        print(user)
        create_reviews(user)
