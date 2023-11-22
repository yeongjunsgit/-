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
from fin_prct_recom.models import UserJoinPrdt, FinancialPrdt, YearSavingPrdt, DepositLoanPrdt, SavingPrdt, PersonalCreditLoanPrdt, HouseLoanPrdt,FinancialOptions, YearSavingOptions, DepositLoanOptions, SavingOptions, PersonalCreditLoanOptions, HouseLoanOptions
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
@api_view(['GET'])
def same_age_filter(request, myage):


    # 1. 유저 데이터를 호출한 후 해당 데이터에서 나이값을 기준으로 10살 위아래로 필터링
    # join_product = UserJoinPrdt.objects.filter()
    # 가입 상품중에 나와 나잇대가 비슷한 상품만 골라서 가져옵니다
    user_datas = get_list_or_404(UserJoinPrdt, user_age__range=(myage - 10, myage + 10))

    # 상품들을 product 명에 따라 개수를 세어 준다.
    count_dict = {}
    for i in range(len(user_datas)):
        if f'{user_datas[i].product_type},{user_datas[i].product}' in count_dict:
            count_dict[f'{user_datas[i].product_type},{user_datas[i].product}'] += 1
        else:
            count_dict[f'{user_datas[i].product_type},{user_datas[i].product}'] = 1
  
    temp_lis = list(count_dict.items())
    # print(type(temp_lis))
    temp_lis.sort(key=lambda x:x[1],reverse=True)
    
    top_10_datas = temp_lis[:min(len(temp_lis), 10)]
    # 2. 정렬한 데이터에서 이름을 비교하여 같은 이름의 정보를 꺼내와 JSON형식으로 저장 (count 필드 추가)
    
    response_data = []
  
    # response_data[name] = count
    financial_data = get_list_or_404(FinancialPrdt)
    yearsaving_data = get_list_or_404(YearSavingPrdt)
    saving_data = get_list_or_404(SavingPrdt)
    depositloanprdt_data = get_list_or_404(DepositLoanPrdt)
    houseloanprdt_data = get_list_or_404(HouseLoanPrdt)

    for tmp in top_10_datas:
        product_type, product = tmp[0].split(',')
        count = tmp[1]
        
        if product_type == 'financial':
            for f in financial_data:
                if f.fin_prdt_cd == product:
                    wanna_data = {
                        'fin_prdt_nm': f.fin_prdt_nm,
                        'kor_co_nm': f.kor_co_nm,
                        'max_limit': f.max_limit,
                        'fin_prdt_cd': f.fin_prdt_cd,
                        'count': count,
                        'product_type': 'financial',
                    }
                    response_data.append(wanna_data)

                    
        elif product_type == 'yearsaving':
            for f in yearsaving_data:
                if f.fin_prdt_cd == product:
                    wanna_data = {
                        'fin_prdt_nm':f.fin_prdt_nm,
                        'fin_prdt_cd':f.fin_prdt_cd,
                        'kor_co_nm': f.kor_co_nm,
                        'btrm_prft_rate_1':f.btrm_prft_rate_1,
                        'prdt_type_nm':f.prdt_type_nm,
                        'count':count,
                        'product_type':product_type,
                    }
                    response_data.append(wanna_data)
                    
        elif product_type == 'saving':
            for f in saving_data:
                if f.fin_prdt_cd == product:
                    wanna_data = {
                        'fin_prdt_cd': f.fin_prdt_cd,
                        'kor_co_nm': f.kor_co_nm,
                        'max_limit': f.max_limit,
                        'fin_prdt_nm': f.fin_prdt_nm,
                        'count': count,
                        'product_type': 'financial',
                    }
                    response_data.append(wanna_data)

                
        elif product_type == 'depositloan':
            for f in depositloanprdt_data:
                if f.fin_prdt_cd == product:
                
                    depositloanoptions_data = DepositLoanOptions.objects.filter(product_id = f.fin_prdt_cd).order_by('lend_rate_min')
                    if len(depositloanoptions_data):

                        max_rate_data = depositloanoptions_data[0]
                        wanna_data = {
                            'fin_prdt_cd': f.fin_prdt_cd,
                            'kor_co_nm': f.kor_co_nm,
                            'fin_prdt_nm': f.fin_prdt_nm,
                            'max_option': max_rate_data.lend_rate_min,
                            'count': count,
                            'product_type': 'depositloan'
                            
                        }
                        response_data.append(wanna_data)
                    
        elif product_type == 'homeloan':
            for f in houseloanprdt_data:
                if f.fin_prdt_cd == product:

                    houseloanoptions_data = HouseLoanOptions.objects.filter(product_id = f.fin_prdt_cd).order_by('lend_rate_min')
                    # HouseLoanOptions.objects.filter(product_id = f.fin_prdt_cd).order_by('lend_rate_min')
                    if len(houseloanoptions_data):
                        # .order_by('lend_rate_min')
                        max_rate_data = houseloanoptions_data[0]
                        wanna_data = {
                            'fin_prdt_cd': f.fin_prdt_cd,
                            'kor_co_nm': f.kor_co_nm,
                            'fin_prdt_nm': f.fin_prdt_nm,
                            'max_option': max_rate_data.lend_rate_min,
                            'count': count,
                            'product_type': 'homeloan'
                        }
                        response_data.append(wanna_data)
    print()
    print()
    print()
    print()
    print(response_data)
    print()
    print()
    print()
    return Response({'data' : response_data}, status=status.HTTP_200_OK)


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
    
    
