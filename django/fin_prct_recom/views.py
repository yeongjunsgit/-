from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
import requests
from .serializers import FinancialPrdtSerializer, FinancialOptionsSerializer
from .models import FinancialOptions,FinancialPrdt

# Create your views here.
@api_view(['GET'])
def save_deposit_products(request):
    # return Response({'data':'none'})
    api_key = '3fd1a070dff058dde65e087c621280b7'
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
                    'fin_prdt_cd': li.get('fin_prdt_cd'),
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


def fdrmDpstlists(request):
    return