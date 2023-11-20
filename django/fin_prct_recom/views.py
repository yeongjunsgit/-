from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.response import Response
import requests
from .serializers import FinancialPrdtSerializer, FinancialOptionsSerializer,YearSavingPrdtSerializer, YearSavingOptionsSerializer, DepositLoanPrdtSerializer, DepositLoanOptionsSerializer, SavingPrdtSerializer, SavingOptionsSerializer, PersonalCreditLoanPrdtSerializer, PersonalCreditLoanOptionsSerializer, FinCompanyInfoSerializer, FinCompanyOptionSerializer, HouseLoanPrdtSerializer, HouseLoanOptionsSerializer
from .models import FinancialOptions,FinancialPrdt,YearSavingPrdt,YearSavingOptions, DepositLoanPrdt, DepositLoanOptions, SavingPrdt, PersonalCreditLoanPrdt,FinCompanyInfo,FinCompanyOptions, HouseLoanPrdt,HouseLoanOptions,SavingOptions
# from rest_framework.decorators import permiSthenticated, IsAdminUser


api_key = '3fd1a070dff058dde65e087c621280b7'
# Create your views here.
@api_view(['GET'])
def save_financial_products(request):
    
    # 정기예금
    url = f"http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1"
    response = requests.get(url).json()
    # return Response(response)
    
    # 상품 저장
    for li in response['result']['baseList']:
        save_baseList = {
            "dcls_month":li.get('dcls_month'),
            "fin_co_no":li.get('fin_co_no'),
            "kor_co_nm":li.get('kor_co_nm'),
            "fin_prdt_cd":li.get('fin_prdt_cd'),
            "fin_prdt_nm":li.get('fin_prdt_nm'),
            "join_way":li.get('join_way'),
            "mtrt_int":li.get('mtrt_int'),
            "spcl_cnd":li.get('spcl_cnd'),
            "join_deny":li.get('join_deny'),
            "join_member":li.get('join_member'),
            "etc_note":li.get('etc_note'),
            "max_limit":li.get('max_limit'),
            "dcls_strt_day":li.get('dcls_strt_day'),
            "dcls_end_dat":li.get('dcls_end_dat'),
            "fin_co_subm_day":li.get('fin_co_subm_day'),
        }
        # 데이터를 포장해서 유효성 확인
        serializers = FinancialPrdtSerializer(data=save_baseList)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
     # 데이터베이스를 돌면서 이름이 같은지 확인하기!
    products = FinancialPrdt.objects.all()

    # 저장된 product들을 순회
    for product in products:
        # 현재 옵션 리스트들을 순회
        for li in response['result']['optionList']:
            # product의 금융상품 코드와 현재 옵션의 금융 상품 코드가 같으면
            if li.get('fin_prdt_cd') == product.fin_prdt_cd:
                # 딕셔너리 형태로 저장 
                save_optionList = {
                    # 'product': li.get('fin_prdt_cd'),
                    'intr_rate_type': li.get('intr_rate_type'),
                    'intr_rate_type_nm': li.get('intr_rate_type_nm'),
                    'save_trm': li.get('save_trm'),
                    'intr_rate': li.get('intr_rate'),
                    'intr_rate2': li.get('intr_rate2'),
                }
                # 데이터 저장
                serializers = FinancialOptionsSerializer(data=save_optionList)
                if serializers.is_valid(raise_exception=True):
                    # 저장 전에 product pk값 참조해야함
                    serializers.save(product=product)
                    
    return JsonResponse({ 'message': 'save_complete'})
    # 연금저축
    # 전세 자금 대출
    # 적금

