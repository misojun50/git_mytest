from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=30, unique=True, null=True)
    message = models.CharField(max_length=200, null=True)


    # onetoonefield = 하나하나 연결시켜줌
    # related_name = 해당하는 이름으로 연결시켜줌
    # on_delete -> set_null = 유저가 누구인지 모르게 설정가능(예)
    # class는 하고나면 makemigration 해줘야하지만 안될꺼임. pip install Pillow 설치(이미지 관련)


