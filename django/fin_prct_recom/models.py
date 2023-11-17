from django.db import models

# Create your models here.

# 정기 예금 상품
class FinancialPrdt(models.Model):                                      
    dcls_month = models.CharField(max_length=10)                        # dcls_month - 공시 제출월 [YYYYMM]
    fin_co_no = models.CharField(max_length=100)                        # fin_co_no - 금융회사 코드
    kor_co_nm = models.CharField(max_length=200)                        # kor_co_nm - 금융회사 명
    fin_prdt_cd = models.CharField(max_length=200,primary_key=True)     # fin_prdt_cd(pk) - 금융상품 코드
    fin_prdt_nm = models.CharField(max_length=200)                      # fin_prdt_nm - 금융 상품명
    join_way = models.CharField(max_length=200,null=True)                         # join_way - 가입방법
    mtrt_int = models.CharField(max_length=200)                         # mtrt_int - 만기 후 이자율
    spcl_cnd = models.CharField(max_length=200,null=True)                         # spcl_cnd - 우대조건
    join_deny = models.IntegerField(null=True)                                   # join_deny - 가입제한
    join_member = models.CharField(max_length=1000, null=True)                     # join_member - 가입대상
    etc_note = models.CharField(max_length=200, null=True)                         # etc_note - 기타 유의 사항
    max_limit = models.CharField(max_length=200, null=True)                        # max_limit - 최고한도
    dcls_strt_day = models.CharField(max_length=20)                     # dcls_strt_day - 공시 시작일
    dcls_end_dat = models.CharField(max_length=20, null=True)                      # dcls_end_dat - 공시 종료일
    fin_co_subm_day = models.CharField(max_length=20,null=True)                   # 금융회사 제출일 [YYYYMMDDHH24MI]
    
# 정기 예금 옵션
class FinancialOptions(models.Model):
    product = models.ForeignKey(FinancialPrdt,on_delete=models.CASCADE,related_name="option") # 금융상품 코드
    intr_rate_type = models.CharField(max_length=200)       # 저축 금리 유형
    intr_rate_type_nm = models.CharField(max_length=200, null=True)    # 저축 금리 유형명
    save_trm = models.CharField(max_length=200)             # 저축 기간 [단위: 개월]
    intr_rate = models.CharField(max_length=200,null=True)            # 저축 금리 [소수점 2자리]
    intr_rate2 = models.CharField(max_length=200,null=True)           # 최고 우대금리 [소수점 2자리]






# class SavingPrdt(models.Model):                     # 연금 저축 상품
#     dcls_month = models.CharField(max_length=200)   # dcls_month     공시 제출월 [YYYYMM]
#     fin_co_no = models.CharField(max_length=200)    # fin_co_no     금융회사 코드
#     kor_co_nm = models.CharField(max_length=200)    # kor_co_nm    금융회사 명
#     fin_prdt_cd = models.CharField(max_length=200, primary_key=True)   # fin_prdt_cd    금융상품 코드
    # fin_prdt_nm    금융 상품명
    # join_way    가입 방법
    # pnsn_kind    연금종류
    # pnsn_kind_nm    연금종류명
    # sale_strt_day    판매 개시일
    # mntn_cnt        유지건수[단위: 건] 또는 설정액 [단위: 원]
    # prdt_type    상품유형
    # prdt_type_nm    상품유형명
    # dcls_rate    공시이율 [소수점 2자리]
    # guar_rate    최저 보증이율
    # btrm_prft_rate_1    과거 수익률1(전년도) [소수점 2자리]
    # btrm_prft_rate_2    과거 수익률2(전전년도) [소수점 2자리]
    # btrm_prft_rate_3    과거 수익률3(전전전년도) [소수점 2자리]
    # etc    기타사항
    # sale_co    판매사
    # dcls_strt_day    공시 시작일
    # dcls_end_day    공시 종료일
    # fin_co_subm_day 금융회사제출일[YYYYMMDDHH24MI]