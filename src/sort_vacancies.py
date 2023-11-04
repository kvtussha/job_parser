import json

import requests

from settings.implemented import headers
from src.json_class import JsonFile
from src.salary_conversion import SalaryConversion
from src.superjob import SuperJobAPI


class SortVacancies:
    def __init__(self):
        self.sj_all_vacancies = SuperJobAPI().all_vacancies()
        self.hh_all_vacancies = SalaryConversion().rur_currency()

    @staticmethod
    def filter_vacancies(hh_vacancies: list, superjob_vacancies: list, filter_words: list) -> list:
        _response_hh = requests.get(f'https://api.superjob.ru/2.0/vacancies/?keywords={filter_words}', headers=headers)
        response = _response_hh.text

        result = []
        result.extend(hh_vacancies)
        result.extend(superjob_vacancies)
        result.extend(response)
        JsonFile.write_json(result)
        return result

    @staticmethod
    def get_top_vacancies(info: list, top_num: int) -> list:
        JsonFile.write_json(info[:top_num])
        return info[:top_num]
