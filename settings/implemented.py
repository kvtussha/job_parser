import os

from dotenv import load_dotenv

from src.hh import HeadHunterAPI
from src.superjob import SuperJobAPI

load_dotenv()
API_KEY = os.getenv('SECRET_API_KEY')

headers = {'Host': 'api.superjob.ru',
           'X-Api-App-Id': API_KEY,
           'Authorisation': f'Bearer {API_KEY[3:]}',
           'Content-Type': 'application/x-www-form-urlencoded'}

hh_all_vacancies = HeadHunterAPI().get_all_vacancies()
sj_all_vacancies = SuperJobAPI().get_all_vacancies()
