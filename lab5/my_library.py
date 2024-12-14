#part A
def task6_1(s1, s2):
    '''
    Задание:
    Даны две строки: S1 и S2. Определить количество вхождений строки S2 в строку S1.

    :param s1: первая строка
    :param s2: вторая строка
    :return counter: кол-во вхождений s2 в s1
    '''

    counter = s1.count(s2)
    return counter


#part B
def task6_2(text, word):
    '''
    Задание:
    Дан текст из слов, разделенных пробелами. Найти самое длинное слово
    фразы и проверить, можно ли из букв этого слова составить заданное слово.

    :param text: введенный текст
    :param word: заданное слово
    :return: None
    '''

    text_list = text.split()
    word_max_len = max(text_list)
    if word in word_max_len:
        print(f'Из {word_max_len} МОЖНО составить {word}')
    else:
        print(f'Из {word_max_len} НЕЛЬЗЯ составить {word}')

def task6_3(text, length):
    '''
    Задание:
    Из текста удалить все слова заданной длины, начинающиеся на согласную букву.
    :param text:
    :param length:
    :return:
    '''

    consonants = "бвгджзйклмнпрстфхцчшщ"
    words = text.lower().split()
    filtered_words = []

    for word in words:
        if len(word) != length or not(word[0] in consonants):
            filtered_words.append(word)
    result = ' '.join(filtered_words)
    return result


def task6_4(s):
    '''
    Задание:
    Дана строка, состоящая из русских слов, разделенных пробелами (одним или
    несколькими). Определить количество слов, которые a) начинаются и
    заканчиваются одной и той же буквой б) содержат хотя бы одну букву "а".
    :param s: вводимая строка
    :return counter: сколько слов начинаются и закачниваются на одну и ту же букву и содержат "а"
    '''
    s = s.split()
    counter = 0
    for word in s:
        if word[0] == word[-1] and 'а' in word:
            counter += 1
    return counter


#part C
def task6_5(date_input):
    '''
    Задание:
    Дата в формате YYYY-MM-DD или YY-MM-DD: Написать регулярное
    выражение, определяющее является ли данная строка датой в формате
    YYYY-MM-DD или YY-MM-DD.
    не используй функции

    :param date_input:
    :return: None
    '''
    import re

    date_pattern = r'^(?:\d{4}|\d{2})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$'

    if re.match(date_pattern, date_input):
        print("Строка соответствует формату даты.")
    else:
        print("Строка не соответствует формату даты.")

def task6_6(input_string):
    '''
    Задание:
    Строки, содержащие «cat» в качестве подстроки, игнорируйте регистр.
    Пример строк, которые подходят: «cat», «cat and cat», «Cat»,
    «theCATisHERE». Пример строк, которые не подходят: «kat», «», «cot»

    :param input_string:
    :return: None
    '''
    import re

    pattern = re.compile(r'cat', re.IGNORECASE)

    if pattern.search(input_string):
        print(f'Подходит: "{input_string}"')
    else:
        print(f'Не подходит: "{input_string}"')


def task6_7(text):
    '''
    Задание:
    Заменить первое вхождение слова, состоящего только из букв «a» (регистр
    не важен) на слово «argh». Примеры замен: «There’ll be no more
    "Aaaaaaaaaaaaaaa"» → «There’ll be no more "argh"».

    :param text: вводимый текст
    :return result: редактированный текст
    '''
    import re

    result = re.sub(r'\b[aA]+\b', 'argh', text, count=1)

    return result







