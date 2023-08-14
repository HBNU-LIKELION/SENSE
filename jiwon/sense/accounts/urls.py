from django.urls import path
from .views import kakao_get_login, get_user_info

app_name = 'accounts'

urlpatterns = [
    path('kakao/login/', kakao_get_login, name='account-login'),
    path('kakao/callback', get_user_info, name='account-callback'),
]