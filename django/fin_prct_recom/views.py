from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.response import Response
import requests
from .serializers import FinancialPrdtSerializer, FinancialOptionsSerializer,YearSavingPrdtSerializer, YearSavingOptionsSerializer, DepositLoanPrdtSerializer, DepositLoanOptionsSerializer, SavingPrdtSerializer, SavingOptionsSerializer, FinCompanyInfoSerializer, FinCompanyOptionSerializer, HouseLoanPrdtSerializer, HouseLoanOptionsSerializer, UserJoinPrdtSerializer
from .models import FinancialOptions,FinancialPrdt,YearSavingPrdt,YearSavingOptions, DepositLoanPrdt, DepositLoanOptions, SavingPrdt,FinCompanyInfo,FinCompanyOptions, HouseLoanPrdt,HouseLoanOptions,SavingOptions, UserJoinPrdt
# from rest_framework.decorators import permiSthenticated, IsAdminUser


api_key = settings.BANK_API_KEY
# Create your views here.
@api_view(['GET'])
def save_financial_products(request):

    for i in range(1,2):
        # 정기예금
        url = f"http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo={i}"
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
            # print()
            # print()
            # print(response['result'])
            # print()
            # print()
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
    # 연금저축
    for i in range(1,22):
    
        url = f"http://finlife.fss.or.kr/finlifeapi/annuitySavingProductsSearch.json?auth={api_key}&topFinGrpNo=060000&pageNo={i}"
        response = requests.get(url).json()
   
        
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
def save_depositloan_products(request):
    for i in range(1,8):
        url = f"http://finlife.fss.or.kr/finlifeapi/rentHouseLoanProductsSearch.json?auth={api_key}&topFinGrpNo=050000&pageNo={i}"

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
    for i in range(1,3):
        url = f"http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo={i}"

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



# 주택 담보 대출
@api_view(['GET'])
def save_homeloan_products(request):
    for i in range(1,9):
        url = f"http://finlife.fss.or.kr/finlifeapi/mortgageLoanProductsSearch.json?auth={api_key}&topFinGrpNo=050000&pageNo={i}"

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
    # data = PersonalCreditLoanPrdt.objects.all()
    # data.delete()
    data = FinCompanyInfo.objects.all()
    data.delete()
    data = FinCompanyOptions.objects.all()
    data.delete()
    data = HouseLoanPrdt.objects.all()
    data.delete()
    data = HouseLoanOptions.objects.all()
    data.delete()

    
    return JsonResponse({'message':'okay'})

# 여러개 조회---------------------------------------------------------------------------------------

# 정기 예금 필터링 view 함수
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