@api_view(['GET'])
def save_yearsaving_products(request):
    # 정기예금
    url = f"http://finlife.fss.or.kr/finlifeapi/annuitySavingProductsSearch.json?auth={api_key}&topFinGrpNo=060000&pageNo=1"
    response = requests.get(url).json()
    # return Response(response)
    
    # 상품 저장
    for li in response['result']['baseList']:
        save_baseList = {
            "dcls_month":li.get('dcls_month'),
            "fin_co_no":li.get('fin_co_no'),
            "kor_co_nm":li.get('kor_co_nm'),
            "fin_prdt_cd":li.get('fin_prdt_cd'),
            "fin_prdt_nm":li.get('fin_prdt_nm'),
            "join_way":li.get('join_way'),
            "pnsn_kind":li.get('pnsn_kind'),
            "pnsn_kind_nm":li.get('pnsn_kind_nm'),
            "sale_strt_day":li.get('sale_strt_day'),
            "mntn_cnt":li.get('mntn_cnt'),
            "prdt_type":li.get('prdt_type'),
            "prdt_type_nm":li.get('prdt_type_nm'),
            "dcls_rate":li.get('dcls_rate'),
            "guar_rate":li.get('guar_rate'),
            "btrm_prft_rate_1":li.get('btrm_prft_rate_1'),
            "btrm_prft_rate_2":li.get('btrm_prft_rate_2'),
            "btrm_prft_rate_3":li.get('btrm_prft_rate_3'),
            "etc":li.get('etc'),
            "sale_co":li.get('sale_co'),
            "dcls_strt_day":li.get('dcls_strt_day'),
            "dcls_end_day":li.get('dcls_end_day'),
            "fin_co_subm_day":li.get('fin_co_subm_day'),
        }
        # 데이터를 포장해서 유효성 확인
        serializers = YearSavingPrdtSerializer(data=save_baseList)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
     # 데이터베이스를 돌면서 이름이 같은지 확인하기!
    products = YearSavingPrdt.objects.all()

    # 저장된 product들을 순회
    for product in products:
        # 현재 옵션 리스트들을 순회
        for li in response['result']['optionList']:
            # product의 금융상품 코드와 현재 옵션의 금융 상품 코드가 같으면
            if li.get('fin_prdt_cd') == product.fin_prdt_cd:
                # 딕셔너리 형태로 저장 
                save_optionList = {
                    'dcls_month': li.get('dcls_month'),
                    'fin_co_no': li.get('fin_co_no'),
                    'fin_prdt_cd': li.get('fin_prdt_cd'),
                    'pnsn_recp_trm': li.get('pnsn_recp_trm'),
                    'pnsn_recp_trm_nm': li.get('pnsn_recp_trm_nm'),
                    'pnsn_entr_age': li.get('pnsn_entr_age'),
                    'pnsn_entr_age_nm': li.get('pnsn_entr_age_nm'),
                    'mon_paym_atm': li.get('mon_paym_atm'),
                    'mon_paym_atm_nm': li.get('mon_paym_atm_nm'),
                    'paym_prd': li.get('paym_prd'),
                    'paym_prd_nm': li.get('paym_prd_nm'),
                    'pnsn_strt_age': li.get('pnsn_strt_age'),
                    'pnsn_strt_age_nm': li.get('pnsn_strt_age_nm'),
                    'pnsn_recp_amt': li.get('pnsn_recp_amt'),
                }
                # 데이터 저장
                serializers = YearSavingOptionsSerializer(data=save_optionList)
                if serializers.is_valid(raise_exception=True):
                    # 저장 전에 product pk값 참조해야함
                    serializers.save(product=product)
                    
    return JsonResponse({ 'message': 'save_complete'})
    


# 전세 자금 대출
@api_view(['GET'])
def save_deposiloan_products(request):
    url = f"http://finlife.fss.or.kr/finlifeapi/rentHouseLoanProductsSearch.json?auth={api_key}&topFinGrpNo=050000&pageNo=1"

    response = requests.get(url).json()
    # return Response(response)
    
    # 상품 저장
    for li in response['result']['baseList']:
        save_baseList = {
            "dcls_month":li.get('dcls_month'),
            "fin_co_no":li.get('fin_co_no'),
            "kor_co_nm":li.get('kor_co_nm'),
            "fin_prdt_cd":li.get('fin_prdt_cd'),
            "fin_prdt_nm":li.get('fin_prdt_nm'),
            "join_way":li.get('join_way'),
            "loan_inci_expn":li.get('loan_inci_expn'),
            "erly_rpay_fee":li.get('erly_rpay_fee'),
            "dly_rate":li.get('dly_rate'),
            "loan_lmt":li.get('loan_lmt'),
            "dcls_strt_day":li.get('dcls_strt_day'),
            "dcls_end_day":li.get('dcls_end_day'),
            "fin_co_subm_day":li.get('fin_co_subm_day'),
        }
        # 데이터를 포장해서 유효성 확인
        serializers = DepositLoanPrdtSerializer(data=save_baseList)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
     # 데이터베이스를 돌면서 이름이 같은지 확인하기!
    products = DepositLoanPrdt.objects.all()

    # 저장된 product들을 순회
    for product in products:
        # 현재 옵션 리스트들을 순회
        for li in response['result']['optionList']:
            # product의 금융상품 코드와 현재 옵션의 금융 상품 코드가 같으면
            if li.get('fin_prdt_cd') == product.fin_prdt_cd:
                # 딕셔너리 형태로 저장 
                save_optionList = {
                    'rpay_type': li.get('rpay_type'),
                    'rpay_type_nm': li.get('rpay_type_nm'),
                    'lend_rate_type': li.get('lend_rate_type'),
                    'lend_rate_type_nm': li.get('lend_rate_type_nm'),
                    'lend_rate_min': li.get('lend_rate_min'),
                    'lend_rate_max': li.get('lend_rate_max'),
                    'lend_rate_avg': li.get('lend_rate_avg'),
                }
                # 데이터 저장
                serializers = DepositLoanOptionsSerializer(data=save_optionList)
                if serializers.is_valid(raise_exception=True):
                    # 저장 전에 product pk값 참조해야함
                    serializers.save(product=product)
    return JsonResponse({ 'message': 'save_complete'})


