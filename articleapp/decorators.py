from django.http import HttpResponseForbidden

from articleapp.models import Article


def article_owner_var(func):
    def wrap(request, *args, **kwargs):
        target_article = Article.objects.get(pk=kwargs['pk'])
        if target_article.writer == request.user:
            return func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    return wrap