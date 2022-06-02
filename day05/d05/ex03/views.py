from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import psycopg2


def populate(request):
    try:
        conn = psycopg2.connect(database=settings.DATABASES['default']['NAME'],
                                user=settings.DATABASES['default']['USER'],
                                password=settings.DATABASES['default']['PASSWORD'],
                                host=settings.DATABASES['default']['HOST'],
                                port=settings.DATABASES['default']['PORT'])
        movies = [
            {
                'episode_nb': 1,
                'title': 'The Phantom Menace',
                'director': 'George Lucas',
                'producer': 'Rick McCallum',
                'release_date': '1999-05-19'
            },
            {
                'episode_nb': 2,
                'title': 'Attack of the Clones',
                'director': 'George Lucas',
                'producer': 'Rick McCallum',
                'release_date': '2002-05-16'
            },
            {
                'episode_nb': 3,
                'title': 'Revenge of the Sith',
                'director': 'George Lucas',
                'producer': 'Rick McCallum',
                'release_date': '2005-05-19'
            },
            {
                'episode_nb': 4,
                'title': 'A New Hope',
                'director': 'George Lucas',
                'producer': 'Gary Kurtz, Rick McCallum',
                'release_date': '1977-05-25'
            },
            {
                'episode_nb': 5,
                'title': 'The Empire Strikes Back',
                'director': 'Irvin Kershner',
                'producer': 'Gary Kurtz, Rick McCallum',
                'release_date': '1980-05-17'
            },
            {
                'episode_nb': 6,
                'title': 'Return of the Jedi',
                'director': 'Richard Marquand',
                'producer': 'Howard G. Kazanjian, George Lucas, Rick McCallum',
                'release_date': '1983-05-25'
            },
            {
                'episode_nb': 7,
                'title': 'The Force Awakens',
                'director': 'J. J. Abrams',
                'producer': 'Kathleen Kennedy, J. J. Abrams, Bryan Burk',
                'release_date': '2015-12-11'
            }
        ]
        answer = []
        with conn.cursor() as cur:
            for movie in movies:
                try:
                    cur.execute("""INSERT INTO ex03_movies(episode_nb, title, director, producer, release_date) 
                                    VALUES (%s, %s, %s, %s, %s);""",
                                [movie['episode_nb'], movie['title'], movie['director'], movie['producer'], movie['release_date']])
                    answer.append("OK")
                    conn.commit()
                except psycopg2.DatabaseError as e:
                    conn.rollback()
                    answer.append(e)
        return HttpResponse("<br/>".join(str(i) for i in answer))
    except Exception as e:
        return HttpResponse(e)


def display(request):
    try:
        conn = psycopg2.connect(database=settings.DATABASES['default']['NAME'],
                                user=settings.DATABASES['default']['USER'],
                                password=settings.DATABASES['default']['PASSWORD'],
                                host=settings.DATABASES['default']['HOST'],
                                port=settings.DATABASES['default']['PORT'])
        with conn.cursor() as cur:
            cur.execute("""SELECT * FROM ex03_movies;""")
            movies = cur.fetchall()
        return render(request, 'ex03/display.html', {'movies': movies})
    except Exception as e:
        return HttpResponse("No data available")
