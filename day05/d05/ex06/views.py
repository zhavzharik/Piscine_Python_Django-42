from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings
import psycopg2
from django.http import HttpResponse
from .forms import RemoveForm, UpdateForm


class Init(View):
    TABLE_NAME = "ex06_movies"
    conn = psycopg2.connect(database=settings.DATABASES['default']['NAME'],
                            user=settings.DATABASES['default']['USER'],
                            password=settings.DATABASES['default']['PASSWORD'],
                            host=settings.DATABASES['default']['HOST'],
                            port=settings.DATABASES['default']['PORT'])

    def get(self, request):
        try:
            with self.conn.cursor() as cur:
                cur.execute(f"""CREATE TABLE {self.TABLE_NAME}(
                    title VARCHAR (64) UNIQUE NOT NULL,
                    episode_nb INT PRIMARY KEY,
                    opening_crawl TEXT,
                    director VARCHAR (32) NOT NULL,
                    producer VARCHAR (128) NOT NULL,
                    release_date DATE NOT NULL,
                    created TIMESTAMP NOT NULL DEFAULT NOW(),
                    updated TIMESTAMP NOT NULL DEFAULT NOW());
                    CREATE OR REPLACE FUNCTION update_changetimestamp_column()
                    RETURNS TRIGGER AS $$
                    BEGIN
                    NEW.updated = now();
                    NEW.created = OLD.created;
                    RETURN NEW;
                    END;
                    $$ language 'plpgsql';
                    CREATE TRIGGER update_films_changetimestamp BEFORE UPDATE
                    ON ex06_movies FOR EACH ROW EXECUTE PROCEDURE
                    update_changetimestamp_column();""")
            self.conn.commit()
        except Exception as e:
            return HttpResponse(e)
        return HttpResponse("OK")


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


class Populate(View):
    TABLE_NAME = "ex06_movies"
    conn = psycopg2.connect(database=settings.DATABASES['default']['NAME'],
                            user=settings.DATABASES['default']['USER'],
                            password=settings.DATABASES['default']['PASSWORD'],
                            host=settings.DATABASES['default']['HOST'],
                            port=settings.DATABASES['default']['PORT'])

    def get(self, request):

        answer = []
        with self.conn.cursor() as cur:
            for movie in movies:
                try:
                    cur.execute(f"""INSERT INTO {self.TABLE_NAME}(episode_nb, title, director, 
                                                producer, release_date) 
                                            VALUES (%s, %s, %s, %s, %s);""",
                                [movie['episode_nb'], movie['title'], movie['director'], movie['producer'], movie['release_date']])
                    answer.append("OK")
                    self.conn.commit()
                except psycopg2.DatabaseError as e:
                    self.conn.rollback()
                    answer.append(e)
        return HttpResponse("<br/>".join(str(i) for i in answer))


class Display(View):
    template = 'ex06/display.html'
    TABLE_NAME = "ex06_movies"
    conn = psycopg2.connect(database=settings.DATABASES['default']['NAME'],
                            user=settings.DATABASES['default']['USER'],
                            password=settings.DATABASES['default']['PASSWORD'],
                            host=settings.DATABASES['default']['HOST'],
                            port=settings.DATABASES['default']['PORT'])

    def get(self, request):
        try:
            with self.conn.cursor() as cur:
                cur.execute(f"""SELECT * FROM {self.TABLE_NAME};""")
                movies = cur.fetchall()
            return render(request, self.template, {'movies': movies})
        except Exception as e:
            return HttpResponse("No data available")


class Remove(View):
    template = "ex06/remove.html"
    TABLE_NAME = "ex06_movies"
    conn = psycopg2.connect(database=settings.DATABASES['default']['NAME'],
                            user=settings.DATABASES['default']['USER'],
                            password=settings.DATABASES['default']['PASSWORD'],
                            host=settings.DATABASES['default']['HOST'],
                            port=settings.DATABASES['default']['PORT'])

    def get(self, request):
        try:
            with self.conn.cursor() as cur:
                cur.execute(f"""SELECT * FROM {self.TABLE_NAME};""")
                movies = cur.fetchall()
            context = {'form': RemoveForm(choices=((movie[0], movie[0]) for movie in movies))}
            return render(request, self.template, context)
        except Exception as e:
            print(e)
            return HttpResponse("No data available")

    def post(self, request):
        try:
            with self.conn.cursor() as cur:
                cur.execute(f"""SELECT * FROM {self.TABLE_NAME};""")
                movies = cur.fetchall()
            choices = ((movie[0], movie[0]) for movie in movies)
        except Exception as e:
            print(e)
        data = RemoveForm(choices, request.POST)
        if data.is_valid() == True:
            try:
                with self.conn.cursor() as cur:
                    cur.execute(f"""DELETE FROM {self.TABLE_NAME} WHERE title = %s""", [data.cleaned_data['title']])
                self.conn.commit()
            except Exception as e:
                print(e)
        return redirect(request.path)


class Update(View):
    conn = psycopg2.connect(database=settings.DATABASES['default']['NAME'],
                            user=settings.DATABASES['default']['USER'],
                            password=settings.DATABASES['default']['PASSWORD'],
                            host=settings.DATABASES['default']['HOST'],
                            port=settings.DATABASES['default']['PORT'])

    def get(self, request):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""SELECT * FROM ex06_movies;""")
                movies = cur.fetchall()
            context = {'form': UpdateForm(choices=(
                (movie[0], movie[0]) for movie in movies))}
            return render(request, 'ex06/update.html', context)
        except Exception as e:
            print(e)
            return HttpResponse("No data available")

    def post(self, request):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""SELECT * FROM ex06_movies;""")
                movies = cur.fetchall()
            choices = (
                (movie[0], movie[0]) for movie in movies)
        except Exception as e:
            print(e)
        data = UpdateForm(choices, request.POST)
        if data.is_valid() == True:
            try:
                with self.conn.cursor() as cur:
                    cur.execute("""UPDATE ex06_movies SET opening_crawl = %s WHERE title = %s""",
                                [data.cleaned_data['opening_crawl'], data.cleaned_data['title']])
                self.conn.commit()
            except Exception as e:
                print(e)
        return redirect(request.path)
