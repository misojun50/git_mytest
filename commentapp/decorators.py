from django.http import HttpResponseForbidden

from commentapp.models import Comment


def comment_owner_var(func):
    def wrap(request, *args, **kwargs):
        target_comment = Comment.objects.get(pk=kwargs['pk'])
        if target_comment.writer == request.user:
            return func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    return wrap