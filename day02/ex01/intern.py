class Intern:
    def __init__(self, Name=None):
        self.Name = "My name? I’m nobody, an intern, I have no name." if Name is None else Name

    def __str__(self):
        return self.Name

    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."

    def work(self):
        raise Exception('I’m just an intern, I can’t do that...')

    def make_coffee(self):
        return self.Coffee()


def test():
    intern = Intern()
    print(intern)
    mark = Intern("Mark")
    print(mark)
    print(mark.make_coffee())
    try:
        intern.work()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    test()
