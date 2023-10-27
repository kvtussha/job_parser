from pprint import pprint

from src.hh import HeadHunterAPI
from src.superjob import SuperJobAPI


class SortVacanciesHH:
    def __init__(self):
        self._hh_api = HeadHunterAPI()
        self._all_vacancies = self._hh_api.all_vacancies()
        """{'currency': 'BYR', 'from': 2320, 'gross': True, 'to': 5320}"""

    def _zero_values_salaries(self):

        """Значения None в словаре с заплатой заменяем на 0"""
        for x in self._all_vacancies:
            salary_dict = x['salary']
            if salary_dict['from'] is None:
                salary_dict['from'] = 0
            if salary_dict['to'] is None:
                salary_dict['to'] = 0
        return self._all_vacancies

    def _rur_currency(self):
        """Переводим валюту в RUR"""
        currency = {
            'KZT': 0.2,
            'BYR': 28.35,
            'UZS': 0.0077
        }
        self._all_vacancies = self._zero_values_salaries()

        for x in self._all_vacancies:
            salary_dict = x['salary']
            if salary_dict:
                if salary_dict['currency'] != 'RUR':
                    if salary_dict['from']:
                        salary_dict['from'] = currency[salary_dict['currency']] * salary_dict['from']
                    if salary_dict['to']:
                        salary_dict['to'] = currency[salary_dict['currency']] * salary_dict['to']
                    salary_dict['currency'] = 'RUR'
        return self._all_vacancies

    @property
    def sort_by_salary(self):
        self._all_vacancies = self._rur_currency()
        self._all_vacancies = sorted(self._all_vacancies, key=lambda x: x['salary']['from'])
        return self._all_vacancies


class SortVacanciesSJ:
    def __init__(self):
        self._sj_api = SuperJobAPI()
        self._all_vacancies = self._sj_api.all_vacancies()

    @property
    def sort_by_salary(self):
        self._all_vacancies = sorted(self._all_vacancies, key=lambda x: x['payment_from'])
        return self._all_vacancies


# hh_api = SortVacanciesHH()
# for i in hh_api.sort_by_salary:
#     print(i['salary'])

# sj_api = SortVacanciesSJ()
# for i in sj_api.sort_by_salary:
#     print(i['payment_from'])
