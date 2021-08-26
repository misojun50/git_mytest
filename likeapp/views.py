from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from articleapp.models import Article
from likeapp.models import LikeRecord

@transaction.atomic #만약 모종의 이유로 적용이 안될경우 DB에 반영안되게 함
def db_transaction(user, article):
    article.like += 1
    article.save()

    like_record = LikeRecord.objects.filter(user=user, article=article)

    if like_record.exists():
        raise ValidationError("like already exists") #여기 에러는 django안에서 확인하는 에러.
    else:  # 좋아요 안했으면 저장하기 -> 완료 메세지 표시
        LikeRecord(user=user, article=article).save()




@method_decorator(login_required, 'get')
class LikeArticleView(RedirectView):

    def get(self, request, *args, **kwargs):
        user = request.user
        article = Article.objects.get(pk=kwargs['article_pk'])

        try:
            db_transaction(user, article)
            # 좋아요 반영 0
            messages.add_message(request, messages.SUCCESS, "좋아요가 완료되었습니다.")
        except ValidationError:
            # 좋아요 반영 안됨
            messages.add_message(request, messages.ERROR, '좋아요는 1번만 가능합니다.')
            return HttpResponseRedirect(reverse('articleapp:detail', kwargs={'pk': kwargs['article_pk']}))

        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse('articleapp:detail', kwargs={'pk':kwargs['article_pk']})