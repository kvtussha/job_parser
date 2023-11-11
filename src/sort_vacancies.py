import json

import requests

from settings.implemented import headers
from src.json_class import JsonFile
from src.salary_conversion import SalaryConversion
from src.superjob import SuperJobAPI


class SortVacancies:
    def __init__(self):
        self.sj_info = JsonFile.load_json('sj_vacancies.json')
        self.hh_info = SalaryConversion().rur_currency()

    @staticmethod
    def filter_vacancies(filter_words: list) -> list:
        _response_hh = requests.get(f'https://api.superjob.ru/2.0/vacancies/?keywords={filter_words}', headers=headers)
        response = _response_hh.json().get('objects')

        result = []
        result.extend(response)
        JsonFile.write_json(result)
        return result

    @staticmethod
    def get_top_vacancies(info: list, top_num: int) -> list:
        JsonFile.write_json(info[:top_num])
        return info[:top_num]


