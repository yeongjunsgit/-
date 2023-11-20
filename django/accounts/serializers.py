from rest_framework import serializers
from django.contrib.auth import get_user_model


class CustomRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'email', 'age', 'money', 'nickname', 'salary', 'financial_products',)
        

    
