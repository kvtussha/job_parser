import json

import requests

from settings.implemented import headers
from src.job import Job
from src.json_class import JsonFile


class SuperJobAPI(Job):
    def __init__(self):
        self._auth = requests.get('https://api.superjob.ru/2.0/vacancies/', headers=headers)
        self.response = self._auth.text

    def all_vacancies(self) -> list:
        """Получение всей информации о вакансиях"""
        return json.loads(self.response)['objects']

    def get_vacancies(self, title: str) -> list | str:
        """Получение информации о вакансии по названию специальности"""
        vacancies = self.all_vacancies()
        need_results = []
        for item in vacancies:
            vacancy_name = item['profession'].lower()
            title = title.lower()

            if title in vacancy_name:
                need_results.append(item)

        if need_results:
            JsonFile().write_json(need_results, 'search_result.json')
            return need_results
        else:
            return "Результатов не найдено"


# sj = SuperJobAPI()
# print(sj.get_vacancies('продавец'))
# for i in sj.all_vacancies():
#     print(i['profession'])
