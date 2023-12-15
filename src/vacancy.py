from src.hh import HeadHunterAPI
from src.json_class import JsonFile
from src.salary_conversion import SalaryConversion
from src.superjob import SuperJobAPI

hh_all_vacancies = HeadHunterAPI().get_all_vacancies()
sj_all_vacancies = SuperJobAPI().get_all_vacancies()


class VacancyHH:
    """
            A class for creating, adding and deleting vacancies on the platform HeadHunter.
            Methods:
                add_vacancy: creates a dictionary with attributes for a new job and adds them to the job list
                get_vacancies_by_salary: it goes through the list of vacancies, converts the salary dictionary
                    using the SalaryConversion class and checks whether the salary is included in the values
                    from and to
                delete_vacancy: in the list of vacancies, it finds a vacancy with the desired id and deletes it
            """
    def __init__(self, company_name: str, vacancy_name: str, address: str, salary: dict | str | None):
        self.company_name = company_name
        self.vacancy_name = vacancy_name
        self.address = address
        self.salary = salary

    def add_vacancy(self) -> dict:
        """
                Adds a new vacancy to all others
                Return:
                    dict, in the dictionary, the parameters of a new vacancy
                """
        vac = {
            'company': self.company_name,
            'name': self.vacancy_name,
            'address': self.address,
            'salary': self.salary,
        }
        hh_all_vacancies.append(vac)
        print('Вакансия добавлена')
        return vac

    @staticmethod
    def get_vacancies_by_salary(first_value: int, second_value: int) -> list:
        """
                Getting vacancies at the upper and lower salary limits
                Params:
                    first_value: int, salary, not lower than which vacancies are needed
                    second_value: salary, no higher than which vacancies are needed
                Return:
                    list, a list of vacancies suitable for salary
                """
        result = []

        for i in hh_all_vacancies:
            if i['salary']:
                SalaryConversion().salary_value(i['salary'])
                if i['salary']['from'] <= first_value:
                    if i['salary']['to'] <= second_value:
                        result.append(i)

        JsonFile().write_json(result)
        return result

    @staticmethod
    def delete_vacancy(vid: int) -> None:
        """
                Deleting a job by id
                Param:
                    vid: int, id vacancy
                Return:
                    None, if the vacancy was deleted
                """
        data = hh_all_vacancies
        if data:
            if 0 <= vid <= len(data):
                del data[vid]
            else:
                print('Элемента с таким индексом нет в списке')
        print('Вакансия удалена')


class VacancySJ:
    """
            A class for creating, adding and deleting vacancies on the platform SuperJob.
            Methods:
                add_vacancy: creates a dictionary with attributes for a new job and adds them to the job list
                get_vacancies_by_salary: it goes through the list of vacancies, converts the salary dictionary
                    using the SalaryConversion class and checks whether the salary is included in the values from and to
                delete_vacancy: in the list of vacancies, it finds a vacancy with the desired id and deletes it
            """
    def __init__(self, company_name: str, vacancy_name: str, address: str, salary: int | str):
        self.company_name = company_name
        self.vacancy_name = vacancy_name
        self.address = address
        self.salary = salary

    def add_vacancy(self):
        """
                Adds a new vacancy to all others
                Return:
                    dict, in the dictionary, the parameters of a new vacancy
                """
        vac = {
            'company': self.company_name,
            'name': self.vacancy_name,
            'address': self.address,
            'salary': self.salary,
        }
        sj_all_vacancies.append(vac)
        print('Вакансия добавлена')
        return vac

    @staticmethod
    def get_vacancies_by_salary(first_value: int, second_value: int) -> list:
        """
                Getting vacancies at the upper and lower salary limits
                Params:
                    first_value: int, salary, not lower than which vacancies are needed
                    second_value: salary, no higher than which vacancies are needed
                Return:
                    list, a list of vacancies suitable for salary
                """
        result = []

        for i in sj_all_vacancies:
            if i['payment_from'] <= first_value:
                if i['payment_to'] <= second_value:
                    result.append(i)

        JsonFile().write_json(result)
        return result

    @staticmethod
    def delete_vacancy(vid: int) -> None:
        """
                Deleting a job by id
                Param:
                    vid: int, id vacancy
                Return:
                    None, if the vacancy was deleted
                """
        data = sj_all_vacancies

        if data:
            if 0 <= vid <= len(data):
                del data[vid]
            else:
                print('Элемента с таким индексом нет в списке')
        print('Вакансия удалена')
