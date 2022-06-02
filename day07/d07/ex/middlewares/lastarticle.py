from ..forms.login import LoginForm
from ..models.article import Article
from django.utils.deprecation import MiddlewareMixin


class LastArticleMiddlware(MiddlewareMixin):
    def process_template_response(self, request, response):
        articles = Article.objects.all().order_by('-id')
        if len(articles):
            response.context_data["last_article"] = articles[0]
        response.context_data['login_form'] = LoginForm
        return response
