from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_world(request):
    return render(request, 'accountapp/hello_world.html')
# 굳이 templates를 새로 만들고 안에 accountapp폴더를 만들고 html 생성 이유 : 그냥 html만 있으면 경로 꼬임 가능성