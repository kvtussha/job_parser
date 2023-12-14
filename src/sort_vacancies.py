import requests

from settings.implemented import headers
from src.json_class import JsonFile


class SortVacancies:
    """
            A class that filters vacancies
            Methods:
                filter_vacancies: getting vacancies by keyword
                get_top_vacancies: returns a list with a certain number of vacancies
            """
    @staticmethod
    def key_filter_vacancies(filter_words: list) -> list:
        """
                Getting vacancies by keyword
                Param:
                    filter_words: list, keywords in the list
                Return:
                    list, there are vacancies in the list that contain keywords
                """
        __response_hh = requests.get(f'https://api.superjob.ru/2.0/vacancies/?keywords={filter_words}',
                                     headers=headers)
        _response = __response_hh.json().get('objects')

        result = []
        result.extend(_response)
        JsonFile.write_json(result)
        return result

    @staticmethod
    def get_top_vacancies(info: list, top_num: int) -> list:
        """
                Receives a certain number of vacancies
                Params:
                    info: list, the list of vacancies that need to be trimmed
                    top_num: int, a number indicating how many vacancies need to be returned
                Return:
                    list, converted job list
                """
        data = info[:top_num]
        JsonFile.write_json(data)
        return data
