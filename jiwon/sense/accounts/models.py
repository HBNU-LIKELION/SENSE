from django.db import models

# Create your models here.
class KakaoUser(models.Model):
    kakao_id = models.IntegerField(verbose_name="Kakao_id", unique=True)
    nickname = models.CharField(verbose_name="Sense NickName", max_length=128)
    post_count = models.IntegerField(verbose_name="Post Count")