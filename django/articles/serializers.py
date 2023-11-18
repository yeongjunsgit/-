from rest_framework import serializers
from .models import Article
from django.contrib.auth import get_user_model


class ArticleListSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('username', 'id')
            
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Article
        fields = ('id', 'title', 'content','user',)
        


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)
