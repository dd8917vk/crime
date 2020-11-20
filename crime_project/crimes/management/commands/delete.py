from django.core.management.base import BaseCommand
from ...models import Departments


class Command(BaseCommand):

    def handle(self, *args, **options):
        clear_all_department_data()

def clear_all_department_data():
    try:
        Departments.objects.all().delete()
        print('Deleted all department data.')
    except:
        print('Could not delete all department data.')

    