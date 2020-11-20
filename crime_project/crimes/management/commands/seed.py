from django.core.management.base import BaseCommand
from ...models import Departments
from django.contrib.auth.models import User
import requests

API_BASE = 'https://api.usa.gov/crime/fbi/sapi/api/agencies'
#AGENCIES_TO_SEED = 
API_KEY = 'C6RIHkoRhyeU6fS83UVm6FAQhDnelLOW0CHb3Ge0'
#https://api.usa.gov/crime/fbi/sapi/api/agencies?api_key=
class Command(BaseCommand):

    def handle(self, *args, **options):
        get_departments()
        seed_departments()
        # clear_all_beer_data()

        
def get_departments():

    response = requests.get(f'{API_BASE}?api_key={API_KEY}', headers={'Content-Type':      
    'application/json'})
    department_data = response.json()
    print(f'Fetched {len(department_data)} departments from {API_BASE}')
    return department_data 

def seed_departments():
    data = get_departments()
    for index, item in enumerate(data):
        for ori in data[item]:
            department = Departments(agency_name=data[item][ori]["agency_name"], state_name=data[item][ori]["state_name"], latitude = data[item][ori]["latitude"], longitude = data[item][ori]["longitude"])
            department.save()
    
#FAILING ON THIS ONE
#ERROR
#     return Database.Cursor.execute(self, query, params)
# django.db.utils.IntegrityError: NOT NULL constraint failed: crimes_departments.latitude
#     "DE0030300" : {
#       "ori" : "DE0030300",
#       "agency_name" : "Laurel Police Department",
#       "agency_type_name" : "City",
#       "state_name" : "Delaware",
#       "state_abbr" : "DE",
#       "division_name" : "South Atlantic",
#       "region_name" : "South",
#       "region_desc" : "Region III",
#       "county_name" : "SUSSEX",
#       "nibrs" : true,
#       "latitude" : 38.677511,
#       "longitude" : -75.335495,
#       "nibrs_start_date" : "01/01/2001"
#     },

            
        

