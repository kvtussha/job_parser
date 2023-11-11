from src.hh import HeadHunterAPI
from src.json_class import JsonFile
from src.sort_vacancies import SortVacancies
from src.superjob import SuperJobAPI
from src.vacancy import Vacancy

# Creating instances of service classes
hh_api = HeadHunterAPI()
superjob_api = SuperJobAPI()
sort_vacancies = SortVacancies()


def employer(platform):
    """Функция работы с работодателем"""
    action = input('Выберите цифру:\n'
                   '1. Я хочу создать вакансию\n'
                   '2. Я хочу удалить вакансию\n')
    if action == '1':
        company_name = input('Введите название компании\n')
        post = input('Введите название должности\n')
        address = input('Введите адрес\n')
        salary = input('Введите зарплату в таком формате: "100 000-150 000 руб."\n')

        vacancy = Vacancy(company_name, post, address, salary)
        return vacancy.add_vacancy(platform)
    elif action == '2':
        data = hh_api.all_vacancies()
        vid = int(input(f'Введите индекс вакансии, которую хотите удалить: от 0 до {len(data) - 2}\n'))
        return Vacancy.delete_vacancy(vid, platform)
    else:
        return 'Возможно, вы ошиблись в вводе. Попробуйте еще раз\n'


def seek_employment(platform, top_n):
    """Функция работы с соискателем"""
    action = input('Выберите цифру:\n'
                   '1. Я хочу получить вакансии по ключевому слову\n'
                   '2. Я хочу получить вакансии по зарплате\n'
                   '3. Я хочу получить вакансии и по ключевому слову, и по зарплате\n')
    if action == '1':
        print('Внимание! Сортировка по ключевому слову доступна лишь на платформе SuperJob')
        if platform == 'SuperJob':
            return getting_by_keyword(top_n)
        else:
            print('Извините, название платформы указано неверно. Попробуйте еще раз')
    elif action == '2':
        return getting_salary(platform, top_n)
    elif action == '3':
        return keyword_salary(platform, top_n)


def getting_by_keyword(top_n: int):
    key_words = input('Введите ключевые слова\n').split()
    info = sort_vacancies.filter_vacancies(key_words)
    top_vacancies = sort_vacancies.get_top_vacancies(info, top_n)
    return top_vacancies


def getting_salary(platform: str, top_n: int):
    first_salary = int(input('Введите нижний порог зарплаты\n'))
    second_salary = int(input('Введите верхний порог зарплаты\n'))
    if platform == 'HeadHunter':
        info = Vacancy.get_vacancies_by_salary_hh(first_salary, second_salary)
        top_vacancies = sort_vacancies.get_top_vacancies(info, top_n)
        print(top_vacancies)
    elif platform == 'SuperJob':
        info = Vacancy.get_vacancies_by_salary_sj(first_salary, second_salary)
        top_vacancies = sort_vacancies.get_top_vacancies(info, top_n)
        print(top_vacancies)


def keyword_salary(platform: str, top_n: int):
    key_words = input('Введите ключевые слова\n').split()
    res1 = sort_vacancies.filter_vacancies(key_words)
    getting_salary(platform, top_n)


def comparison_vacancies(res1, res2):
    end_result = []
    if len(res1) <= len(res2):
        for item in res1:
            if item in res2:
                end_result.append(item)
    elif len(res2) <= len(res1):
        for item in res2:
            if item in res1:
                end_result.append(item)
    return end_result
