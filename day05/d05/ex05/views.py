from django.shortcuts import render, redirect
from django.views import View
from .models import Movies
from django.http import HttpResponse
from .forms import RemoveForm
from django import db


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

    def get(self, request):
        answer = []
        for movie in movies:
            try:
                Movies.objects.create(episode_nb=movie['episode_nb'],
                                      title=movie['title'],
                                      director=movie['director'],
                                      producer=movie['producer'],
                                      release_date=movie['release_date'])
                answer.append("OK")
            except db.Error as e:
                answer.append(e)
        return HttpResponse("<br/>".join(str(i) for i in answer))


class Display(View):
    template = 'ex05/display.html'

    def get(self, request):
        try:
            movies = Movies.objects.all()
            if len(movies) == 0:
                raise Movies.DoesNotExist
            return render(request, self.template, {'movies': movies})
        except Movies.DoesNotExist as e:
            return HttpResponse("No data available")


class Remove(View):
    template = 'ex05/remove.html'

    def get(self, request):
        try:
            movies = Movies.objects.all()
            if len(movies) == 0:
                raise Movies.DoesNotExist
        except Movies.DoesNotExist as e:
            print(e)
            return HttpResponse("No data available")
        choices = ((movie.title, movie.title) for movie in movies)
        context = {'form': RemoveForm(choices)}
        return render(request, self.template, context)

    def post(self, request):
        try:
            movies = Movies.objects.all()
            if len(movies) == 0:
                raise Movies.DoesNotExist
        except Movies.DoesNotExist as e:
            return redirect(request.path)
        choices = ((movie.title, movie.title) for movie in movies)
        data = RemoveForm(choices, request.POST)
        if data.is_valid() == True:
            try:
                Movies.objects.get(title=data.cleaned_data['title']).delete()
            except db.Error as e:
                print(e)
        return redirect(request.path)
