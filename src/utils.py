import json


def get_file(pth):
    """ Функция считывающая данные из файла operations.json """
    with open(pth, encoding='utf-8') as file:
        data_file_json = json.load(file)
    return data_file_json


def get_operation_list(dic):
    """ Фильтрующая функция"""
    list_of_filtered_dates = list(filter(lambda x: x.get('date'), dic))
    list_of_completed_operations = list(filter(lambda e: e['state'] == 'EXECUTED', list_of_filtered_dates))
    the_list_of_completed_operations_is_sorted_by_date = sorted(list_of_completed_operations, key=lambda d: d['date'],
                                                                reverse=True)
    return the_list_of_completed_operations_is_sorted_by_date


def get_first_line(data_from_file: dict):
    """ Функция, выводящая первую строку в программе """
    date_operations = data_from_file['date']
    date_highlighting = date_operations.find('T')
    date_format = date_operations[:date_highlighting].split('-')
    text = data_from_file['description']
    desired_date_format = date_format[-1] + '.' + date_format[-2] + '.' + date_format[-3] + ' ' + text
    return desired_date_format


def get_second_line(data_from_file: dict):
    """ Функция, выводящая вторую строку в программе """
    value_from = data_from_file.get('from')
    value_to = data_from_file.get('to')

    def card_and_account_number(text: str):
        text_split = text.split(' ')
        reversed_list = text_split[-1]
        format_numbers = reversed_list[0:4] + ' ' + reversed_list[4:6] + '** **** ' + reversed_list[-4:]
        return ' '.join(text_split[:-1]) + ' ' + format_numbers

    if value_from is None and value_to[0:2] == 'Сч':
        return '-> ' + value_to[:4] + ' ' + value_to[-4:].rjust(6, '*')
    elif value_from is None:
        return '-> ' + card_and_account_number(value_to)
    elif value_from.startswith('Сч') and value_to[:2] != 'Сч':
        agent = value_from[:4] + ' ' + value_from[-4:].rjust(6, '*')
        return agent + ' -> ' + card_and_account_number(value_to)
    elif value_to.startswith('Сч') and value_from[:2] != 'Сч':
        accaunt = value_to[0:4] + ' ' + value_to[-4:].rjust(6, '*')
        return card_and_account_number(value_from) + ' -> ' + accaunt
    elif value_to.startswith('Сч') and value_from.startswith('Сч'):
        agent = value_from[:4] + ' ' + value_from[-4:].rjust(6, '*')
        accaunt = value_to[0:4] + ' ' + value_to[-4:].rjust(6, '*')
        return agent + ' -> ' + accaunt
    else:
        return card_and_account_number(value_from) + ' -> ' + card_and_account_number(value_to)


def get_third_line(data_from_file: dict):
    """ Функция, выводящая третью строку в программе """
    operation_amount = data_from_file['operationAmount']
    transfer_amount = operation_amount['amount']
    currency = operation_amount['currency']['name']
    return transfer_amount + ' ' + currency + '.'