# 연금 저축 필터링 view 함수
@api_view(['GET'])
def list_yearsaving_products(request):
    if request.method == 'GET':
        financial_data = YearSavingPrdt.objects.all().order_by('-btrm_prft_rate_1')

        if financial_data:
            serializer = YearSavingPrdtSerializer(financial_data, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    
@api_view(['GET'])
def list_yearsaving_options(request):
    if request.method == 'GET':
        financial_datas = get_list_or_404(YearSavingOptions)
        serializer = YearSavingOptionsSerializer(financial_datas, many=True)
        return Response(serializer.data)
        
        
        

# 적금 필터링 view 함수
@api_view(['GET'])
def list_saving_products(request):
    if request.method == 'GET':
        financial_data = get_list_or_404(SavingPrdt)
        serializer = SavingPrdtSerializer(financial_data, many=True)
        return Response(serializer.data)
    
    
@api_view(['GET'])
def list_saving_options(request):
    if request.method == 'GET':
        financial_datas = SavingOptions.objects.all().order_by('-intr_rate2')
        if financial_datas:
            serializer = SavingOptionsSerializer(financial_datas, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)



# 주택 담보 대출 view 함수
@api_view(['GET'])
def list_homeloan_products(request):
    if request.method == 'GET':
        
        financial_datas = HouseLoanPrdt.objects.all().order_by('-loan_lmt')
        if financial_datas:
            serializer = HouseLoanPrdtSerializer(financial_datas, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    
@api_view(['GET'])
def list_homeloan_options(request):
    if request.method == 'GET':
        financial_datas = HouseLoanOptions.objects.all().order_by('lend_rate_min')
        if financial_datas:
            serializer = HouseLoanOptionsSerializer(financial_datas, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

        
# 전세자금 대출 view 함수
@api_view(['GET'])
def list_depositloan_products(request):
    if request.method == 'GET':
        financial_datas = DepositLoanPrdt.objects.all().order_by('-loan_lmt')
        if financial_datas:
            serializer = DepositLoanPrdtSerializer(financial_datas, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def list_depositloan_options(request):
    if request.method == 'GET':
        financial_datas = DepositLoanOptions.objects.all().order_by('lend_rate_min')
        if financial_datas:
            serializer = DepositLoanOptionsSerializer(financial_datas, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)




# -----------------------------------------------------------------------------------------
# 단일조회
@api_view(['GET'])
def object_financial_products(request,fin_prdt_cd):
    if request.method == 'GET':
        financial_data = get_object_or_404(FinancialPrdt,fin_prdt_cd=fin_prdt_cd)
        serializer = FinancialPrdtSerializer(financial_data)
        return Response(serializer.data)
    
    
@api_view(['GET'])
def object_financial_options(request,fin_prdt_cd):
    if request.method == 'GET':
        financial_datas = FinancialOptions.objects.filter(product=fin_prdt_cd).order_by('-intr_rate2')
        if financial_datas:
            serializer = FinancialOptionsSerializer(financial_datas, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


# 연금 저축 필터링 view 함수
@api_view(['GET'])
def object_yearsaving_products(request,fin_prdt_cd):
    if request.method == 'GET':
        financial_data = get_object_or_404(YearSavingPrdt,fin_prdt_cd=fin_prdt_cd)

        if financial_data:
            serializer = YearSavingPrdtSerializer(financial_data)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    
@api_view(['GET'])
def object_yearsaving_options(request,fin_prdt_cd):
    if request.method == 'GET':
        financial_datas = get_list_or_404(YearSavingOptions,fin_prdt_cd=fin_prdt_cd)
        serializer = YearSavingOptionsSerializer(financial_datas, many=True)
        return Response(serializer.data)
        
        
        

# 적금 필터링 view 함수
@api_view(['GET'])
def object_saving_products(request,fin_prdt_cd):
    if request.method == 'GET':
        financial_data = get_object_or_404(SavingPrdt,fin_prdt_cd=fin_prdt_cd)
        serializer = SavingPrdtSerializer(financial_data)
        return Response(serializer.data)
    
    
@api_view(['GET'])
def object_saving_options(request,fin_prdt_cd):
    if request.method == 'GET':
        financial_datas =  SavingOptions.objects.filter(product=fin_prdt_cd).order_by('-intr_rate2')
        if financial_datas:
            serializer = SavingOptionsSerializer(financial_datas, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)



# 주택 담보 대출 view 함수
@api_view(['GET'])
def object_homeloan_products(request,fin_prdt_cd):
    if request.method == 'GET':    
        financial_datas = get_object_or_404(HouseLoanPrdt,fin_prdt_cd=fin_prdt_cd)
        if financial_datas:
            serializer = HouseLoanPrdtSerializer(financial_datas)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    
@api_view(['GET'])
def object_homeloan_options(request,fin_prdt_cd):
    if request.method == 'GET':
        financial_datas = HouseLoanOptions.objects.filter(product=fin_prdt_cd).order_by('lend_rate_min')
        if financial_datas:
            serializer = HouseLoanOptionsSerializer(financial_datas, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

        
# 전세자금 대출 view 함수
@api_view(['GET'])
def object_depositloan_products(request,fin_prdt_cd):
    if request.method == 'GET':
        financial_datas = get_object_or_404(DepositLoanPrdt,fin_prdt_cd=fin_prdt_cd)
        if financial_datas:
            serializer = DepositLoanPrdtSerializer(financial_datas)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def object_depositloan_options(request,fin_prdt_cd):
    if request.method == 'GET':
        financial_datas = DepositLoanOptions.objects.filter(product=fin_prdt_cd).order_by('lend_rate_min')
        if financial_datas:
            serializer = DepositLoanOptionsSerializer(financial_datas, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
