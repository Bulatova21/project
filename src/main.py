from os import path
import utils

PATH = path.join('..', 'operations.json')
lst = utils.get_file(PATH)
operation_list = utils.get_operation_list(lst)

for item in operation_list[:5]:
    print(utils.get_first_line(item))
    print(utils.get_second_line(item))
    print(utils.get_third_line(item))
