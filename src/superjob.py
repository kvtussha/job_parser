import json

import requests

from settings.implemented import headers
from src.job import Job
from src.json_class import JsonFile


class SuperJobAPI(Job):
    def __init__(self):
        self._auth = requests.get('https://api.superjob.ru/2.0/vacancies/', headers=headers)
        self.response = self._auth.text

    def get_all_vacancies(self) -> list:
        """
                Get all the vacancies, with full information about each one.
                Return:
                     list: a list containing dictionaries with information about
                     for each vacancy.
                """
        return json.loads(self.response)['objects']

    def vacancies_by_profession(self, title: str) -> list | str:
        """
                Get vacancies by the name of the specialty.
                Param:
                    title: str, the name of the specialty from the user
                Return:
                    list: if there are vacancies with this specialty name, you will receive them
                    str: if there are no vacancies with this specialty name, you will receive
                    a phrase with an apology
                """
        vacancies = self.get_all_vacancies()
        need_results = [item for item in vacancies if title.lower() in item['profession'].lower()]

        if need_results:
            JsonFile().write_json(need_results, 'search_result.json')
            return need_results
        else:
            return "No results found"
