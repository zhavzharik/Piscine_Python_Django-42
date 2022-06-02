from django.forms.forms import BaseForm
from django.db import DatabaseError
from django.shortcuts import redirect
from django.views.generic.list import ListView
from ..models.article import Article
from ..models.userfavouritearticle import UserFavouriteArticle
from django.contrib.auth.mixins import LoginRequiredMixin
from ..forms.userfavouritearticle import UserFavouriteArticleForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import FormView
from django.urls import reverse_lazy


class Favourite(LoginRequiredMixin, ListView, FormView):
    template_name = "userfavouritearticle.html"
    form_class = UserFavouriteArticleForm
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    model: UserFavouriteArticle = UserFavouriteArticle

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    def form_valid(self, form: AuthenticationForm):
        article_id = form.cleaned_data['article']
        try:
            UserFavouriteArticle.objects.get(
                article=article_id, user=self.request.user).delete()
            messages.success(
                self.request, "successful Remove to favourite.")
        except UserFavouriteArticle.DoesNotExist as e:
            try:
                UserFavouriteArticle.objects.create(
                    user=self.request.user,
                    article=Article.objects.get(id=article_id),
                )
                messages.success(
                    self.request, "successful Add to favourite.")
            except DatabaseError as e:
                messages.error(
                    self.request, "Unsuccessful Add to favourite. Database error.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, "Unsuccessful Add to favourite. Invalid information.")
        return redirect('favourite')

    def get_form(self, form_class=None) -> BaseForm:
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(None, **self.get_form_kwargs())
