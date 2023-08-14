from django.contrib import admin
from .models import KakaoUser

# Register your models here.
@admin.register(KakaoUser)

class KakaoUserModelAdmin(admin.ModelAdmin):
    pass