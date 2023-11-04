# Creating a class instance to work with the APIs of job search sites

from src.hh import HeadHunterAPI
from src.json_class import JsonFile
from src.sort_vacancies import SortVacancies
from src.superjob import SuperJobAPI
from src.vacancy import Vacancy

# Creating instances of service classes
hh_api = HeadHunterAPI()
superjob_api = SuperJobAPI()

# Getting job vacancies from different platforms
hh_vacancies = hh_api.get_vacancies("Курьер")
superjob_vacancies = superjob_api.get_vacancies("Продавец")

# Creating a class instance to work with vacancies
vacancy1 = Vacancy("Сбербанк", "Python Developer", "г.Москва, ул. Садовая, д.3", "100 000-150 000 руб.")
vacancy2 = Vacancy("Яндекс", "Java Developer", "г.Москва, ул. Ленинградская, д.5", "89 000-91 000 руб.")
vacancy3 = Vacancy("VK", "JavaScript Developer", "г.Москва, ул. Узбекистанская, д.8", "140 000-172 000 руб.")

# Saving information about vacancies to a file
json_saver = JsonFile()

# Creating new vacancies
vacancy1.add_vacancy()
vacancy2.add_vacancy()
vacancy3.add_vacancy()

# Getting vacancies by salary
vacancy2.get_vacancies_by_salary_hh(30000, 100000)
vacancy1.delete_vacancy(0)

# Create instance of class SortVacancies
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
