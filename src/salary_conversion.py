from pprint import pprint

from src.hh import HeadHunterAPI
from src.json_class import JsonFile


class SalaryConversion:
    """Класс для преобразования зарплаты в HH"""

    def __init__(self):
        self._all_vacancies = HeadHunterAPI().all_vacancies()
        """{'currency': 'BYR', 'from': 2320, 'gross': True, 'to': 5320}"""

    def _zero_values_salaries(self):

        """Значения None в словаре с заплатой заменяем на 0"""
        for x in self._all_vacancies:
            if x['salary']:
                salary_dict = x['salary']
                if salary_dict['from'] is None:
                    salary_dict['from'] = 0
                if salary_dict['to'] is None:
                    salary_dict['to'] = 0
        return self._all_vacancies

    def rur_currency(self):
        """Переводим валюту в RUR"""
        currency = {
            'KZT': 0.2,
            'BYR': 28.35,
            'UZS': 0.0077,
            'KGS': 1.05,
            'USD': 93.55
        }
        self._all_vacancies = self._zero_values_salaries()

        for x in self._all_vacancies:
            if x['salary']:
                salary_dict = x['salary']
                if salary_dict:
                    if salary_dict['currency'] != 'RUR':
                        if salary_dict['from']:
                            salary_dict['from'] = currency[salary_dict['currency']] * salary_dict['from']
                        if salary_dict['to']:
                            salary_dict['to'] = currency[salary_dict['currency']] * salary_dict['to']
                        salary_dict['currency'] = 'RUR'
        return self._all_vacancies


# s = SalaryConversion()
# for i in s.rur_currency():
#     print(i['salary'])
