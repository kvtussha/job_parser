from src.hh import HeadHunterAPI
from src.json_class import JsonFile
from src.salary_conversion import SalaryConversion
from src.superjob import SuperJobAPI


class Vacancy:
    new_vacancies = []
    hh_all_vacancies = HeadHunterAPI().get_all_vacancies()
    sj_all_vacancies = SuperJobAPI().all_vacancies()

    def __init__(self, company_name, vacancy_name, address, salary):
        self.company_name = company_name
        self.vacancy_name = vacancy_name
        self.address = address
        self.salary = salary

    def add_vacancy(self, platform):
        vac = {
            'company': self.company_name,
            'name': self.vacancy_name,
            'address': self.address,
            'salary': self.salary,
        }
        if platform == 'HeadHunter':
            Vacancy.hh_all_vacancies.append(vac)
            print(Vacancy.hh_all_vacancies[-1])
        elif platform == 'SuperJob':
            Vacancy.sj_all_vacancies.append(vac)
            print(Vacancy.sj_all_vacancies[-1])
        print('Вакансия добавлена')
        return vac

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
        print(f'Результат по Вашему запросу записан в файл search_result.json')
        return result

    @staticmethod
    def get_vacancies_by_salary_sj(first_value, second_value):
        sj_all_vacancies = SuperJobAPI().all_vacancies()
        result = []

        for i in sj_all_vacancies:
            if i['payment_from'] <= first_value:
                if i['payment_to'] <= second_value:
                    result.append(i)

        JsonFile().write_json(result, 'search_result.json')
        print(f'Результат по Вашему запросу записан в файл search_result.json')
        return result

    @staticmethod
    def delete_vacancy(platform, vid):
        if platform == 'HeadHunter':
            data = Vacancy.hh_all_vacancies
        elif platform == 'SuperJob':
            data = Vacancy.sj_all_vacancies
        else:
            data = []

        if data:
            if 0 <= vid <= len(data):
                del data[vid]
            else:
                print('Элемента с таким индексом нет в списке')
        return 'Вакансия удалена'
