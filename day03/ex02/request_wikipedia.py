import requests
import json
import dewiki
import sys


def read_wiki(arg):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "parse",
        "page": arg,
        "prop": "wikitext",
        "format": "json",
        "redirects": "true",
    }
    try:
        r = requests.get(url, params)
        r.raise_for_status()
    except requests.HTTPError as e:
        raise e
    try:
        data = json.loads(r.text)
    except json.decoder.JSONDecodeError as e:
        raise e
    if data.get("error") is not None:
        raise Exception(data["error"]["info"])
    result = dewiki.from_string(data["parse"]["wikitext"]["*"])
    return result


def check_argv_write_file():
    if len(sys.argv) != 2:
        print("The program takes 1 string argument!")
    else:
        try:
            result = read_wiki(sys.argv[1])
        except Exception as e:
            print(e)
        try:
            with open("{}.wiki".format(sys.argv[1]), 'w', encoding='utf-8') as f:
                f.write(result)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    check_argv_write_file()
