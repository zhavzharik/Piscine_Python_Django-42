import sys


def find_capital(arg, states, capital_cities):
    answer = 'Unknown state'
    code = None
    for f, c in states.items():
        if f == arg:
            code = c
    if code:
        for f, c in capital_cities.items():
            if f == code:
                return c
    return answer


def display_capital():
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
        answer = find_capital(sys.argv[1], states, capital_cities)
        print(answer)


if __name__ == '__main__':
    display_capital()