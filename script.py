import os
import sys
from datetime import datetime
from pathlib import Path
from random import choice

import django
from django.conf import settings
from django.core.management import call_command

DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OF_OBJECTS = 1000

sys.path.append(str(DJANGO_BASE_DIR))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
settings.USE_TZ = False

django.setup()

if __name__ == '__main__':
    import faker

    from contact.models import Category, Contact

    call_command('migrate', verbosity=0)

    Contact.objects.all().delete()
    Category.objects.all().delete()

    fake = faker.Faker('pt_BR')
    categories = ['Amigos', 'Família', 'Conhecidos']

    django_categories = [Category(name=name) for name in categories]

    for category in django_categories:
        category.save()

    django_contacts = []

    for _ in range(NUMBER_OF_OBJECTS):
        profile = fake.profile()
        email = profile['mail']
        first_name, last_name = profile['name'].split(' ', 1)
        phone_number = fake.phone_number()
        created_date = datetime.combine(fake.date_this_year(), datetime.min.time())
        description = fake.text(max_nb_chars=100)
        category = choice(django_categories)

        django_contacts.append(
            Contact(
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number,
                email=email,
                created_date=created_date,
                description=description,
                category=category,
            )
        )

    if django_contacts:
        Contact.objects.bulk_create(django_contacts)

    print(f'Foram criados {len(django_contacts)} contatos com sucesso.')