from ..forms import UserFavouriteArticleForm
from ..models.article import Article
from django.views.generic import DetailView


class Detail(DetailView):
    template_name = "detail.html"
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = context['object']
        context["favouriteForm"] = UserFavouriteArticleForm(article.id)
        return context
