# Creating a class instance to work with the APIs of job search sites

from src.hh import HeadHunterAPI
from src.json_class import JsonFile
from src.sort_vacancies import SortVacancies
from src.superjob import SuperJobAPI
from src.vacancy import Vacancy

# Creating instances of service classes
hh_api = HeadHunterAPI()
superjob_api = SuperJobAPI()
sort_vacancies = SortVacancies()


# Function to interact with the user
def user_interaction():
    platforms = ["HeadHunter", "SuperJob"]

    while True:
        role = input('Здравствуйте! Выберите цифру:\n'
                     '1. Я работадатель\n'
                     '2. Я ищу работу\n'
                     '3. Выход')
        platform = input('Введите платформу: HeadHunter или SuperJob')
        if platform not in platforms:
            print('Вы ошиблись с вводом')
            break
        top_n = int(input("Введите число топ-N вакансий, которые хотите получать: "))

        if role == '1':
            action = input('Выберите цифру:\n'
                           '1. Я хочу создать вакансию\n'
                           '2. Я хочу удалить вакансию\n')
            if action == '1':
                company_name = input('Введите название компании')
                post = input('Введите название должности')
                address = input('Введите адрес')
                salary = input('Введите зарплату в таком формате: "100 000-150 000 руб."')

                vacancy = Vacancy(company_name, post, address, salary)
                print(vacancy.add_vacancy())
            elif action == '2':
                data = JsonFile.load_json('new_vacancies.json')
                vid = int(input(f'Введите индекс вакансии, которую хотите удалить: от 0 до {len(data) - 1}'))
                print(Vacancy.delete_vacancy(vid))
            else:
                print('Возможно, вы ошиблись в вводе. Попробуйте еще раз')
        elif role == '2':
            action = input('Выберите цифру:\n'
                           '1. Я хочу получить вакансии по ключевому слову\n'
                           '2. Я хочу получить вакансии по зарплате\n'
                           '3. Я хочу получить вакансии и по ключевому слову, и по зарплате\n')
            if action == '1':
                key_words = input('Введите ключевые слова').split()
                info = sort_vacancies.filter_vacancies(key_words)
                top_vacancies = sort_vacancies.get_top_vacancies(info, top_n)
                print(top_vacancies)
            elif action == '2':
                first_salary = int(input('Введите нижний порог зарплаты'))
                second_salary = int(input('Введите верхний порог зарплаты'))
                if platform == 'HeadHunter':
                    info = Vacancy.get_vacancies_by_salary_hh(first_salary, second_salary)
                    top_vacancies = sort_vacancies.get_top_vacancies(info, top_n)
                    print(top_vacancies)
                elif platform == 'SuperJob':
                    info = Vacancy.get_vacancies_by_salary_sj(first_salary, second_salary)
                    top_vacancies = sort_vacancies.get_top_vacancies(info, top_n)
                    print(top_vacancies)
            elif action == '3':
                key_words = input('Введите ключевые слова').split()
                sort_vacancies.filter_vacancies(key_words)
                first_salary = int(input('Введите нижний порог зарплаты'))
                second_salary = int(input('Введите верхний порог зарплаты'))
                if platform == 'HeadHunter':
                    info = Vacancy.get_vacancies_by_salary_hh(first_salary, second_salary)
                    top_vacancies = sort_vacancies.get_top_vacancies(info, top_n)
                    print(top_vacancies)
                elif platform == 'SuperJob':
                    info = Vacancy.get_vacancies_by_salary_sj(first_salary, second_salary)
                    top_vacancies = sort_vacancies.get_top_vacancies(info, top_n)
                    print(top_vacancies)
        elif role == '3':
            break
        else:
            print('Возможно, Вы ошиблись с вводом')


if __name__ == "__main__":
    user_interaction()
