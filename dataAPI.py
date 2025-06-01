from json import loads, dump
from csv import reader
from functools import reduce

class JsonAPI:
    def __init__(self, path_: str):
        self.__path: str = path_
        self.__data: dict = self.__save_default()

    def get(self):
        return self.__data.items()

    def __save_default(self) -> dict:
        json_file = open(self.__path, 'r+', encoding='utf-8')
        data = json_file.read()
        return loads(data)
    
    def update_default(self, path_: str, value_):
        self.deep_set(path_, value_)
        json_file = open(self.__path, 'r+', encoding='utf-8')
        json_file.seek(0)
        dump(self.__data, json_file, indent=4, ensure_ascii=False)
        json_file.truncate()

    def deep_get(self, keys_: str, default_=None, target_type_=None) -> object:
        _value = reduce(
            lambda d, key: d.get(key, default_) if isinstance(d, dict) else default_,
            keys_.split("."),
            self.__data
        )
        return _value if not target_type_ else target_type_(_value)
    
    def deep_set(self, path_: str, value):
        _saved_timetable: dict = self.__data
        _keys = path_.split('_')
        _latest = _keys.pop()
        for k in _keys:
            _saved_timetable = _saved_timetable.setdefault(k, {})
        _saved_timetable[_latest] = value

class CsvAPI:
    def __init__(self, path_: str, delimiter_: str = ";", comment_caracter_: str = "#"):
        self.__path: str = path_
        self.__delimiter = delimiter_
        self.__comment_caracter = comment_caracter_

    def get_data(self) -> list:
        _returned: list = []
        for row in self.__save_default():
            for i in row:
                if not self.__comment_caracter in i:
                    _returned.append(row)
                    break
        return _returned

    def get_comment(self) -> dict:
        _returned: list = []
        for row in self.__save_default():
            for i in row:
                i: str
                if self.__comment_caracter in i:
                    _character = i
                    _returned.append(_character.replace("# ", ""))
        return _returned

    def __save_default(self) -> dict:
        csv_file = open(self.__path, 'r+', encoding='utf-8')
        return reader(csv_file, delimiter=self.__delimiter)
