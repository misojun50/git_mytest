from django.forms import ModelForm
from profileapp.models import Profile


#djange구문, 특이하게 클래스 안에 Meta 클래스가 있음.
class ProfileCreationForm(ModelForm):
    class Meta:
        # 방금 만들었던 Profile
        model = Profile
        # fields = 클라이언트에게 받을 데이터(이미지, 닉네임, 메세지)입력을 받음
        fields = ['image', 'nickname', 'message']
        # 만들었던 클래스값은 4개인데 여기서는 3개인 이유 = 클래스를 믿지마라 ㅇㅅㅇ.
