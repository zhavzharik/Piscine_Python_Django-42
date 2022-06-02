import sys
import os
import re


def get_data_dict():
    k = []
    v = []
    with open('settings.py', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            data = line.split(sep='=')
            k.append(data[0].strip())
            v.append(data[1].strip().replace("\"", ''))
    my_dict = {x: y for x, y in zip(k, v)}
    return my_dict


def get_template():
    file_name = sys.argv[1]
    with open(file_name, 'r', encoding='utf-8') as f:
        template = ''.join(f.readlines())

    return template


def create_html(template: str, my_dict: dict, file_name_html):
    temp = sys.stdout
    sys.stdout = open(file_name_html, 'w', encoding='utf-8')
    print(template.format(title=my_dict["title"], body=my_dict["body"], name=my_dict["name"],
                          surname=my_dict["surname"], age=my_dict.get("age"),
                          profession=my_dict.get("profession")))
    sys.stdout.close()
    sys.stdout = temp


def convert_to_html():
    if len(sys.argv) != 2:
        return print("Wrong number of arguments!")
    file_name = sys.argv[1]
    if not re.compile(".*\.templates").match(file_name):
        return print("Wrong extension of file! It should be .templates")
    if not os.path.isfile(file_name):
        return print(f'There is no file {file_name}')
    my_dict = get_data_dict()
    template = get_template()
    file_name_html = "".join([file_name[0:re.compile("(\.templates)").search(file_name).start()], ".html"])
    create_html(template, my_dict, file_name_html)


if __name__ == '__main__':
    convert_to_html()
