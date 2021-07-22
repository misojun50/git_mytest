from django.contrib.auth.models import User
from django.http import HttpResponseForbidden




#get(self, request, *args, **kwargs
#request유저와 target 유저 설정 필요
#User 로드 + 단일 객체만 들고옴(all X)
def account_owner_var(func):
    def wrap(request, *args, **kwargs):
        target_user = User.objects.get(pk=kwargs['pk'] )
        if target_user == request.user:
            return func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    return wrap