from django.http import HttpResponseForbidden

from profileapp.models import Profile


def profile_owner_var(func):
    def wrap(request, *args, **kwargs):
        target_profile = Profile.objects.get(pk=kwargs['pk'])
        if target_profile.user == request.user:
            # 조건이 맞으므로
            return func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    return wrap
