from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.decorators import account_owner_var
from accountapp.forms import AccountCreationForm
from accountapp.models import HelloWorld


#decorater 테스트. Django가 '또' 다해줌
@login_required  #경로가 다를경우 @login_required(login_url=reverse_lazy('accountapp/login')
def hello_world(request):

    if request.method == "POST":
        temp = request.POST.get('input_text')
        new_hel = HelloWorld()
        new_hel.text = temp
        new_hel.save()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))

    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html',
                      context={'hello_world_list': hello_world_list})


# CreateView 불러오기 그래도 어디 있는지 알아만 두면 편함
# User, UserCreationForm 도 불러오기
# class 에서는 "reverse_lazy" 를 쓰는데 함수에서의 reverse 방법과 class 에서의 reverse 방법이 다르기 때문.
class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'
# 이상 진짜로 간단한 회원가입 로직.
# urls.py에 path 경로 내용 추가


#로그인 시 로그인정보 불러오기
#다음 urls.py에서 라우팅(경로) 설정
class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_User'
    template_name = 'accountapp/detail.html'


#decorator사용
owner_var = [login_required, account_owner_var]
@method_decorator(owner_var, 'get')
@method_decorator(owner_var, 'post')  # 이렇게 하면 깔끔함
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    #만들었던 form에서 가져옴
    context_object_name = 'target_User'
    success_url = reverse_lazy('accountapp:hello_world')
    #지금은 detail이 안됨. <int:pk>를 지정안했기 때문.
    template_name = 'accountapp/update.html'

#회원탈퇴 기능
@method_decorator(owner_var, 'get')
@method_decorator(owner_var, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_User'
    success_url = reverse_lazy("accountapp:hello_world")
    template_name = 'accountapp/delete.html'


