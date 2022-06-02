from elem import Elem, Text


class Html(Elem):
    def __init__(self, content=None, attr={}, tag_type='double'):
        super().__init__(tag='html', content=content, attr=attr, tag_type=tag_type)


class Head(Elem):
    def __init__(self, content=None, attr={}, tag_type='double'):
        super().__init__(tag='head', content=content, attr=attr, tag_type=tag_type)


class Body(Elem):
    def __init__(self, content=None, attr={}, tag_type='double'):
        super().__init__(tag='body', content=content, attr=attr, tag_type=tag_type)


class Title(Elem):
    def __init__(self, content=None, attr={}, tag_type='double'):
        super().__init__(tag='title', content=content, attr=attr, tag_type=tag_type)


class Meta(Elem):
    def __init__(self, content=None, attr={}, tag_type='double'):
        super().__init__(tag='meta', content=content, attr=attr, tag_type=tag_type)


class Img(Elem):
    def __init__(self, content=None, attr={}, tag_type='double'):
        super().__init__(tag='img', content=content, attr=attr, tag_type=tag_type)


class Table(Elem):
    def __init__(self, content=None, attr={}, tag_type='double'):
        super().__init__(tag='table', content=content, attr=attr, tag_type=tag_type)


class Th(Elem):
    def __init__(self, content=None, attr={}, tag_type='double'):
        super().__init__(tag='th', content=content, attr=attr, tag_type=tag_type)


class Tr(Elem):
    def __init__(self, content=None, attr={}, tag_type='double'):
        super().__init__(tag='tr', content=content, attr=attr, tag_type=tag_type)


class Td(Elem):
    def __init__(self, content=None, attr={}, tag_type='double'):
        super().__init__(tag='td', content=content, attr=attr, tag_type=tag_type)


class Ul(Elem):
    def __init__(self, content=None, attr={}, tag_type='double'):
        super().__init__(tag='ul', content=content, attr=attr, tag_type=tag_type)


class Ol(Elem):
    def __init__(self, content=None, attr={}, tag_type='double'):
        super().__init__(tag='ol', content=content, attr=attr, tag_type=tag_type)


class Li(Elem):
    def __init__(self, content=None, attr={}, tag_type='double'):
        super().__init__(tag='li', content=content, attr=attr, tag_type=tag_type)


class H1(Elem):
    def __init__(self, content=None, attr={}, tag_type='double'):
        super().__init__(tag='h1', content=content, attr=attr, tag_type=tag_type)


class H2(Elem):
    def __init__(self, content=None, attr={}, tag_type='double'):
        super().__init__(tag='h2', content=content, attr=attr, tag_type=tag_type)


class P(Elem):
    def __init__(self, content=None, attr={}, tag_type='double'):
        super().__init__(tag='p', content=content, attr=attr, tag_type=tag_type)


class Div(Elem):
    def __init__(self, content=None, attr={}, tag_type='double'):
        super().__init__(content=content, attr=attr, tag_type=tag_type)


class Span(Elem):
    def __init__(self, content=None, attr={}, tag_type='double'):
        super().__init__(tag='span', content=content, attr=attr, tag_type=tag_type)


class Hr(Elem):
    def __init__(self, content=None, attr={}, tag_type='double'):
        super().__init__(tag='hr', content=content, attr=attr, tag_type=tag_type)


class Br(Elem):
    def __init__(self, content=None, attr={}, tag_type='double'):
        super().__init__(tag='br', content=content, attr=attr, tag_type=tag_type)


def test():
    print('*' * 39)
    print("Test 1:")
    print('*' * 39)
    document = Html([Head(Title(Text('"Hello ground!"'))), Body(
        [H1(Text('"Oh no, not again!"')), Img(attr={'src': 'http://i.imgur.com/pfp3T.jpg'}, tag_type='simple')])])
    print(document)
    print('*' * 39)
    print("Test 2:")
    print('*' * 39)
    print(Html([Head(), Body()]))
    print('*' * 39)
    print("Test 3:")
    print('*' * 39)
    print(Html([Head([Meta(attr={'charset': "UTF-8"}, tag_type='simple'), Title(Text("Test"))]),
                Body(Table([H1(), Tr([Td(Ul([Li(), Li(), Li(), Li()])), Td(), Td()]), Tr([Td(Ol([Li(), Li(), Li(), Li()])), Td(), Td()])]))]))


if __name__ == '__main__':
    test()
