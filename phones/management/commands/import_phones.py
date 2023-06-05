import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
        i = 0
        for phone in phones:
            # TODO: Добавьте сохранение модели
            if i != 0:
                import_phones = Phone(
                    name=phone['name'],
                    price=phone['price'],
                    image=phone['image'],
                    release_date=phone['release_date'],
                    lte_exists=phone['lte_exists'],
                # slug=phone['slug']
            )
                import_phones.save()
            i += 1
            pass
