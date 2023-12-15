from src.user_functions import UserFunctions, platform

user_func = UserFunctions()


# Function to interact with the user
def user_interaction():
    role = input("Выберите роль:\n"
                 "1. Работодатель\n"
                 "2. Ищу работу\n")
    if role == '1':
        action_emp = input('Выберите цифру:\n'
                           '1. Я хочу создать вакансию\n'
                           '2. Я хочу удалить вакансию\n')
        if action_emp == '1':
            user_func.employer_create_vac()
        elif action_emp == '2':
            user_func.employer_del_vac()
        else:
            print('Вы ошиблись с вводом. Попробуйте еще раз')
    elif role == '2':
        res = []
        if platform == 'HeadHunter':
            print('На платформе SuperJob еще больше интересного) Посмотри')
            action_cl = input('Выберите цифру:\n'
                              '1. Я хочу получить вакансии по зарплате\n')
            if action_cl == '1':
                res = user_func.salary_sort()
        elif platform == 'SuperJob':
            action_cl = input('Выберите цифру:\n'
                              '1. Я хочу получить вакансии по ключевому слову\n'
                              '2. Я хочу получить вакансии по зарплате\n'
                              '3. Я хочу получить вакансии и по ключевому слову, и по зарплате\n')
            if action_cl == '1':
                res = user_func.key_sort()
            elif action_cl == '2':
                res = user_func.salary_sort()
            elif action_cl == '3':
                res = user_func.salary_keyword_sort()
            else:
                print('Вы ошиблись с вводом. Попробуйте еще раз')
        else:
            print('Извините, Вы ошиблись с названием платформы')

        if res:
            return res
    else:
        print('Возможно, Вы ошиблись с вводом\n')


if __name__ == "__main__":
    user_interaction()
