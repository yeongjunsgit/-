from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# from rest_framework.response import JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404
# from django.contrib.auth import get_
from .serializers import CustomRegisterSerializer,UserSerializer
from .models import User
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
        print()
        
        print(request.data)
        join_data = {
            'user':request.data['user'],
            'product':request.data['financial_products'],
        }
        print(join_data)
        serializer2 = UserJoinPrdtSerializer(data=join_data)
    
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            if serializer2.is_valid(raise_exception=True):
                serializer2.save()
            return Response(serializer.data)
        


    
# # 나와 비슷한 나이대의 사용자가 많이 가입한 상품 데이터 정제
# @api_view(['GET'])
# def same_age_filter(request):
#     if request.method == 'GET':
#         financial_datas = get_user_model().objects.values('name').annotate(count=Count('name')).filter(count__gt=1)
#         sorted_datas = sorted(financial_datas, key=lambda x: x[count], reverse=True)
#         top_10_datas = sorted_datas[:10]
#         response_data = [{'name': item['name'], 'count': item['count']} for item in top_10_datas]

#         all_products = []
#         for i in range(6):
#             if i == 0:
#                 sub_url = financal_products
#             elif i == 1:
#                 sub_url = financal_products
#             elif i == 2:
#                 sub_url = financal_products
#             elif i == 3:
#                 sub_url = financal_products
#             elif i == 4:
#                 sub_url = rfdfdf

#             tmp_datas = (~~models).objects.all()

#             for data in tmp_datas:
#                 for match in top_10_datas:
#                     if data.~~_prdt_cd == match.~~name:
#                         all_products.append(data)

#         response(all_products)