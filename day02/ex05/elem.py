#!/usr/bin/python3


class Text(str):
    def __str__(self):
        return super().__str__().replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace('\n', '\n<br />\n')


class Elem:
    class ValidationError(Exception):
        def __init__(self):
            self.message = "incorrect behaviour"
            super().__init__(self.message)

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        self.tag = tag
        self.attr = attr
        self.content = []
        if not (self.check_type(content) or content is None):
            raise self.ValidationError
        if type(content) == list:
            self.content = content
        elif content is not None:
            self.content.append(content)
        if tag_type != 'double' and tag_type != 'simple':
            raise self.ValidationError
        self.tag_type = tag_type

    def __str__(self):
        if self.tag_type == 'double':
            result = f'<{self.tag}{self.__make_attr()}>{self.__make_content()}</{self.tag}>'
        elif self.tag_type == 'simple':
            result = f'<{self.tag}{self.__make_attr()} />'
        return result

    def __make_attr(self):
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        if len(self.content) == 0:
            return ''
        result = '\n'
        for elem in self.content:
            if (len(str(elem)) != 0):
                result += f'{elem}\n'
        result = '  '.join([line for line in result.splitlines(True)])
        if len(result.strip()) == 0:
            return ''
        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))


def test():
    document = Elem(tag='html', content=[Elem(tag='head', content=Elem(tag='title', content=Text('"Hello ground!"'))),
                                     Elem(tag='body', content=[Elem(tag='h1', content=Text('"Oh no, not again!"')),
                                                               Elem(tag='img', attr={'src': 'http://i.imgur.com/pfp3T.jpg'}, tag_type='simple')])])
    print(document)


if __name__ == '__main__':
    test()
