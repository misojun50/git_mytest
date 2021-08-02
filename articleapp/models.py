from django.contrib.auth.models import User
from django.db import models

# Create your models here.


#onetoonefield : 1대 1
#Foreignkey : 1대 다수
#on_delete = 작성자가 삭제했을때 : 작성자 미상으로 남김
class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='article', null=True)

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=True)
    content = models.TextField(null=True)

    created_at = models.DateField(auto_now_add=True, null=True)
    #이러면 지정해주지않아도 시간이 자동으로 입력됨.
# textfield = 긴 문자열
# 모델 만들었으니 당연히 form도