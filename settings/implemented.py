import os

from dotenv import load_dotenv

load_dotenv()
SJ_API_KEY = os.getenv('SJ_API_KEY')
ER_API_KEY = os.getenv('ER_API_KEY')

headers = {'Host': 'api.superjob.ru',
           'X-Api-App-Id': SJ_API_KEY,
           'Authorisation': f'Bearer {SJ_API_KEY[3:]}',
           'Content-Type': 'application/x-www-form-urlencoded'}