# 적금 상품
@api_view(['GET'])
def save_saving_products(request):
    url = f"http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1"

    response = requests.get(url).json()
    # return Response(response)
    
    # 상품 저장
    for li in response['result']['baseList']:
        save_baseList = {
            "dcls_month":li.get('dcls_month'),
            "fin_co_no":li.get('fin_co_no'),
            "kor_co_nm":li.get('kor_co_nm'),
            "fin_prdt_cd":li.get('fin_prdt_cd'),
            "fin_prdt_nm":li.get('fin_prdt_nm'),
            "join_way":li.get('join_way'),
            "mtrt_int":li.get('mtrt_int'),
            "spcl_cnd":li.get('spcl_cnd'),
            "join_deny":li.get('join_deny'),
            "join_member":li.get('join_member'),
            "etc_note":li.get('etc_note'),
            "max_limit":li.get('max_limit'),
            "dcls_strt_day":li.get('dcls_strt_day'),
            "dcls_end_day":li.get('dcls_end_day'),
            "fin_co_subm_day":li.get('fin_co_subm_day'),
        }
        # 데이터를 포장해서 유효성 확인
        serializers = SavingPrdtSerializer(data=save_baseList)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
    # 데이터베이스를 돌면서 이름이 같은지 확인하기!
    products = SavingPrdt.objects.all()

    # 저장된 product들을 순회
    for product in products:
        # 현재 옵션 리스트들을 순회
        for li in response['result']['optionList']:
            # product의 금융상품 코드와 현재 옵션의 금융 상품 코드가 같으면
            if li.get('fin_prdt_cd') == product.fin_prdt_cd:
                # 딕셔너리 형태로 저장 
                save_optionList = {
                    'intr_rate_type': li.get('intr_rate_type'),
                    'intr_rate_type_nm': li.get('intr_rate_type_nm'),
                    'rsrv_type': li.get('rsrv_type'),
                    'rsrv_type_nm': li.get('rsrv_type_nm'),
                    'save_trm': li.get('save_trm'),
                    'intr_rate': li.get('intr_rate'),
                    'intr_rate2': li.get('intr_rate2'),
                }
                # 데이터 저장
                serializers = SavingOptionsSerializer(data=save_optionList)
                if serializers.is_valid(raise_exception=True):
                    # 저장 전에 product pk값 참조해야함
                    serializers.save(product=product)
    return JsonResponse({ 'message': 'save_complete'})

