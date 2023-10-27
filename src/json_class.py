import json


class JsonFile:
    def write_json_file(self, info: list):
        """Функция, которая записывает в json file"""
        with open('data.txt', 'w', encoding='utf-8') as outfile:
            json.dump(info, outfile, ensure_ascii=False)
        return 'Результаты по вашему запросу записаны в файл data.txt'

    def read_json(self, filename):
        """Функция, которая читает json file"""
        with open(filename) as json_file:
            data = json.load(json_file)
        return data
    