import json


class JsonFile:
    @staticmethod
    def write_json(info, filename='search_result.json'):
        """Функция, которая записывает в json file"""
        with open(filename, 'w', encoding='utf-8') as outfile:
            json.dump(info, outfile, indent=4, ensure_ascii=False)
        print(f'Результаты по вашему запросу записаны в файл {filename}')
        return info

    @staticmethod
    def load_json(filename):
        """Функция, которая читает json file"""
        data = []
        try:
            with open(filename) as json_file:
                res = json.load(json_file)
                data.extend(res)
        except FileNotFoundError:
            pass
        finally:
            return data

    @staticmethod
    def create_json(info, filename):
        with open(filename, 'w', encoding='utf-8') as outfile:
            json.dump(info, outfile, indent=4, ensure_ascii=False)
        return info