# 개인 신용 대출
@api_view(['GET'])
def save_personalcreditloan_products(request):
    url = f"http://finlife.fss.or.kr/finlifeapi/creditLoanProductsSearch.json?auth={api_key}&topFinGrpNo=030200&pageNo=1"

    response = requests.get(url).json()
    return Response(response)
    
    # # 상품 저장
    # for li in response['result']['baseList']:
    #     save_baseList = {
    #         "dcls_month":li.get('dcls_month'),
    #         "fin_co_no":li.get('fin_co_no'),
    #         "kor_co_nm":li.get('kor_co_nm'),
    #         "fin_prdt_cd":li.get('fin_prdt_cd'),
    #         "fin_prdt_nm":li.get('fin_prdt_nm'),
    #         "join_way":li.get('join_way'),
    #         "crdt_prdt_type":li.get('crdt_prdt_type'),
    #         "crdt_prdt_type_nm":li.get('crdt_prdt_type_nm'),
    #         "cb_name":li.get('cb_name'),
    #         "dcls_strt_day":li.get('dcls_strt_day'),
    #         "dcls_end_day":li.get('dcls_end_day'),
    #         "fin_co_subm_day":li.get('fin_co_subm_day'),
    #     }
    #     # 데이터를 포장해서 유효성 확인
    #     serializers = PersonalCreditLoanPrdtSerializer(data=save_baseList)
    #     if serializers.is_valid(raise_exception=True):
    #         serializers.save()
    # # 데이터베이스를 돌면서 이름이 같은지 확인하기!
    # products = PersonalCreditLoanPrdt.objects.all()

    # # 저장된 product들을 순회
    # for product in products:
    #     # 현재 옵션 리스트들을 순회
    #     for li in response['result']['optionList']:
    #         # product의 금융상품 코드와 현재 옵션의 금융 상품 코드가 같으면
    #         if li.get('fin_prdt_cd') == product.fin_prdt_cd:
    #             # 딕셔너리 형태로 저장 
    #             save_optionList = {
    #                 'crdt_lend_rate_type': li.get('crdt_lend_rate_type'),
    #                 'crdt_lend_rate_type_nm': li.get('crdt_lend_rate_type_nm'),
    #                 'crdt_grad_1': li.get('crdt_grad_1'),
    #                 'crdt_grad_4': li.get('crdt_grad_4'),
    #                 'crdt_grad_5': li.get('crdt_grad_5'),
    #                 'crdt_grad_6': li.get('crdt_grad_6'),
    #                 'crdt_grad_10': li.get('crdt_grad_10'),
    #                 'crdt_grad_11': li.get('crdt_grad_11'),
    #                 'crdt_grad_12': li.get('crdt_grad_12'),
    #                 'crdt_grad_13': li.get('crdt_grad_13'),
    #                 'crdt_grad_avg': li.get('crdt_grad_avg'),
    #             }
    #             # 데이터 저장
    #             serializers = PersonalCreditLoanOptionsSerializer(data=save_optionList)
    #             if serializers.is_valid(raise_exception=True):
    #                 # 저장 전에 product pk값 참조해야함
    #                 serializers.save(product=product)
    # return JsonResponse({ 'message': 'save_complete'})


# 주택 담보 대출
@api_view(['GET'])
def save_houseloan_products(request):
    url = f"http://finlife.fss.or.kr/finlifeapi/mortgageLoanProductsSearch.json?auth={api_key}&topFinGrpNo=050000&pageNo=1"

    response = requests.get(url).json()
    # return Response(response)
    
    # 상품 저장
    for li in response['result']['baseList']:
        save_baseList = {
            "dcls_month":li.get('dcls_month'),
            "fin_co_no":li.get('fin_co_no'),
            "kor_co_nm":li.get('kor_co_nm'),
            "fin_prdt_cd":li.get('fin_prdt_cd'),
            "fin_prdt_nm":li.get('fin_prdt_nm'),
            "join_way":li.get('join_way'),
            "loan_inci_expn":li.get('loan_inci_expn'),
            "erly_rpay_fee":li.get('erly_rpay_fee'),
            "dly_rate":li.get('dly_rate'),
            "loan_lmt":li.get('loan_lmt'),
            "dcls_strt_day":li.get('dcls_strt_day'),
            "dcls_end_day":li.get('dcls_end_day'),
            "fin_co_subm_day":li.get('fin_co_subm_day'),
        }
        # 데이터를 포장해서 유효성 확인
        serializers = HouseLoanPrdtSerializer(data=save_baseList)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
    # 데이터베이스를 돌면서 이름이 같은지 확인하기!
    products = HouseLoanPrdt.objects.all()

    # 저장된 product들을 순회
    for product in products:
        # 현재 옵션 리스트들을 순회
        for li in response['result']['optionList']:
            # product의 금융상품 코드와 현재 옵션의 금융 상품 코드가 같으면
            if li.get('fin_prdt_cd') == product.fin_prdt_cd:
                # 딕셔너리 형태로 저장 
                save_optionList = {
                    'mrtg_type': li.get('mrtg_type'),
                    'mrtg_type_nm': li.get('mrtg_type_nm'),
                    'rpay_type': li.get('rpay_type'),
                    'rpay_type_nm': li.get('rpay_type_nm'),
                    'lend_rate_type': li.get('lend_rate_type'),
                    'lend_rate_type_nm': li.get('lend_rate_type_nm'),
                    'lend_rate_min': li.get('lend_rate_min'),
                    'lend_rate_max': li.get('lend_rate_max'),
                    'lend_rate_avg': li.get('lend_rate_avg'),
                }
                # 데이터 저장
                serializers = HouseLoanOptionsSerializer(data=save_optionList)
                if serializers.is_valid(raise_exception=True):
                    # 저장 전에 product pk값 참조해야함
                    serializers.save(product=product)
    return JsonResponse({ 'message': 'save_complete'})


