import sys
import requests
from bs4 import BeautifulSoup


class RoadToPhilosophy:
    def __init__(self) -> None:
        self.prev = []

    def search_wiki(self, path):
        url = f'https://en.wikipedia.org{path}'
        try:
            r = requests.get(url)
            r.raise_for_status()
        except requests.HTTPError as e:
            if r.status_code == requests.codes.ok:
                return print("It's a dead end !")
            return print(e)
        soup = BeautifulSoup(r.text, 'html.parser')
        title = soup.find(id='firstHeading').text
        if title in self.prev:
            return print("It leads to an infinite loop !")
        self.prev.append(title)
        print(title)
        if title == 'Philosophy':
            return print("{} roads from {} to Philosophy".format(len(self.prev), self.prev[0] if len(self.prev) > 0 else 'Philosophy'))
        content = soup.find(id='mw-content-text')
        all_links = content.select('p > a')
        for link in all_links:
            if link.get('href') is not None and link['href'].startswith('/wiki/')\
                    and not link['href'].startswith('/wiki/Wikipedia:') and not link['href'].startswith('/wiki/Help:'):
                return self.search_wiki(link['href'])
        return print("It leads to a dead end !.")


def check_argv_search_wiki():
    if len(sys.argv) != 2:
        print("The program takes 1 string argument!")
    else:
        result = RoadToPhilosophy()
        result.search_wiki('/wiki/'+sys.argv[1])


if __name__ == '__main__':
    check_argv_search_wiki()