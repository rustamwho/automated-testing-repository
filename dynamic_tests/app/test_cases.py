"""
Test_cases for dynamic testing of repository.


Name of each test case should be:
            TEST_CASE_module_ + <module_number> + _task_ + <task_number>
            e.g. "TEST_CASE_module_1_task_1" - test case for module 1 task 1
And the test case should be in this format:
            { <example_input> : <expected_output>, }
"""
TEST_CASE_module_1_task_1 = {
    1043: 'YES',
    1045: 'NO',
    2751: 'YES',
    2753: 'NO',
    3262: 'YES',
    3263: 'NO',
    3264: 'YES',
    9359: 'YES',
    9366: 'YES',
    9362: 'NO',
    9996: 'YES',
    9997: 'NO',
    9999: 'NO',
    987: 'NO',
    994: 'NO',
    7: 'NO',
    14: 'NO',
    17: 'NO',
    15: 'NO',
    18: 'NO',
    1057672: 'NO',
    594405: 'NO',
    83521: 'NO'
}

TEST_CASE_module_3_task_1 = {
    (3, 8): (11, -5, 24, 0.375, 0, 3, 32768.90100384814),
    (123, 2): (125, 121, 246, 61.5, 61, 1, 28153056843.0),
    (454, 322): (776, 132, 146188, 1.4099378881987579, 1,
                 132, 19595820067580.043),
    (0, 245): (245, -245, 0, 0.0, 0, 0, 882735153125.0),
    (1, 1000): (1001, -999, 1000, 0.001, 0, 1, 1000000000000000.0),
    (10, 2): (12, 8, 20, 5.0, 5, 0, 100000.00511999987),
    (34, 400): (434, -366, 13600, 0.085, 0, 34, 10240000000100.8),
    (87, 432): (519, -345, 37584, 0.2013888888888889,
                0, 87, 15045920331982.766)
}

TEST_CASE_module_4_task_1 = {
    (1, 'bwfusvfupdbftbs'): 'avetruetocaesar',
    (14, 'fsfftsfufksttskskt'): 'rerrfergrweffewewf',
    (25, 'jjjjjjj'): 'kkkkkkk'
}

TEST_CASE_module_4_task_2 = {
    'АааГГЦЦцТТттт': ('Аденин: 3', 'Гуанин: 2', 'Цитозин: 3', 'Тимин: 5'),
    'ааггццттААГГЦЦТТ': ('Аденин: 4', 'Гуанин: 4', 'Цитозин: 4', 'Тимин: 4'),
}

TEST_CASE_module_4_task_3 = {
    'abcdefg': 5,
    'abcdefgfhfabc': '5 9',
    'abcd': 'NO',
    'comfort': 3,
    'office': '1 2',
    'hello': 'NO',
    'fffffffffffffff': '0 14',
    'aaaaaaaaaaaaaaaaaaaaafaaaaaaaaaaaaaaaaaaaaaaaa': 21,
    'aaaaaaaaaaaaaaaaaaaaaaaaffaaaaaaaaaaaaaaaaaaaa': '24 25',
    'afafafafafafafa': '1 13',
}

TEST_CASE_module_6_task_1 = {
    10: 'палатка брезент удочка брюки пила карандаш спички'
}

TEST_CASE_module_6_task_2 = {
    '3 4': ('1  2  3  4', '5  6  7  8', '9  10 11 12'),
    '4 7': ('1  2  3  4  5  6  7', '8  9  10 11 12 13 14',
            '15 16 17 18 19 20 21', '22 23 24 25 26 27 28'),
    '6 6': ('1  2  3  4  5  6', '7  8  9  10 11 12', '13 14 15 16 17 18',
            '19 20 21 22 23 24', '25 26 27 28 29 30', '31 32 33 34 35 36'),
    '1 15': '1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 ',
    '9 1': (1, 2, 3, 4, 5, 6, 7, 8, 9),
    '2 2': ('1  2', '3  4'),
    '2 9': ('1  2  3  4  5  6  7  8  9', '10 11 12 13 14 15 16 17 18'),
    '5 2': ('1  2', '3  4', '5  6', '7  8', '9  10')
}

TEST_CASE_module_6_task_3 = {
    ('5', 'Язык Python прекрасен', 'C# - отличный язык программирования',
     'Stepik - отличная платформа', 'BEEGEEK FOREVER!',
     'язык Python появился 20 февраля 1991', '2', 'язык', 'python'): (
        'Язык Python прекрасен', 'язык Python появился 20 февраля 1991'),
    ('6', 'A caelo usque ad BEEGEEK centrum', 'A capillo usque ad ungues',
     'A capite ad calcem beegeek', 'Ab absurdo beegeeK',
     'Ab BEEGEEK equis ad asinos', 'Ab hoedis scindere oves', '1',
     'Beegeek'): (
        'A caelo usque ad BEEGEEK centrum', 'A capite ad calcem beegeek',
        'Ab absurdo beegeeK', 'Ab BEEGEEK equis ad asinos'),
    ('5', 'Язык Python прекрасен', 'C# - отличный язык программирования',
     'Stepik - отличная платформа', 'BEEGEEK FOREVER!',
     'язык Python появился 20 февраля 1991', '3', 'язык', 'python',
     'прекрасен'): 'Язык Python прекрасен'
}

TEST_CASE_module_6_task_4 = {
    ('a b c d e f', '2'): "[['a', 'b'], ['c', 'd'], ['e', 'f']]",
    ('a b c d e f', '3'): "[['a', 'b', 'c'], ['d', 'e', 'f']]",
    ('a b c', '1'): "[['a'], ['b'], ['c']]",
}

TEST_CASE_module_7_task_5 = {
    (114, 223): 'NO',
    (1523, 3678): 'YES',
    (5543, 3455): 'YES',
    (111234, 989897): 'NO',
    (7756, 15167): 'YES',
    (1234, 4321): 'YES',
    (1234, 5678): 'NO',
    (9754, 123): 'NO',
}
