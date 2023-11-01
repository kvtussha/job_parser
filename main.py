# Creating a class instance to work with the APIs of job search sites

from src.hh import HeadHunterAPI
from src.json_class import JsonFile
from src.sort_vacancies import SortVacancies
from src.superjob import SuperJobAPI
from src.vacancy import Vacancy

hh_api = HeadHunterAPI()
superjob_api = SuperJobAPI()

# Getting job vacancies from different platforms
hh_vacancies = hh_api.get_vacancies("Менеджер")
superjob_vacancies = superjob_api.get_vacancies("Полицейский")

# Creating a class instance to work with vacancies
vacancy = Vacancy("Сбербанк", "Python Developer", "г.Москва, ул. Садовая, д.3", "100 000-150 000 руб.")

# Saving information about vacancies to a file
json_saver = JsonFile()
vacancy.add_vacancy()
vacancy.get_vacancies_by_salary(30000, 45000)
vacancy.delete_vacancy(0)
#
sort_vacancies = SortVacancies()


# Function to interact with the user
def user_interaction():
    platforms = ["HeadHunter", "SuperJob"]
    search_query = input("Enter a search query: ")
    top_n = int(input("Enter the number of vacancies to display in top N: "))
    filter_words = input("Enter keywords to filter vacancies: ").split()
    filtered_vacancies = sort_vacancies.filter_vacancies(hh_vacancies, superjob_vacancies, filter_words)
    # print(filtered_vacancies)

    if not filtered_vacancies:
        print("Vacancies matching the selected criteria are not found.")
        return

    top_vacancies = sort_vacancies.get_top_vacancies(filtered_vacancies, top_n)
    # print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
