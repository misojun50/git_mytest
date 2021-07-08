from django.db import models

# Create your models here.

class HelloWorld(models.Model):
    text = models.CharField(max_length=255, null=False)
        # 최대길이 255, 텍스트는 비어있으면 안된다는 선언.
    # 그다음 python mamage.py makemigrations