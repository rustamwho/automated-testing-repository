import re

import cdmpyparser


def get_module_info(file) -> cdmpyparser.BriefModuleInfo:
    c = cdmpyparser.getBriefModuleInfoFromFile(file)
    return c


def get_all_variables(file_name) -> set:
    # ^\s* - строка начинается с 0 или более пробелов
    # (\w+) - один или более буква, а также цифры и _
    # после знака равно любые символы
    pattern = r'^\s*(?P<variable>\w+) = .+'
    variables = set()
    with open(file_name, 'r') as file:
        for line in file.readlines():
            match = re.search(pattern, line)
            if match:
                variables.add(match.group('variable'))
    return variables


def get_class_functions_decorators(file_name) -> set:
    """
    Return decorators of methods inside classes.
    """
    decorators = set()
    c = get_module_info(file_name)
    for cls in c.classes:
        for func in cls.functions:
            for dec in func.decorators:
                decorators.add(dec.name)
    return decorators


def is_using_abstractmethod(file_list: list) -> bool:
    """ Return True if abstractmethod is exists in any file. """
    for file in file_list:
        decorators = get_class_functions_decorators(file)
        if 'abstractmethod' in decorators:
            return True
    return False


def get_classes_with_base(file_name) -> set:
    """ Return classes with parent class. """
    classes = set()
    c = get_module_info(file_name)
    for cls in c.classes:
        if cls.base:
            classes.add(cls.name)
    return classes


def is_using_inheritance(file_list: list) -> bool:
    """ Return True if inheritance class is exists in any file. """
    for file in file_list:
        if get_classes_with_base(file):
            return True
    return False


def get_classes_attributes(file_name) -> set:
    """ Return attributes of each class in file. """
    attributes = set()
    c = get_module_info(file_name)
    for cls in c.classes:
        for attr in cls.instanceAttributes:
            attributes.add(attr.name)
    return attributes


def is_using_private_attributes(file_list: list) -> bool:
    for file in file_list:
        attributes = get_classes_attributes(file)
        if attributes:
            if any([attr.startswith('_') for attr in attributes]):
                return True
    return False


def is_using_self(file_list: list) -> bool:
    """ Return True if any method in class using self argument. """
    for file in file_list:
        c = get_module_info(file)
        for cls in c.classes:
            for func in cls.functions:
                if 'self' in [k.name for k in func.arguments]:
                    return True
    return False


def is_using_constructors(file_list: list) -> bool:
    """ Return True if '__init__' function is exists in any file. """
    for file in file_list:
        module_info = get_module_info(file)
        if '__init__' in [func.name for cls in module_info.classes
                          for func in cls.functions]:
            return True
    return False


def is_using_classes(file_list: list) -> bool:
    """ Return True if class is exists in any file. """
    for file in file_list:
        module_info = get_module_info(file)
        if module_info.classes:
            return True
    return False


def is_using_methods(file_list: list) -> bool:
    """ Return True if class method is exists in any file. """
    for file in file_list:
        module_info = get_module_info(file)
        if [meth for cls in module_info.classes for meth in cls.functions]:
            return True
    return False
