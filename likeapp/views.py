from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from articleapp.models import Article
from likeapp.models import LikeRecord

@method_decorator(login_required, 'get')
class LikeArticleView(RedirectView):

    def get(self, request, *args, **kwargs):
        user = request.user
        article = Article.objects.get(pk=kwargs['article_pk'])

        like_record = LikeRecord.objects.filter(user=user, article=article)

        if like_record.exists():    # 좋아요를 찍은적이 있으면 아무것도 안하고 되돌아감
            # 좋아요 반영안됨 -> 에러 메세지 표시
            # 모듈은 django.contrib.messages
            messages.add_message(request, messages.ERROR, '좋아요는 1번만 가능합니다.')
            return HttpResponseRedirect(reverse('articleapp:detail', kwargs={'pk':kwargs['article_pk']}))
        else:   # 좋아요 안했으면 저장하기 -> 완료 메세지 표시
            messages.add_message(request, messages.SUCCESS, "좋아요가 완료되었습니다.")
            LikeRecord(user=user, article=article).save()
        article.like += 1
        article.save()


        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse('articleapp:detail', kwargs={'pk':kwargs['article_pk']})