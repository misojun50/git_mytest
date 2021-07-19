from django.contrib.auth.forms import UserCreationForm

#아이디 변경 불가능한 비밀번호 변경방법
class AccountCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.fields['username'].disabled = True