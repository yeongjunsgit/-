from django.db import models
from django.contrib.auth.models import AbstractUser
from allauth.account.adapter import DefaultAccountAdapter


# Create your models here.
class User(AbstractUser):
    
    username = models.CharField(max_length=30, unique=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True,null=True)
    age = models.IntegerField()
    money = models.IntegerField(blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    financial_products = models.TextField(blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    
    USERNAME_FIELD = 'username'
    # def __str__(self):
    #     return self.username
    
class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        print('aaaaaaa')
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        from allauth.account.utils import user_email, user_field, user_username
        # 기존 코드를 참고하여 새로운 필드들을 작성해줍니다.
        data = form.cleaned_data
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        username = data.get("username")
        nickname = data.get("nickname")
        age = data.get("age")
        money = data.get("money")
        salary = data.get("salary")
        financial_products = data.get("financial_products")
        print('aaaaaaa', financial_products)
        user_email(user, email)
        user_username(user, username)
        if first_name:
            user_field(user, "first_name", first_name)
        if last_name:
            user_field(user, "last_name", last_name)
        if nickname:
            user_field(user, "nickname", nickname)
        if age:
            user.age = age
        if money:
            user.money = money
        if salary:
            user.salary = salary
        if financial_products:
            user.financial_products = financial_products
            
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            # Ability not to commit makes it easier to derive from
            # this adapter by adding
            user.save()
        return user
    
# from django.conf import settings
# class UserSurvey(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
#     # 연금저축
#     like_yearsaving = models.BooleanField(null=True)
#     # 적금
#     like_save = models.BooleanField(null=True)
#     # 예금
#     like_deposit = models.BooleanField(null=True)
#     # 장기추구, 단기 추구
#     period = models.CharField(max_length=30,null=True)
#     # 대출필요?
#     need_loan = models.BooleanField(null=True)
#     # 대출 필요할때 주택담보/ 개인신용/ 전세자금
#     need_loantype = models.CharField(max_length=30,null=True)
#     # 한도? vs 최저금리
#     like_high_limit = models.BooleanField(null=True)

    