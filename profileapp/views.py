from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreationView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        # 검증과정이 끝나고 나서 실행되는 함수.(성공했을 때)
        form.instance.user = self.request.user
        return super().form_valid(form)# 부모의 form_valid값을 불러옴

class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/update.html'

    #데이터베이스 안에는 이미지 자체가 저장되지 않음. 정확히는 경로를 저장함
    #그리고 media,profile 폴더가 만들어진 이유 : media_root 를 설정해 뒀기 때문.
    # +models.py에서 upload_to에 profile이라는 곳에 저장을 하라고 지정해뒀음.