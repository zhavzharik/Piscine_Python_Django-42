from django.http import HttpResponse
from django.conf import settings
import psycopg2


def home(request):
    return HttpResponse("Piscine Django day05.")


def init(request):
    try:
        conn = psycopg2.connect(database=settings.DATABASES['default']['NAME'],
                                user=settings.DATABASES['default']['USER'],
                                password=settings.DATABASES['default']['PASSWORD'],
                                host=settings.DATABASES['default']['HOST'],
                                port=settings.DATABASES['default']['PORT'])
        with conn.cursor() as cur:
            cur.execute("""CREATE TABLE IF NOT EXISTS ex00_movies(
                title VARCHAR (64) UNIQUE NOT NULL,
                episode_nb INT PRIMARY KEY,
                opening_crawl TEXT,
                director VARCHAR (32) NOT NULL,
                producer VARCHAR (128) NOT NULL,
                release_date DATE NOT NULL);""")
            cur.execute('commit')
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(e)
