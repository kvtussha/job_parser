from src.hh import HeadHunterAPI
from src.json_class import JsonFile
from src.salary_conversion import SalaryConversion
from src.superjob import SuperJobAPI


class Vacancy:
    new_vacancies = []

    def __init__(self, company_name, vacancy_name, address, salary):
        self.company_name = company_name
        self.vacancy_name = vacancy_name
        self.address = address
        self.salary = salary
        self.hh_all_vacancies = HeadHunterAPI().all_vacancies()
        self.sj_all_vacancies = SuperJobAPI().all_vacancies()

    def add_vacancy(self):
        vac = {
            'company': self.company_name,
            'name': self.vacancy_name,
            'address': self.address,
            'salary': self.salary,
        }
        JsonFile().write_json(vac, 'new_vacancies.json')
        return f"Вакансия записана в файл с новыми вакансиями - new_vacancies.json"

    @staticmethod
    def get_vacancies_by_salary_hh(first_value, second_value):
        hh_all_vacancies = SalaryConversion().rur_currency()
        result = []

        for i in hh_all_vacancies:
            if i['salary']:
                if i['salary']['from'] <= first_value:
                    if i['salary']['to'] <= second_value:
                        result.append(i)

        JsonFile().write_json(result, 'search_result.json')
        return f'Результат по Вашему запросу записан в файл search_result.json'

    @staticmethod
    def get_vacancies_by_salary_sj(first_value, second_value):
        sj_all_vacancies = SuperJobAPI().all_vacancies()
        result = []

        for i in sj_all_vacancies:
            if i['payment_from'] <= first_value:
                if i['payment_to'] <= second_value:
                    result.append(i)

        JsonFile().write_json(result, 'search_result.json')
        return f'Результат по Вашему запросу записан в файл search_result.json'

    @staticmethod
    def delete_vacancy(vid):
        data = JsonFile().load_json('new_vacancies.json')
        if 0 <= vid < len(data):
            del data[vid]
            JsonFile.write_json(data, 'new_vacancies.json')
        else:
            print('Элемента с таким индексом нет в списке')
        return 'Вакансия удалена'

