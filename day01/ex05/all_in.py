import sys


def find_capital(arg, states, capital_cities):
    answer = 'Unknown'
    code = None
    for f, c in states.items():
        if f == arg:
            code = c
    if code:
        for f, c in capital_cities.items():
            if f == code:
                return c
    return answer


def find_state(arg, states, capital_cities):
    answer = 'Unknown'
    code = None
    for f, c in capital_cities.items():
        if c == arg:
            code = f
    if code:
        for f, c in states.items():
            if c == code:
                return f
    return answer


def get_list():
    new_list = []
    data = sys.argv[1].split(sep=',')
    for item in data:
        if len(item.strip()) != 0:
            new_list.append(item.strip())
    return new_list


def display_info(new_list, states, capital_cities):
    for item in new_list:
        capital = find_capital(item.lower().title(), states, capital_cities)
        state = find_state(item.lower().title(), states, capital_cities)
        if capital == 'Unknown' and state == 'Unknown':
            print(f'{item} is neither a capital city nor a state')
        elif capital != 'Unknown':
            print(f'{capital} is the capital of {item.lower().title()}')
        elif state != 'Unknown':
            print(f'{item.lower().title()} is the capital of {state}')


def display_all():
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    if len(sys.argv) == 2:
        new_list = get_list()
        display_info(new_list, states, capital_cities)


if __name__ == '__main__':
    display_all()