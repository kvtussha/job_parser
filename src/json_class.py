import json


class JsonFile:
    @staticmethod
    def write_json(info: list, filename='search_result.json') -> None:
        """
                Get vacancies by the name of the specialty.
                Param:
                    info: list, a list with information to be written in json
                    filename: str, file name
                Return:
                    None: if there were no errors and everything worked out
                """
        with open(filename, 'w', encoding='utf-8') as outfile:
            json.dump(info, outfile, indent=4, ensure_ascii=False)
            print(f'Результат по Вашему запросу записан в файл {filename}')

    @staticmethod
    def load_json(filename: str) -> list:
        """
                The function loads information from json
                Param:
                    filename: str, file name
                Return:
                    list: information received
                """
        data = []
        try:
            with open(filename) as json_file:
                res = json.load(json_file)
                data.extend(res)
        except FileNotFoundError:
            pass
        finally:
            return data
