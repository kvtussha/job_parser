from src.hh import HeadHunterAPI
from src.sort_vacancies import SortVacancies
from src.superjob import SuperJobAPI
from src.vacancy import VacancyHH, VacancySJ

sort_vacancies = SortVacancies()

hh_all_vacancies = HeadHunterAPI().get_all_vacancies()
sj_all_vacancies = SuperJobAPI().get_all_vacancies()

platform = input('Введите платформу: HeadHunter или SuperJob\n')


class UserFunctions:

    @classmethod
    def __employer_info(cls):
        company_name = input('Введите название компании\n')
        post = input('Введите название должности\n')
        address = input('Введите адрес\n')
        salary = input('Введите зарплату в таком формате: "100 000-150 000 руб."\n')
        return [platform, company_name, post, address, salary]

    @classmethod
    def employer_create_vac(cls):
        """Функция работы с работодателем"""
        emp_list = cls.__employer_info()
        if platform == 'HeadHunter':
            vacancy = VacancyHH(emp_list[1], emp_list[2],
                                emp_list[3], emp_list[4])
            vacancy.add_vacancy()
        elif platform == 'SuperJob':
            vacancy = VacancySJ(emp_list[1], emp_list[2],
                                emp_list[3], emp_list[4])
            vacancy.add_vacancy()
        else:
            print("Извините, произошла ошибка")

    @classmethod
    def employer_del_vac(cls):
        vac_list = []

        if platform == 'HeadHunter':
            vac_list = hh_all_vacancies
        elif platform == 'SuperJob':
            vac_list = sj_all_vacancies
        else:
            print("Извините, произошла ошибка")

        if vac_list:
            vid = int(
                input(f'Введите индекс вакансии, которую хотите удалить: '
                      f'от 0 до {len(vac_list) - 2}\n'))
            VacancyHH.delete_vacancy(vid)

    @classmethod
    def key_sort(cls):
        print('Внимание! Сортировка по ключевому слову доступна лишь на платформе SuperJob, убедитесь, что Вы на '
              'правильной платформе')
        key_words = input('Введите ключевые слова\n').split()
        top_n = int(input("Введите число топ-N вакансий, которые хотите получать: \n"))

        if platform == 'SuperJob':
            res = SortVacancies().key_filter_vacancies(key_words)
            return SortVacancies.get_top_vacancies(res, top_n)
        else:
            print('Извините, название платформы указано неверно. Попробуйте еще раз')

    @classmethod
    def salary_sort(cls):
        first_salary = int(input('Введите нижний порог зарплаты\n'))
        second_salary = int(input('Введите верхний порог зарплаты\n'))
        top_n = int(input("Введите число топ-N вакансий, которые хотите получать: \n"))

        res = []
        if platform == 'HeadHunter':
            res = VacancyHH.get_vacancies_by_salary(first_salary, second_salary)
        elif platform == 'SuperJob':
            res = VacancySJ.get_vacancies_by_salary(first_salary, second_salary)
        return SortVacancies.get_top_vacancies(res, top_n)

    @classmethod
    def salary_keyword_sort(cls):
        top_n = int(input("Введите число топ-N вакансий, которые хотите получать: \n"))
        res = []
        for i in cls.key_sort():
            if i in cls.salary_sort():
                res.append(i)
        return SortVacancies.get_top_vacancies(res, top_n)
