from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='project/', null=False)

    created_at = models.DateTimeField(auto_now_add=True)

    # 이거는 python 에서 어떻게 부를지를 정의하는거라 migration 필요없음
    def __str__(self):
        return f'{self.name}'