import re


def is_exists_overload_arithmetic(file_name: str, operator: str) -> bool:
    """
    Search overloading arithmetic operators.

    :param file_name: str of the file for matching
    :param operator: operator
    :return: True if find, else - False
    """
    # ^\s* - строка начинается с 0 или более пробелов
    # def __truediv__ (self, other): - перегрузка
    pattern = fr'^\s*def {operator}\(self, other\):\s*$'
    with open(file_name, 'r') as file:
        match = re.findall(pattern, file.read(), flags=re.MULTILINE)
        if match:
            return True
    return False


def is_exists_pattern(file_name: str, pattern: str) -> bool:
    """
    Search pattern in file.
    Final pattern for matching: fr'^\s*\w+\s*\{pattern}\s*\w+'.

    :param file_name: str of the file for matching
    :param pattern: pattern for searching
    :return: True if pattern is exists in file, else - False
    """
    # ^\s* - строка начинается с 0 или более пробелов
    # \w+ - любой символ, котороый может быть переменной (буквы, цифры и _)
    pattern = fr'^\s*\w+\s*\{pattern}\s*\w+'
    with open(file_name, 'r') as file:
        match = re.findall(pattern, file.read(), flags=re.MULTILINE)
        if match:
            return True
    return False


def is_exist_multiple_logical_ops_in_one_expression(file_name: str) -> bool:
    """
    Search using multiple logical operations in one expression in <file_name>.

    :param file_name: str of the file for matching
    :return: True if multiple logical operations in one expression are exist,
    else - False
    """
    # ^[^#\'\"\n]* - строка начинается с любого символа кроме этих
    # (?:or|and|not|>|<|>=|<=|!=|==) - комбинация из двух операторов
    # (между ними любые символы кроме переноса строки .+)
    pattern = (r'^[^#\'\"\n]*(?:or|and|not|>|<|>=|<=|!=|==).+'
               r'(?:or|and|not|>|<|>=|<=|!=|==)[^\'\"\n]+$')
    with open(file_name, 'r') as file:
        match = re.findall(pattern, file.read(), flags=re.MULTILINE)
        if match:
            return True
    return False
