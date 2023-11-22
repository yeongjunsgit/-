from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# from rest_framework.response import JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404
# from django.contrib.auth import get_
from .serializers import CustomRegisterSerializer,UserSerializer,UserSurveySerializer
from .models import User,UserSurvey
from django.shortcuts import render

from fin_prct_recom.serializers import UserJoinPrdtSerializer
# Create your views here.
@api_view(['GET'])
def user_detail(request):
    if request.method == 'GET':
        Users = get_list_or_404(User)
        serializer = CustomRegisterSerializer(Users, many=True)
        return Response(serializer.data)
        

from django.contrib.auth import get_user_model
@api_view(['PUT'])
def add_data(request):
    print('add_data')
    if request.method == 'PUT':
        user_instance = get_object_or_404(User, username=request.user.username)
        serializer = UserSerializer(user_instance, data={'financial_products':request.data['financial_products']}, partial=True)
        financial_products_list = request.data['financial_products'].split(',')
        type_products_list = request.data['product_type'].split(',')

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            for i in range(len(financial_products_list)):
                join_data = {
                    'user':request.data['user'],
                    'user_age':request.data['user_age'],
                    'product':financial_products_list[i],
                    'product_type':type_products_list[i],
                }
                print(request.data)
                serializer2 = UserJoinPrdtSerializer(data=join_data)
                if serializer2.is_valid(raise_exception=True):
                    serializer2.save()
            return Response(serializer.data)
        


# # 나와 비슷한 나이대의 사용자가 많이 가입한 상품 데이터 정제
# @api_view(['GET'])
# def same_age_filter(request, myage):
#     # 1. 유저 데이터를 호출한 후 해당 데이터에서 나이값을 기준으로 10살 위아래로 필터링
#     user_datas = get_list_or_404(get_user_model(), myage-10 <= age <= myage+10)
#     financial_datas = user_datas.annotate(count=Count('name')).filter(count__gt=1)
#     sorted_datas = sorted(financial_datas, key=lambda x: x[count], reverse=True)
#     top_10_datas = sorted_datas[:10]
    
#     return Response({'data': 'yes'})
    
    # financial_datas = get_user_model().objects.values('name').annotate(count=Count('name')).filter(count__gt=1)
    # sorted_datas = sorted(financial_datas, key=lambda x: x[count], reverse=True)
    # top_10_datas = sorted_datas[:10]
    # response_data = [{'name': item['name'], 'count': item['count']} for item in top_10_datas]

    # all_products = []
    # for i in range(6):
    #     if i == 0:
    #         sub_url = financal_products
    #     elif i == 1:
    #         sub_url = financal_products
    #     elif i == 2:
    #         sub_url = financal_products
    #     elif i == 3:
    #         sub_url = financal_products
    #     elif i == 4:
    #         sub_url = rfdfdf

    #     tmp_datas = (~~models).objects.all()

    #     for data in tmp_datas:
    #         for match in top_10_datas:
    #             if data.~~_prdt_cd == match.~~name:
    #                 all_products.append(data)

    # response(all_products)


@api_view(['POST'])
def survey(request):
    user_survey = UserSurvey.objects.filter(user_id=request.data['user'])
    if len(user_survey)==0 and request.method == "POST":
        serializer = UserSurveySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == "POST":
        user_survey = get_object_or_404(UserSurvey, user_id=request.data['user'])
        serializer = UserSurveySerializer(user_survey,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method =='DELETE':
        user_surveys = UserSurvey.objects.all()
        user_surveys.delete()
        return Response({'mes':'okay'})