@api_view(['GET'])
def save_fincompany_info(request):
    url = f"http://finlife.fss.or.kr/finlifeapi/companySearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1"

    response = requests.get(url).json()
    
    # return JsonResponse(response)
    # 상품 저장
    for li in response['result']['baseList']:
        save_baseList = {
            
            "dcls_month":li.get('dcls_month'),
            "fin_co_no":li.get('fin_co_no'),
            "kor_co_nm":li.get('kor_co_nm'),
            "dcls_chrg_man":li.get('dcls_chrg_man'),
            "homp_url":li.get('homp_url'),
            "cal_tel":li.get('cal_tel'),
        }
        # 데이터를 포장해서 유효성 확인
        serializers = FinCompanyInfoSerializer(data=save_baseList)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
    # 데이터베이스를 돌면서 이름이 같은지 확인하기!
    products = FinCompanyInfo.objects.all()

    # 저장된 product들을 순회
    for product in products:
        # 현재 옵션 리스트들을 순회
        for li in response['result']['optionList']:
            # product의 금융상품 코드와 현재 옵션의 금융 상품 코드가 같으면
            if li.get('fin_co_no') == product.fin_co_no:
                # 딕셔너리 형태로 저장 
                save_optionList = {
                    'area_cd': li.get('area_cd'),
                    'area_nm': li.get('area_nm'),
                    'exis_yn': li.get('exis_yn'),
                }
                # 데이터 저장
                serializers = FinCompanyOptionSerializer(data=save_optionList)
                if serializers.is_valid(raise_exception=True):
                    # 저장 전에 product pk값 참조해야함
                    serializers.save(product=product)
    return JsonResponse({ 'message': 'save_complete'})




def delete(req):

    data = FinancialOptions.objects.all()
    data.delete()
    data = FinancialPrdt.objects.all()
    data.delete()
    data = YearSavingPrdt.objects.all()
    data.delete()
    data = YearSavingOptions.objects.all()
    data.delete()
    data = DepositLoanPrdt.objects.all()
    data.delete()
    data = DepositLoanOptions.objects.all()
    data.delete()
    data = SavingPrdt.objects.all()
    data.delete()
    data = SavingOptions.objects.all()
    data.delete()
    data = PersonalCreditLoanPrdt.objects.all()
    data.delete()
    data = FinCompanyInfo.objects.all()
    data.delete()
    data = FinCompanyOptions.objects.all()
    data.delete()
    data = HouseLoanPrdt.objects.all()
    data.delete()
    data = HouseLoanOptions.objects.all()
    data.delete()

    
    return JsonResponse({'message':'okay'})


@api_view(['GET'])
def list_financial_products(request):
    if request.method == 'GET':
        financial_data = get_list_or_404(FinancialPrdt)


        serializer = FinancialPrdtSerializer(financial_data, many=True)
        return Response(serializer.data)
    
    
@api_view(['GET'])
def list_financial_options(request):
    if request.method == 'GET':
        financial_datas = FinancialOptions.objects.all().order_by('-intr_rate2')
        if financial_datas:
            serializer = FinancialOptionsSerializer(financial_datas, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)



# # Create your views here.
# @api_view(['GET'])
# def user_detail(request):
#     if request.method == 'GET':
#         Users = get_list_or_404(User)
#         serializer = CustomRegisterSerializer(Users, many=True)
#         return Response(serializer.data)
        