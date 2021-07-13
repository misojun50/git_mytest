from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_world, AccountCreateView

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name="hello_world"),
# 함수는 classname.as_view() 추가
    path('create/', AccountCreateView.as_view(), name='create'),
# 안뜨는게 정상. template설정을 안했기 때문.

# 로그인 설정+ html만들기 (template_name 쓰기)
    path('login/',  LoginView.as_view(template_name='accountapp/login.html'), name='login'),
# 로그아웃 설정(Django 가  다 다해줌)
    path('logout/', LogoutView.as_view(), name='logout'),


]

