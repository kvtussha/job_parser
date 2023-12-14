from main_utils import UserFunctions

user_func = UserFunctions()


# Function to interact with the user
def user_interaction():
    platforms = ["HeadHunter", "SuperJob"]

    role = input('Здравствуйте! Выберите цифру:\n'
                 '1. Я работадатель\n'
                 '2. Я ищу работу\n')
    platform = input('Введите платформу: HeadHunter или SuperJob\n')

    if platform not in platforms:
        print('Вы ошиблись с вводом')

    if role == '1':
        if platform == platforms[0]:
            if user_func.action_emp == '1':
                user_func.employer_create_vac()
            elif user_func.action_emp == '2':
                user_func.employer_del_vac()
    elif role == '2':
        if UserFunctions.action_cl == '1':
            res = user_func.key_sort()
        elif UserFunctions.action_cl == '2':
            res = user_func.salary_sort()
        elif UserFunctions.action_cl == '3':
            res = user_func.salary_keyword_sort()
        return res
    else:
        print('Возможно, Вы ошиблись с вводом\n')


if __name__ == "__main__":
    user_interaction()
