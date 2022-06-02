import sys


def find_state(arg, states, capital_cities):
    answer = 'Unknown capital city'
    code = None
    for f, c in capital_cities.items():
        if c == arg:
            code = f
    if code:
        for f, c in states.items():
            if c == code:
                return f
    return answer


def display_state():
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
        answer = find_state(sys.argv[1], states, capital_cities)
        print(answer)


if __name__ == '__main__':
    display_state()