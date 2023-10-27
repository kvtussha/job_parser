from src.hh import HeadHunterAPI


class VacancyHH:
    new_vacancies = []

    def __init__(self, service, company_name, vacancy_name, schedule, salary, experience):
        self.service = service
        self.hh = HeadHunterAPI()
        self.all_vacancies = self.hh.all_vacancies()

        self.company_name = company_name
        self.vacancy_name = vacancy_name
        self.salary = salary
        self.schedule = schedule
        self.experience = experience

    def create_vacancy(self):
        vac = {
            'name': self.vacancy_name,
            'salary': self.salary,
            'schedule': self.schedule,
            'experience': self.experience,
            'employer': {'name': self.company_name}
        }
        VacancyHH.new_vacancies.append(vac)
        return VacancyHH.new_vacancies

    @staticmethod
    def change_vacancy(vid, key, value):
        vac = VacancyHH.new_vacancies[vid]
        vac[key] = value
        return VacancyHH.new_vacancies

    @staticmethod
    def delete_vacancy(vid):
        all_vac = VacancyHH.new_vacancies
        all_vac.pop(vid)
        return "Вакансия была удалена"


class VacancySJ:
    def __init__(self, service, company_name, vacancy_name, payment_from, payment_to, experience):
        self.service = service
        self.hh = HeadHunterAPI()
        self.all_vacancies = self.hh.all_vacancies()

        self.company_name = company_name
        self.vacancy_name = vacancy_name
        self.payment_from = payment_from
        self.payment_to = payment_to
        self.experience = experience

    def create_vacancy(self):
        vac = {
            'name': self.vacancy_name,
            'salary': {'payment_from': self.payment_from,
                       'payment_to': self.payment_to},
            'experience': self.experience,
            'firm_name': self.company_name
        }
        return self.all_vacancies.append(vac)

    def change_vacancy(self, vid, key, value):
        vac = self.all_vacancies[vid]
        vac[key] = value

        return "Вакансия была изменена"

    def delete_vacancy(self, vid):
        all_vac = self.all_vacancies
        all_vac.pop(vid)

        return "Вакансия была изменена"
