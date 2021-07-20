from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountCreationForm
from accountapp.models import HelloWorld


def hello_world(request):
#로그인'했을때'정보 불러오기
     if request.user.is_authenticated:

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
     else:
         #로그인 안했을 때 로그인 창으로 보내버림
         return HttpResponseRedirect(reverse('accountapp:login'))

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

#업데이트..?
#createview,detailview 와 비슷함. 각각 요소를 다 들고온다고 생각하면 됨.
#usercreationform은 아이디도 바꿔 버리기에 그거만 막아야함.
#accountapp폴더에 forms.py생성


#create와 detail에는 로그인(정보확인)이 필요가 없음.
#정보 업데이트와 삭제에 개인 데이터가 필요함으로 사용
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    #만들었던 form에서 가져옴
    context_object_name = 'target_User'
    success_url = reverse_lazy('accountapp:hello_world')
    #지금은 detail이 안됨. <int:pk>를 지정안했기 때문.
    template_name = 'accountapp/update.html'

    #로그인=정보 일치한사람만 변경가능  <=여기까지는 '로그인만 되있으면' 다른사람 정보도 접속 가능했기에 수정해야함
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.get_object() == request.user: #동일 인물인지 확인.
        #밑에 것을 실행하기 전에 로그인 여부 확인
            return super().get(request, *args, **kwargs)
        else:
            #다른 정보를 불러와서 잘못된 접근이라고 알려야 한다
            return HttpResponseForbidden()

        #post메소드로 변경
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.get_object() == request.user:
            return super().post(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()



#회원탈퇴 기능
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_User'
    success_url = reverse_lazy("accountapp:hello_world")
    template_name = 'accountapp/delete.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.get_object() == request.user:  # 동일 인물인지 확인.
            # 밑에 것을 실행하기 전에 로그인 여부 확인
            return super().get(request, *args, **kwargs)
        else:
            # 다른 정보를 불러와서 잘못된 접근이라고 알려야 한다
            return HttpResponseForbidden()

        # post메소드로 변경

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.get_object() == request.user:
            return super().post(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

        #어짜피 안에 들어가는 내용은 똑같기에(로그인 확인, 정보 수정) 그대로 붙여 써도 상관없음.
