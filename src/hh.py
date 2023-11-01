import json
from pprint import pprint

import requests

from src.job import Job


class HeadHunterAPI(Job):
    def __init__(self):
        self._response_hh = requests.get('https://api.hh.ru/vacancies')
        self._response = self._response_hh.text

    def all_vacancies(self):
        """Получение всей информации о вакансиях"""
        return json.loads(self._response)['items']

    def get_vacancies(self, title):
        """Получение информации о вакансии по названию специальности"""
        vacancies = self.all_vacancies()
        need_results = []
        for item in vacancies:
            if title.lower() in item['name'].lower():
                need_results.append(item)

        if need_results:
            return need_results
        else:
            return "Результатов не найдено"


# hh_api = HeadHunterAPI()
# pprint(hh_api.all_vacancies())
# count = 0
# print(len(hh_api.all_vacancies()))
# for i in hh_api.all_vacancies():
#     if i['salary']:
#         print(i['salary'])
#
# print(count)


# hh_api = HeadHunterAPI()
# hh_vacancies = hh_api.get_vacancies("Менеджер")
# pprint(hh_vacancies)
