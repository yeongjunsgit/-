from rest_framework import serializers
from allauth.account import app_settings as allauth_settings
from allauth.utils import get_username_max_length
from allauth.account.adapter import get_adapter
from .models import User
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model

class CustomRegisterSerializer(RegisterSerializer):
# 추가할 필드들을 정의합니다.
    nickname = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=255
    )
    age = serializers.IntegerField(required=False)
    money = serializers.IntegerField(required=False)
    salary = serializers.IntegerField(required=False)
    financial_products = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=1000
    )

    def validate_financial_products(self, value):
        # financial_products 값을 쉼표로 구분하여 리스트로 변환
        if value:
            value = value.split(',')
        return value

    def to_internal_value(self, data):
        # financial_products 값을 쉼표로 구분하여 리스트로 변환
        if isinstance(data, str):
            data = data.split(',')
        return super().to_internal_value(data)
    def get_cleaned_data(self):
        return {
        'username': self.validated_data.get('username', ''),
        'password1': self.validated_data.get('password1', ''),
        'email': self.validated_data.get('email', ''),
        'nickname': self.validated_data.get('nickname', ''),
        'age': self.validated_data.get('age', ''),
        'money': self.validated_data.get('money', ''),
        'salary': self.validated_data.get('salary', ''),
        'financial_products': self.validated_data.get('financial_products', ''),
        }
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields=('financial_products',)


# class UserSurveySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserSurvey
#         fields=('__all__')
#         read_only_fields=('user',)