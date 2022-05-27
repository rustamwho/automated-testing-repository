import os
import sys
import importlib

from tester_with_running import TestResult
from logger_utils import get_logger

logger = get_logger(__name__)


def with_custom_dir_and_python_path(func):
    """
    Decorator for setting current directory and PYTHONPATH before running
    testing and after.
    """

    def wrapper(base_dir, *args, **kwargs):
        # Save cwd for future recovering
        cwd = os.getcwd()
        # Set current directory to dir with solutions
        os.chdir(base_dir)
        # Add solutions dir to PYTHONPATH
        sys.path.append(base_dir)

        res = func(base_dir, *args, **kwargs)

        # Recover all settings
        sys.path.remove(base_dir)
        os.chdir(cwd)

        return res

    return wrapper


def reload_module(module_name: str) -> None:
    """
    Importing or Re-importing module and its parent modules.
    I.e. for the case 'from foo.bar import hello' need to reloading 'foo.bar'
    and 'foo'. And after call main importing.

    :param module_name: full module name with parents.
    :return: if module is not exists, raise ImportError. Else None.
    """
    if '.' in module_name:
        parent = module_name.split('.')[0]
        reload_module(parent)

    if module_name in sys.modules:
        del sys.modules[module_name]

    importlib.import_module(module_name)


@with_custom_dir_and_python_path
def testing_module_10_task_1(base_dir: str) -> list[TestResult]:
    try:
        reload_module('module_10.task_1_mean_function')
        from module_10.task_1_mean_function import mean
    except ImportError:
        return [TestResult(0, False, 'Import error')]

    results = []
    if mean() != 0.0:
        results.append(TestResult(0, False, 'WRONG ANSWER'))
    else:
        results.append(TestResult(0, True, 'ACCESS'))

    if mean(7) != 7.0:
        results.append(TestResult(1, False, 'WRONG ANSWER'))
    else:
        results.append(TestResult(1, True, 'ACCESS'))

    if mean(1.5, True, ['джфыщкпл'], 'beegeek', 2.5, (1, 2)) != 2.0:
        results.append(TestResult(2, False, 'WRONG ANSWER'))
    else:
        results.append(TestResult(2, True, 'ACCESS'))

    if mean(True, ['stop'], 'beegeek', (1, 2)) != 0.0:
        results.append(TestResult(3, False, 'WRONG ANSWER'))
    else:
        results.append(TestResult(3, True, 'ACCESS'))

    if mean(-1, 2, 3, 10, ('5')) != 3.5:
        results.append(TestResult(4, False, 'WRONG ANSWER'))
    else:
        results.append(TestResult(4, True, 'ACCESS'))

    return results


@with_custom_dir_and_python_path
def testing_module_10_task_2(base_dir: str) -> list[TestResult]:
    try:
        reload_module('module_10.task_2_filling_matrix')
        from module_10.task_2_filling_matrix import matrix
    except ImportError:
        return [TestResult(0, False, 'Import error')]

    results = []
    if matrix() != [[0]]:
        results.append(TestResult(0, False, 'WRONG ANSWER'))
    else:
        results.append(TestResult(0, True, 'ACCESS'))

    if matrix(3) != [[0, 0, 0], [0, 0, 0], [0, 0, 0]]:
        results.append(TestResult(1, False, 'WRONG ANSWER'))
    else:
        results.append(TestResult(1, True, 'ACCESS'))

    if matrix(2, 5) != [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]:
        results.append(TestResult(2, False, 'WRONG ANSWER'))
    else:
        results.append(TestResult(2, True, 'ACCESS'))

    if matrix(3, 4, 9) != [[9, 9, 9, 9], [9, 9, 9, 9], [9, 9, 9, 9]]:
        results.append(TestResult(3, False, 'WRONG ANSWER'))
    else:
        results.append(TestResult(3, True, 'ACCESS'))

    return results


@with_custom_dir_and_python_path
def testing_module_10_task_4(base_dir: str) -> list[TestResult]:
    try:
        reload_module('module_10.task_4_info_kwargs_function')
        from module_10.task_4_info_kwargs_function import info_kwargs
    except ImportError:
        return [TestResult(0, False, 'Import error')]

    output = info_kwargs(first_name='Timur', last_name='Guev', age=28,
                         job='teacher')
    expected = 'age: 28\nfirst_name: Timur\njob: teacher\nlast_name: Guev'

    results = []
    if output.strip() != expected:
        results.append(TestResult(0, False, 'WRONG ANSWER'))
    else:
        results.append(TestResult(0, True, 'ACCESS'))

    return results


@with_custom_dir_and_python_path
def testing_module_10_task_8(base_dir: str) -> list[TestResult]:
    try:
        reload_module('module_10.task_8_negative_non_negative')
        from module_10.task_8_negative_non_negative import is_non_negative_num
    except ImportError:
        return [TestResult(0, False, 'Import error')]

    results = []
    if is_non_negative_num('10.34ab') != False:
        results.append(TestResult(0, False, 'WRONG ANSWER'))
    else:
        results.append(TestResult(0, True, 'ACCESS'))

    if is_non_negative_num('10.45') != True:
        results.append(TestResult(1, False, 'WRONG ANSWER'))
    else:
        results.append(TestResult(1, True, 'ACCESS'))

    if is_non_negative_num('-18') != False:
        results.append(TestResult(2, False, 'WRONG ANSWER'))
    else:
        results.append(TestResult(2, True, 'ACCESS'))

    if is_non_negative_num('123.122.12') != False:
        results.append(TestResult(3, False, 'WRONG ANSWER'))
    else:
        results.append(TestResult(3, True, 'ACCESS'))

    if is_non_negative_num('987') != True:
        results.append(TestResult(4, False, 'WRONG ANSWER'))
    else:
        results.append(TestResult(4, True, 'ACCESS'))

    return results


@with_custom_dir_and_python_path
def testing_module_13_task_2(base_dir: str) -> list[TestResult]:
    try:
        from task_2_classes import Country, Republic
    except ImportError:
        return [TestResult(0, False, 'Import error')]

    print(Country.__dict__)
    print(Country in Republic.__bases__)
