from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accountapp.models import HelloWorld


def hello_world(request):
    #return render(request, 'accountapp/hello_world.html')
# 굳이 templates를 새로 만들고 안에 accountapp폴더를 만들고 html 생성 이유 : 그냥 html만 있으면 경로 꼬임 가능성
    if request.method == "POST":

        # request에 POST함수에 get으로 input_text 라는 이름을 가진 데이터를 가져와서 temp에 할당시킴
        temp = request.POST.get('input_text')
        # 데이터베이스에 저장해주는 과정
        new_hel = HelloWorld()
        new_hel.text = temp
        new_hel.save()

        return render(request, 'accountapp/hello_world.html',
                      context={'new_hel': new_hel})     #이번에는 객체를 반환함 + html에서 템플릿 변환
    else:   #get방식일때
        return render(request, 'accountapp/hello_world.html',
                      context={'text': 'GET METHOD!'})