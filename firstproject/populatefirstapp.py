import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','firstproject.settings')


import django
django.setup()


# Fake pop script
import random
from firstapp.models import AccessRecord,Webpage,Topic
from faker import Faker


fakegen=Faker()
topics = ['Search','Social','Marketplace','Games']

def add_topics():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    # returning a topic object
    return t

def populate(N=5):
    for entry in range(N):
        # get the topic for entry
        top=add_topics()

        # create fake data for that entry
        fake_url=fakegen.url()
        fake_date=fakegen.date()
        fake_name=fakegen.company()

        """
        If it is a foreign key then you need to pass an entire object rather than just passing the string.
        """

        # create a new webpage entry
        webpg=Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        # Create a fake access record for that webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]


if __name__=="__main__":
    print("Populating Scripts...")
    populate(20)
    print("Populating Complete.....")