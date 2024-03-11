import json

""" Функция считывающая данные из файла operations.json """
def get_file(pth):
    with open(pth, encoding='utf-8') as file:
        lst = json.load(file)
    return lst

""" Фильтрующая функция"""
def get_operation_list(dic: list):
    dic_filtred = list(filter(lambda x: x.get('date'), dic))
    filtred_list = list(filter(lambda e: e['state'] == 'EXECUTED', dic_filtred))
    lst = sorted(filtred_list, key=lambda d: d['date'], reverse=True)
    return lst


""" Функция, выводящая первую строку в программе """
def get_first_line(col: dict):
    s = col['date']
    ind = s.find('T')
    lst = s[:ind].split('-')
    text = col['description']
    line = lst[-1] + '.' + lst[-2] + '.' + lst[-3] + ' ' + text
    return line

""" Функция, выводящая вторую строку в программе """
def get_second_line(col: dict):
    s1 = col.get('from')
    s2 = col.get('to')

    def form_line(text: str):
        lst = text.split(' ')
        num = lst[-1]
        f_num = num[0:4] + ' ' + num[4:6] + '** **** ' + num[-4:]
        return ' '.join(lst[:-1]) + ' ' + f_num

    if s1 is None and s2[0:2] == 'Сч':
        return '-> ' + s2[:4] + ' ' + s2[-4:].rjust(6, '*')
    elif s1 is None:
        return '-> ' + form_line(s2)
    elif s1.startswith('Сч') and s2[:2] != 'Сч':
        agent = s1[:4] + ' ' + s1[-4:].rjust(6, '*')
        return agent + ' -> ' + form_line(s2)
    elif s2.startswith('Сч') and s1[:2] != 'Сч':
        accaunt = s2[0:4] + ' ' + s2[-4:].rjust(6, '*')
        return form_line(s1) + ' -> ' + accaunt
    elif s2.startswith('Сч') and s1.startswith('Сч'):
        agent = s1[:4] + ' ' + s1[-4:].rjust(6, '*')
        accaunt = s2[0:4] + ' ' + s2[-4:].rjust(6, '*')
        return agent + ' -> ' + accaunt
    else:
        return form_line(s1) + ' -> ' + form_line(s2)

""" Функция, выводящая третью строку в программе """
def get_third_line(col: dict):
    am_col = col['operationAmount']
    summ = am_col['amount']
    currency = am_col['currency']['name']
    return summ + ' ' + currency + '.'
