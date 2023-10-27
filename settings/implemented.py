import os

from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('SECRET_API_KEY')

headers = {'Host': 'api.superjob.ru',
           'X-Api-App-Id': api_key,
           'Authorisation': f'Bearer {api_key[3:]}',
           'Content-Type': 'application/x-www-form-urlencoded'}
