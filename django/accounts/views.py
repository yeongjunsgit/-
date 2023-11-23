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
from django.core import serializers 
from django.core.serializers import serialize
from django.http import JsonResponse
import heapq
from django.db.models import F, ExpressionWrapper, fields
import json

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
        financial_products_list = request.data['financial_products'].split(',')
        type_products_list = request.data['product_type'].split(',')
        name_products_list = request.data['fin_prdt_nm'].split(',')
        
        user_model_datas = []
        for i in range(len(financial_products_list)):
            user_model_datas.append(f'{name_products_list[i]}|{financial_products_list[i]}')

        user_model_datas = ','.join(user_model_datas)

        serializer = UserSerializer(user_instance, data={'financial_products':user_model_datas}, partial=True)


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
   
    return Response({'data' : response_data}, status=status.HTTP_200_OK)


@api_view(['POST', 'DELETE'])
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
    
    
@api_view(['GET'])
def get_survey(request):
    if request.method == 'GET':
        s = UserSurvey.objects.filter(user_id=request.user.pk)[0]

        data = {
            'like_yearsaving':s.like_yearsaving,
            'like_save':s.like_save,
            'like_deposit':s.like_deposit,
            'period':s.period,
            'need_loan':s.need_loan,
            'need_loantype':s.need_loantype,
            'like_high_limit':s.like_high_limit,
        }
        final_data = {}

        # # 위험성 필터 → 
        # # 위험을 안골랐을때
        # # 전년도, 전전년도, 전전전년도 셋이 비등비등 → 차가 적은것
        # # 위험을 고른 경우
        # # 걍 아묻따 작년기준 높은거
        yearsaving_data = YearSavingPrdt.objects.all()

        if data['like_yearsaving'] == 1:
            warning_yearsave = yearsaving_data.order_by('-btrm_prft_rate_1')
            temp_lis = list(warning_yearsave.values()[:3])
            
            final_data['YearSavingPrdt'] = temp_lis

        # # 위험성 NO
        else:
            warning_yearsave = yearsaving_data.annotate(calculated_field=ExpressionWrapper(
                F('btrm_prft_rate_1') - F('btrm_prft_rate_2') + F('btrm_prft_rate_1') - F('btrm_prft_rate_3') + F('btrm_prft_rate_3') - F('btrm_prft_rate_2'),
                output_field=fields.FloatField()
                    )).order_by('-calculated_field')
            
            temp_lis = list(warning_yearsave.values()[:3])
            
            final_data['YearSavingPrdt'] = temp_lis


        # # # 저축기간 형식 필터 → 최고 우대 금리 높은 순
        

        # 적금 추천을 받겠다

        if data['like_save']:
            saving_data = SavingOptions.objects.all()
            if data['period'] == '단기':
                # 적금
                saving_data.filter(save_trm=6).order_by('-intr_rate2')
              
            else:
                saving_data = SavingOptions.objects.filter(save_trm__gte=12).order_by('-intr_rate2')
            top_3_saving_data = saving_data[:min(len(saving_data),3)]

            final_saving_data = []
            for i in range(len(top_3_saving_data)):

                saving_data_prdt = get_object_or_404(SavingPrdt,fin_prdt_cd=top_3_saving_data[i].product_id)
                if saving_data_prdt:
                    saving_dict = {
                    'fin_prdt_cd':saving_data_prdt.fin_prdt_cd,
                    'kor_co_nm':saving_data_prdt.kor_co_nm,
                    'fin_prdt_nm':saving_data_prdt.fin_prdt_nm,
                    'intr_rate2':top_3_saving_data[i].intr_rate2,
                    'save_trm':top_3_saving_data[i].save_trm,
                    }
                    final_saving_data.append(saving_dict)

            final_data['saving_data'] = final_saving_data

        # 예금 추천을 받겠다
        if  data['like_deposit']:
            if data['period'] == '단기':
                # 적금
                deposit_data = FinancialOptions.objects.filter(save_trm=6).order_by('-intr_rate2')
            else:
                deposit_data = FinancialOptions.objects.filter(save_trm__gte=12).order_by('-intr_rate2')

            top_3_deposit_data = deposit_data[:min(len(deposit_data),3)]
            final_deposit_data = []
            for i in range(len(top_3_deposit_data)):
                deposit_data_prdt = get_object_or_404(FinancialPrdt,fin_prdt_cd=top_3_deposit_data[i].product_id)
                if deposit_data_prdt:
                    deposit_dict = {
                    'fin_prdt_cd':deposit_data_prdt.fin_prdt_cd,
                    'kor_co_nm':deposit_data_prdt.kor_co_nm,
                    'fin_prdt_nm':deposit_data_prdt.fin_prdt_nm,
                    'intr_rate2':top_3_deposit_data[i].intr_rate2,
                    'save_trm':top_3_deposit_data[i].save_trm,
                    }
                    final_deposit_data.append(deposit_dict)
                
            final_data['deposit_data'] = final_deposit_data


        # 대출
        # 필요? → 추천
        # 필요 x → 추천 X
        # 한도 높은거 VS 금리 낮은거
        # 주택 필요하신분 → 주택
        if data['need_loan']:
            final_loan_data = []
            if data['need_loantype'] == '주택담보':
                houseloanprdt_options = HouseLoanOptions.objects.all().order_by('lend_rate_min')
                top_3 = houseloanprdt_options[:3]
                for i in range(3):
                    prdt = get_object_or_404(HouseLoanPrdt,fin_prdt_cd=top_3[i].product_id)
                    house_loan_dict={
                        'fin_prdt_cd':prdt.fin_prdt_cd,
                        'kor_co_nm':prdt.kor_co_nm,
                        'fin_prdt_nm':prdt.fin_prdt_nm,
                        'lend_rate_min':top_3[i].lend_rate_min,
                        'lend_rate_max':top_3[i].lend_rate_max,
                        'product_type':'house_loan',
                    }
                    final_loan_data.append(house_loan_dict)
            elif data['need_loantype'] == '전세자금':
                depositloanprdt_options = DepositLoanOptions.objects.all().order_by('lend_rate_min')
                top_3 = depositloanprdt_options[:3]
                for i in range(3):
                    prdt = get_object_or_404(DepositLoanPrdt,fin_prdt_cd=top_3[i].product_id)
                    deposit_loan_dict={
                        'fin_prdt_cd':prdt.fin_prdt_cd,
                        'kor_co_nm':prdt.kor_co_nm,
                        'fin_prdt_nm':prdt.fin_prdt_nm,
                        'lend_rate_min':top_3[i].lend_rate_min,
                        'lend_rate_max':top_3[i].lend_rate_max,
                        'product_type':'deposit_loan',
                    }
                    final_loan_data.append(deposit_loan_dict)
            final_data['loan_data'] = final_loan_data

        return JsonResponse({'data': final_data})
    
        
    
