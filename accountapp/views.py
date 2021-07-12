from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
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

        #모든 데이터 베이스 불러오기
        hello_world_list = HelloWorld.objects.all()


        return render(request, 'accountapp/hello_world.html',
                      context={'hello_world_list': hello_world_list})     #
    else:   #get방식일때
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html',
                      context={'hello_world_list': hello_world_list})      # get method 가 안뜨는 이유 = 지정한걸 없애버렸으니 ㅇㅅㅇ