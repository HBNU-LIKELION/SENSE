from rest_framework.serializers import ModelSerializer

from .models import Post, Report

class PostBaseModelSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class ReportBaseModelserializer(ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

class PostListRetrieveModelSerializer(PostBaseModelSerializer):
    class Meta(PostBaseModelSerializer.Meta):
        fields = ['id', 'word', 'meaning', 'writer', 'prev_id', 'next_id']
        depth = 1

class PostCreateModelSerializer(PostBaseModelSerializer):
    class Meta(PostBaseModelSerializer.Meta):
        fields = ['id', 'word', 'meaning', 'prev_id', 'next_id']