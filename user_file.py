from src.hh import HeadHunterAPI
from src.json_class import JsonFile
from src.sort_vacancies import SortVacanciesHH, SortVacanciesSJ
from src.superjob import SuperJobAPI
from src.vacancy import VacancyHH, VacancySJ

input1 = input('Здравствуйте! Напишите цифру:\n'
               '1. Я ищу работу\n'
               '2. Я работодатель \n')
service = input('Напишите название сервиса: HeadHunter / SuperJob \n')
if input1 == '1':
    input2 = input('Выберите цифру: \n'
                   '1. Если Вы хотите посмотреть все вакансии \n'
                   '2. Если Вы хотите найти вакансию по кодовому слову. Например: менеджер, продавец \n')
    if input2 == '2':
        keyword_ = input('Введите кодовое слово \n')

    if input2 == '1':
        input3 = input('Хотите увидеть вакансии : \n'
                       '1. По возрастанию зарплаты \n'
                       '2. В любом порядке \n')
elif input1 == '2':
    input4 = input('Вы хотите:'
                   '1. Cоздать вакансию'
                   '2. Изменить вакансию'
                   '3. Удалить вакансию? \n')

hh = HeadHunterAPI()
sj = SuperJobAPI()
j = JsonFile()

if service == 'HeadHunter':
    instance = hh
    vacancy = VacancyHH
elif service == 'SuperJob':
    instance = sj
    vacancy = VacancySJ


def search_vac():
    if input2 == '1' and input3 == '2':
        print(j.write_json_file(instance.all_vacancies()))
    elif input2 == '1' and input3 == '1':
        sort_ = SortVacanciesHH()
        print(j.write_json_file(sort_.sort_by_salary))
    elif input2 == '2':
        print(j.write_json_file(instance.get_vacancies(keyword_)))
    return ''


def create_vacancy():
    if input4 == '1':
        company_name = input('Введите название компании \n')
        vacancy_name = input('Введите название вакансии \n')
        salary = input('Введите зарплату \n')
        schedule = input('Введите расписание \n')
        experience = input('Введите опыт \n')
        new_vac = VacancyHH(service, company_name, vacancy_name, schedule, salary, experience)
        new_vac.create_vacancy()
        print(f'Вакансия добавлена в список новых вакансий. Полный список новых вакансий: {new_vac.new_vacancies}')


def change_vacancy():
    if input4 == '2':
        vid = int(input('Введите id вакансии \n'))
        k = input('Введите ключ в вакансии, значение которого хотите изменить \n')
        v = input('Введите значение для ключа вакансии \n')
        vacancy.change_vacancy(vid, k, v)
        print(f'Вакансия с id {vid} была изменена. Полный список новых вакансий: {VacancyHH.new_vacancies}')


def delete_vacancy():
    if input4 == '3':
        print('Внимание! Удаление возможно только в списке новых вакансий')
        vid = input('Введите id вакансии \n')
        print(vacancy.new_vacancies.delete_vacancy(vid))
    return ''


if input1 == '1':
    search_vac()
elif input1 == '2':
    if input4 == '1':
        create_vacancy()
    elif input4 == '2':
        change_vacancy()
    elif input4 == '3':
        delete_vacancy()
