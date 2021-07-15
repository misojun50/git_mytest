from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView

from accountapp.models import HelloWorld


def hello_world(request):
    # return render(request, 'accountapp/hello_world.html')
    # 굳이 templates를 새로 만들고 안에 accountapp폴더를 만들고 html 생성 이유 : 그냥 html만 있으면 경로 꼬임 가능성
    if request.method == "POST":

        # request에 POST함수에 get으로 input_text 라는 이름을 가진 데이터를 가져와서 temp에 할당시킴
        temp = request.POST.get('input_text')
        # 데이터베이스에 저장해주는 과정
        new_hel = HelloWorld()
        new_hel.text = temp
        new_hel.save()

        # 새로고침하면 데이터 재입력 방지 urls 참조
        # 역추적 한다는 개념으로 reverse(django꺼 사용)
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