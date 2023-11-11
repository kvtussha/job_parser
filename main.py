from main_utils import employer, seek_employment


# Function to interact with the user
def user_interaction():
    platforms = ["HeadHunter", "SuperJob"]

    role = input('Здравствуйте! Выберите цифру:\n'
                 '1. Я работадатель\n'
                 '2. Я ищу работу\n')
    platform = input('Введите платформу: HeadHunter или SuperJob\n')
    if role == '2':
        top_n = int(input("Введите число топ-N вакансий, которые хотите получать: \n"))

    if platform not in platforms:
        print('Вы ошиблись с вводом')

    if role == '1':
        print(employer(platform))
    elif role == '2':
        print(seek_employment(platform, top_n))
    else:
        print('Возможно, Вы ошиблись с вводом\n')


if __name__ == "__main__":
    user_interaction()
