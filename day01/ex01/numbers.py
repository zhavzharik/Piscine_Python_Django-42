def read_display_numbers():
    with open('numbers.txt', 'r', encoding='utf-8') as f:
        contents = f.read().split(sep=',')
        for nb in contents:
            print(nb.replace('\n', ''))


if __name__ == '__main__':
    read_display_numbers()