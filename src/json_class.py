import json


class JsonFile:
    @staticmethod
    def write_json(info, filename='search_result.json'):
        """Функция, которая записывает в json file"""
        data = JsonFile.load_json(filename)
        data.append(info)
        with open(filename, 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, indent=4, ensure_ascii=False)
        return f'Результаты по вашему запросу записаны в файл {filename}'

    @staticmethod
    def load_json(filename):
        data = []
        """Функция, которая читает json file"""
        try:
            with open(filename) as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            pass
        finally:
            return data
