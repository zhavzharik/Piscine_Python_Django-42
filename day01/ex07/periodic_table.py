import sys


def write_head():
    print('<!DOCTYPE html>\n<html lang="en">\n<head>\n\t<meta charset="UTF-8">')
    print('\t<meta http-equiv="X-UA-Compatible" content="IE=edge">')
    print('\t<meta name="viewport" content="width=device-width, initial-scale=1.0">')
    print('\t<title>Periodic Table</title>')
    print('\t<style>\n\t\ttable {\n\t\t\tfont-family: Verdana;\n\t\t}')
    print('\t\th4 {\n\t\t\ttext-align: center;\n\t\t}')
    print('\t\tul {\n\t\t\tlist-style:none;\n\t\t\tpadding-left:0px;\n\t\t\tfont-size:60%;\n\t\t}')
    print('\t</style>\n</head>\n<body>\n\t<table>')


def write_end():
    print('\t</table>\n</body>\n</html>')


def read_periodic_table():
    name = []
    position = []
    number = []
    small = []
    molar = []
    electron = []
    with open('periodic_table.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            data = line.split(sep=',')
            name.append(data[0].partition(' = ')[0])
            position.append(int(data[0].partition(':')[2]))
            number.append(data[1].partition(':')[2])
            small.append(data[2].partition(': ')[2])
            molar.append(data[3].partition(':')[2])
            electron.append(data[4].replace('\n', '').partition(':')[2])
    return name, position, number, small, molar, electron


def create_html_file():
    name, position, number, small, molar, electron = read_periodic_table()
    temp = sys.stdout
    sys.stdout = open('periodic_table.html', 'w', encoding='utf-8')
    write_head()
    for i in range(len(name)):
        if position[i] == 0:
            print('\t\t<tr>')
        if i > 0 and position[i] - position[i-1] != 1:
            count = position[i] - position[i-1]
            n = ''.join(['\t\t\t<td></td>\n' for s in range(count - 1)])
            print(n)
        print('\t\t\t<td style="border: 1px solid black; padding:10px">')
        print(f'\t\t\t\t<h4>{name[i]}</h4>')
        print('\t\t\t\t\t<ul>')
        print(f'\t\t\t\t\t\t<li>No {number[i]}</li>')
        print(f'\t\t\t\t\t\t<li>{small[i]}</li>')
        print(f'\t\t\t\t\t\t<li>{molar[i]}</li>')
        if name[i] == 'Hydrogen':
            print(f'\t\t\t\t\t\t<li>{electron[i]} electron</li>')
        else:
            print(f'\t\t\t\t\t\t<li>{electron[i]} electrons</li>')
        print('\t\t\t\t\t</ul>')
        print('\t\t\t</td>')
        if position[i] == 17:
            print('\t\t</tr>')
    write_end()
    sys.stdout.close()
    sys.stdout = temp


if __name__ == '__main__':
    create_html_file()