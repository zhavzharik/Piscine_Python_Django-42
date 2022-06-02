def split_year_name(d):
    year = []
    name = []
    for info in d:
        year.append(info[1])
        name.append(info[0])
    return year, name


def create_dict(d):
    year, name = split_year_name(d)
    my_dict = {}
    for f, c in zip(year, name):
        my_dict[f] = " ".join([my_dict.get(f, ""), c]).strip()
    return my_dict


def display_dict():
    d = [
        ('Hendrix', '1942'),
        ('Allman', '1946'),
        ('King', '1925'),
        ('Clapton', '1945'),
        ('Johnson', '1911'),
        ('Berry', '1926'),
        ('Vaughan', '1954'),
        ('Cooder', '1947'),
        ('Page', '1944'),
        ('Richards', '1943'),
        ('Hammett', '1962'),
        ('Cobain', '1967'),
        ('Garcia', '1942'),
        ('Beck', '1944'),
        ('Santana', '1947'),
        ('Ramone', '1948'),
        ('White', '1975'),
        ('Frusciante', '1970'),
        ('Thompson', '1949'),
        ('Burton', '1939')
    ]
    my_dict = create_dict(d)
    for f, c in my_dict.items():
        print(f'{f} : {c}')


if __name__ == '__main__':
    display_dict()
