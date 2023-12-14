from settings.implemented import hh_all_vacancies, sj_all_vacancies
from src.sort_vacancies import SortVacancies
from src.vacancy import VacancyHH, VacancySJ

sort_vacancies = SortVacancies()


class UserFunctions:
    platform = input('Введите платформу: HeadHunter или SuperJob\n')
    action_emp = input('Выберите цифру:\n'
                       '1. Я хочу создать вакансию\n'
                       '2. Я хочу удалить вакансию\n')
    action_cl = input('Выберите цифру:\n'
                      '1. Я хочу получить вакансии по ключевому слову\n'
                      '2. Я хочу получить вакансии по зарплате\n'
                      '3. Я хочу получить вакансии и по ключевому слову, и по зарплате\n')
    key_words = input('Введите ключевые слова\n').split()
    first_salary = int(input('Введите нижний порог зарплаты\n'))
    second_salary = int(input('Введите верхний порог зарплаты\n'))
    top_n = int(input("Введите число топ-N вакансий, которые хотите получать: \n"))

    @classmethod
    def __employer_info(cls):
        company_name = input('Введите название компании\n')
        post = input('Введите название должности\n')
        address = input('Введите адрес\n')
        salary = input('Введите зарплату в таком формате: "100 000-150 000 руб."\n')

        return [cls.platform, company_name, post, address, salary]

    @classmethod
    def employer_create_vac(cls):
        """Функция работы с работодателем"""
        if cls.platform == 'HeadHunter':
            vacancy = VacancyHH(cls.__employer_info()[1], cls.__employer_info()[2],
                                cls.__employer_info()[3], cls.__employer_info()[4])
            return vacancy.add_vacancy()
        elif cls.platform == 'SuperJob':
            vacancy = VacancySJ(cls.__employer_info()[1], cls.__employer_info()[2],
                                cls.__employer_info()[3], cls.__employer_info()[4])
            return vacancy.add_vacancy()
        else:
            print("Извините, произошла ошибка")

    @classmethod
    def employer_del_vac(cls):
        vac_list = []

        if cls.platform == 'HeadHunter':
            vac_list = hh_all_vacancies
        elif cls.platform == 'SuperJob':
            vac_list = sj_all_vacancies
        else:
            print("Извините, произошла ошибка")

        if vac_list:
            vid = int(
                input(f'Введите индекс вакансии, которую хотите удалить: '
                      f'от 0 до {len(vac_list) - 2}\n'))
            return VacancyHH.delete_vacancy(vid)

    @classmethod
    def key_sort(cls):
        print('Внимание! Сортировка по ключевому слову доступна лишь на платформе SuperJob')
        if cls.platform == 'SuperJob':
            res = SortVacancies().key_filter_vacancies(cls.key_words)
            return SortVacancies.get_top_vacancies(res, cls.top_n)
        else:
            print('Извините, название платформы указано неверно. Попробуйте еще раз')

    @classmethod
    def salary_sort(cls):
        res = []
        if cls.platform == 'HeadHunter':
            res = VacancyHH.get_vacancies_by_salary(cls.first_salary, cls.second_salary)
        elif cls.platform == 'SuperJob':
            res = VacancySJ.get_vacancies_by_salary(cls.first_salary, cls.second_salary)
        return SortVacancies.get_top_vacancies(res, cls.top_n)

    @classmethod
    def salary_keyword_sort(cls):
        res = []
        for i in cls.key_sort():
            if i in cls.salary_sort():
                res.append(i)
        return SortVacancies.get_top_vacancies(res, cls.top_n)
