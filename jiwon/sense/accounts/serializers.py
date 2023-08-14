from rest_framework.serializers import ModelSerializer
from .models import KakaoUser

class KaKaoUserSerializer(ModelSerializer):
    class Meta:
        model = KakaoUser
        fields = '__all__'