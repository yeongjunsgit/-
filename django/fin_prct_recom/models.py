from django.db import models

# Create your models here.

# 정기 예금 상품
class FinancialPrdt(models.Model):                                      
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
    dcls_end_dat = models.CharField(max_length=20, null=True)                      # dcls_end_dat - 공시 종료일
    # dcls_month = models.CharField(max_length=10)                        # dcls_month - 공시 제출월 [YYYYMM]
    # dcls_strt_day = models.CharField(max_length=20)                     # dcls_strt_day - 공시 시작일
    # fin_co_subm_day = models.CharField(max_length=20,null=True)                   # 금융회사 제출일 [YYYYMMDDHH24MI]
    
# 정기 예금 옵션
class FinancialOptions(models.Model):
    product = models.ForeignKey(FinancialPrdt,on_delete=models.CASCADE,related_name="option") # 금융상품 코드
    intr_rate_type = models.CharField(max_length=200)       # 저축 금리 유형
    intr_rate_type_nm = models.CharField(max_length=200, null=True)    # 저축 금리 유형명
    save_trm = models.IntegerField()             # 저축 기간 [단위: 개월]
    intr_rate = models.FloatField(null=True)            # 저축 금리 [소수점 2자리]
    intr_rate2 = models.FloatField(null=True)           # 최고 우대금리 [소수점 2자리]

# 추가 모델 작성, makemigration 안해서 주석처리 해놓은 상태

# 연금 저축 상품
class YearSavingPrdt(models.Model):
    fin_co_no = models.CharField(max_length=200)                #금융회사 코드
    kor_co_nm = models.CharField(max_length=200)                #금융회사 명
    fin_prdt_cd = models.CharField(max_length=200, primary_key=True)         #금융상품 코드
    fin_prdt_nm = models.CharField(max_length=200)              #금융 상품명
    join_way = models.CharField(max_length=200, null=True)      #가입 방법
    pnsn_kind = models.CharField(max_length=200, null=True)     #연금종류
    pnsn_kind_nm = models.CharField(max_length=200, null=True)  #연금종류명
    prdt_type = models.CharField(max_length=200, null=True)     #상품유형
    prdt_type_nm = models.CharField(max_length=200, null=True)  #상품유형명
    dcls_rate = models.CharField(max_length=20, null=True)     #공시이율 [소수점 2자리]
    guar_rate = models.CharField(max_length=20, null=True)     #최저 보증이율
    btrm_prft_rate_1 = models.FloatField(null=True)         #과거 수익률1(전년도) [소수점 2자리]
    btrm_prft_rate_2 = models.FloatField(null=True)         #과거 수익률2(전전년도) [소수점 2자리]
    btrm_prft_rate_3 = models.FloatField(null=True)         #과거 수익률3(전전전년도) [소수점 2자리]
    etc = models.CharField(max_length=200, null=True)           #기타사항
    sale_co = models.CharField(max_length=1000, null=True)       #판매사
    dcls_end_day = models.CharField(max_length=20, null=True)         #공시 종료일
    # mntn_cnt = models.CharField(max_length=200, null=True)      #유지건수[단위: 건] 또는 설정액 [단위: 원]
    # sale_strt_day = models.CharField(max_length=20,null=True)             #판매 개시일
    # dcls_strt_day = models.CharField(max_length=20)            #공시 시작일
    # dcls_month = models.CharField(max_length=200)               #공시 제출월 [YYYYMM]
    # fin_co_subm_day = models.CharField(max_length=20, null=True)      #금융회사제출일

# 연금저축옵션
class YearSavingOptions(models.Model):
    product = models.ForeignKey(YearSavingPrdt,on_delete=models.CASCADE,related_name="option")      # 상품 옵션
    fin_co_no = models.CharField(max_length=20, null=True)      # 금융회사 코드
    fin_prdt_cd = models.CharField(max_length=20, null=True)    # 금융상품 코드
    pnsn_recp_trm = models.CharField(max_length=20, null=True)  # 연금수령 기간
    pnsn_entr_age = models.CharField(max_length=20, null=True)  # 연금 가입 나이
    mon_paym_atm = models.CharField(max_length=20, null=True)   # 월 납입 금액
    paym_prd = models.CharField(max_length=20, null=True)       # 납입기간
    pnsn_strt_age = models.CharField(max_length=20, null=True)  # 연금 개시나이
    pnsn_recp_amt = models.IntegerField(null=True)  # 연금 수령액
    
    # dcls_month = models.CharField(max_length=20, null=True)     # 시작년도달?
    # pnsn_recp_trm_nm = models.CharField(max_length=20, null=True)
    # mon_paym_atm_nm = models.CharField(max_length=20, null=True)
    # pnsn_entr_age_nm = models.CharField(max_length=20, null=True)
    # paym_prd_nm = models.CharField(max_length=20, null=True)
    # pnsn_strt_age_nm = models.CharField(max_length=20, null=True)


# 전세 자금 대출 상품
class DepositLoanPrdt(models.Model):
    fin_co_no = models.CharField(max_length=200)                    # 금융회사 코드 1
    kor_co_nm = models.CharField(max_length=200,null=True)          # 금융회사 명
    fin_prdt_cd = models.CharField(max_length=200, primary_key=True) # 금융상품 코드 1
    fin_prdt_nm = models.CharField(max_length=200,null=True)        # 금융 상품명
    join_way = models.CharField(max_length=200,null=True)           # 가입 방법
    loan_inci_expn = models.CharField(max_length=500,null=True)     # 대출 부대비용
    erly_rpay_fee = models.CharField(max_length=200,null=True)      # 중도상환 수수료
    dly_rate = models.CharField(max_length=200,null=True)           # 연체 이자율
    loan_lmt = models.CharField(max_length=200,null=True)           # 대출한도
    dcls_end_day = models.CharField(max_length=20,null=True)       # 공시 종료일
    # dcls_month = models.CharField(max_length=20)                   # 공시 제출월 [YYYYMM] 1
    # dcls_strt_day = models.CharField(max_length=20,null=True)      # 공시 시작일
    # fin_co_subm_day = models.CharField(max_length=20,null=True)    # 금융회사 제출일 [YYYYMMDDHH24MI]


# 전세 자금 대출 옵션

class DepositLoanOptions(models.Model):
    product = models.ForeignKey(DepositLoanPrdt,on_delete=models.CASCADE,related_name="option")      # 상품 옵션
    rpay_type_nm = models.CharField(max_length=200)                   # 대출상환유형 **
    lend_rate_type_nm = models.CharField(max_length=200,null=True)    # 대출금리유형
    lend_rate_min = models.FloatField(null=True)        # 대출금리_최저 [소수점 2자리]
    lend_rate_max = models.FloatField(null=True)        # 대출금리_최고 [소수점 2자리]
    lend_rate_avg = models.CharField(max_length=20,null=True)        # 전월 취급 평균금리 [소수점 2자리]
    # rpay_type = models.CharField(max_length=200,null=True)            # 대출상환유형 코드
    # lend_rate_type = models.CharField(max_length=200,null=True)       # 대출금리유형 코드


# # 적금 상품 
class SavingPrdt(models.Model):
    fin_co_no = models.CharField(max_length=200,null=True)              # 금융회사 코드
    kor_co_nm = models.CharField(max_length=200,null=True)              # 금융회사 명
    fin_prdt_cd = models.CharField(max_length=200,primary_key=True)     # 금융상품 코드
    fin_prdt_nm = models.CharField(max_length=200,null=True)            # 금융 상품명
    join_way = models.CharField(max_length=200,null=True)               # 가입 방법
    mtrt_int = models.CharField(max_length=200,null=True)               # 만기 후 이자율
    spcl_cnd = models.CharField(max_length=200,null=True)               # 우대조건
    join_deny = models.CharField(max_length=200,null=True)              # 가입제한
    join_member = models.CharField(max_length=200,null=True)            # 가입대상
    etc_note = models.CharField(max_length=200,null=True)               # 기타 유의사항
    max_limit = models.CharField(max_length=200,null=True)              # 최고한도
    dcls_end_day = models.CharField(max_length=20,null=True)           # 공시 종료일
    # dcls_month   = models.CharField(max_length=20,null=True)           # 공시 제출월 [YYYYMM]
    # dcls_strt_day = models.CharField(max_length=20,null=True)          # 공시 시작일
    # fin_co_subm_day = models.CharField(max_length=20,null=True)        # 금융회사제출일[YYYYMMDDHH24MI]



# # 적금 옵션
class SavingOptions(models.Model):
    product = models.ForeignKey(SavingPrdt,on_delete=models.CASCADE,related_name='option') # 금융 상품 코드
    intr_rate_type = models.CharField(max_length=200,null=True)         # 저축 금리 유형
    intr_rate_type_nm = models.CharField(max_length=200,null=True)      # 저축 금리 유형명
    save_trm = models.IntegerField(null=True)               # 저축 기간 [단위: 개월]
    intr_rate = models.CharField(max_length=20,null=True)              # 저축 금리 [소수점 2자리]
    intr_rate2 = models.FloatField(null=True)             # 최고 우대금리 [소수점 2자리]
    # rsrv_type = models.CharField(max_length=200,null=True)              # 적립 유형
    # rsrv_type_nm = models.CharField(max_length=200,null=True)           # 적립 유형명



## 데이터 문제로 개인 신용 대출은 사용 불가능
# # 개인 신용 대출
# class PersonalCreditLoanPrdt(models.Model):
#     dcls_month  = models.CharField(max_length=200)              # 공시 제출월 [YYYYMM] 1
#     fin_co_no  = models.CharField(max_length=200)               # 금융회사 코드 1
#     kor_co_nm = models.CharField(max_length=200,null=True)      # 금융회사 명
#     fin_prdt_cd = models.CharField(max_length=200, primary_key=True)        # 금융상품 코드 1
#     fin_prdt_nm = models.CharField(max_length=200,null=True)    # 금융 상품명
#     join_way = models.CharField(max_length=200,null=True)       # 가입 방법
#     crdt_prdt_type = models.CharField(max_length=200,null=True) # 대출종류 코드
#     crdt_prdt_type_nm = models.CharField(max_length=200,null=True)      # 대출종류명
#     cb_name = models.CharField(max_length=200,null=True)        # CB 회사명
#     dcls_strt_day = models.CharField(max_length=20,null=True)  # 공시 시작일
#     dcls_end_day = models.CharField(max_length=20,null=True)   # 공시 종료일
#     fin_co_subm_day = models.CharField(max_length=20,null=True)# 금융회사 제출일 [YYYYMMDDHH24MI]


# # 개인 신용 대출 옵션
# class PersonalCreditLoanOptions(models.Model):
#     product = models.ForeignKey(PersonalCreditLoanPrdt,on_delete=models.CASCADE,related_name='option')  # 금융상품 코드
#     crdt_lend_rate_type = models.CharField(max_length=20,null=True)    # 금리구분 코드
#     crdt_lend_rate_type_nm = models.CharField(max_length=20,null=True)     # 금리구분
#     crdt_grad_1 = models.CharField(max_length=20,null=True)    # 900점 초과 [소수점 2자리]
#     crdt_grad_4 = models.CharField(max_length=20,null=True)    # 801~900점 [소수점 2자리]
#     crdt_grad_5 = models.CharField(max_length=20,null=True)    # 701~800점 [소수점 2자리]
#     crdt_grad_6 = models.CharField(max_length=20,null=True)    # 601~700점 [소수점 2자리]
#     crdt_grad_10 = models.CharField(max_length=20,null=True)   # 501~600점 [소수점 2자리]
#     crdt_grad_11 = models.CharField(max_length=20,null=True)   # 401~500점 [소수점 2자리]
#     crdt_grad_12 = models.CharField(max_length=20,null=True)   # 301~400점 [소수점 2자리]
#     crdt_grad_13 = models.CharField(max_length=20,null=True)   # 300점 이하 [소수점 2자리]
#     crdt_grad_avg = models.CharField(max_length=20,null=True)  # 평균 금리 [소수점 2자리]    
    
    

# 주택 담보 대출
class HouseLoanPrdt(models.Model):
    fin_co_no = models.CharField(max_length=200)                    # 금융회사 코드 ***
    kor_co_nm = models.CharField(max_length=200,null=True)          # 금융회사 명
    fin_prdt_cd = models.CharField(max_length=200,primary_key=True)  # 금융상품 코드 ***
    fin_prdt_nm = models.CharField(max_length=200,null=True)        # 금융 상품명
    join_way = models.CharField(max_length=200,null=True)           # 가입 방법
    loan_inci_expn = models.CharField(max_length=200,null=True)     # 대출 부대비용
    erly_rpay_fee = models.CharField(max_length=200,null=True)      # 중도상환 수수료
    dly_rate = models.CharField(max_length=200,null=True)           # 연체 이자율
    loan_lmt = models.CharField(max_length=200,null=True)                       # 대출한도
    # dcls_month = models.CharField(max_length=6)                   # 공시 제출월 [YYYYMM] ***
    # dcls_strt_day = models.CharField(max_length=20,null=True)      # 공시 시작일
    # dcls_end_day = models.CharField(max_length=20,null=True)       # 공시 종료일
    # fin_co_subm_day = models.CharField(max_length=20,null=True)    # 금융회사 제출일 [YYYYMMDDHH24MI]


# 주택 담보 대출 옵션
class HouseLoanOptions(models.Model):
    product = models.ForeignKey(HouseLoanPrdt,on_delete=models.CASCADE,related_name='option')  # 금융상품 코드
    rpay_type_nm = models.CharField(max_length=200)         # 대출상환유형 **
    lend_rate_type_nm = models.CharField(max_length=200,null=True)  # 대출금리유형
    lend_rate_min = models.FloatField(null=True)  # 대출금리_최저 [소수점 2자리]
    lend_rate_max = models.FloatField(null=True)  # 대출금리_최고 [소수점 2자리]
    lend_rate_avg = models.CharField(max_length=10,null=True)  # 전월 취급 평균금리 [소수점 2자리]
    # mrtg_type = models.CharField(max_length=200,null=True)  # 담보유형 코드
    # mrtg_type_nm = models.CharField(max_length=200,null=True)  # 담보유형
    # rpay_type = models.CharField(max_length=200,null=True)  # 대출상환유형 코드
    # lend_rate_type = models.CharField(max_length=200,null=True)  # 대출금리유형 코드
    
# 금융회사 정보 
class FinCompanyInfo(models.Model):
    dcls_month = models.CharField(max_length=6,null=True)         # 공시 제출월 [YYYYMM]**
    fin_co_no = models.CharField(max_length=200,primary_key=True)   # 금융회사코드**
    kor_co_nm = models.CharField(max_length=200,null=True)          # 금융회사 명
    dcls_chrg_man = models.CharField(max_length=200,null=True)      # 공시담당자
    homp_url = models.CharField(max_length=200,null=True)           # 홈페이지주소
    cal_tel = models.CharField(max_length=20,null=True)            # 콜센터전화번호


# # 금융 회사 옵션
class FinCompanyOptions(models.Model):
    product = models.ForeignKey(FinCompanyInfo,on_delete=models.CASCADE,related_name='option') # 금융회사코드
    area_cd = models.CharField(max_length=20,null=True)            # 지역구분
    area_nm = models.CharField(max_length=20,null=True)            # 지역이름
    exis_yn = models.CharField(max_length=5,null=True)            # 점포소재여부
    


from django.conf import settings
class UserJoinPrdt(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    user_age = models.IntegerField(null=True)
    product = models.TextField(null=True)
    product_type = models.TextField(null=True)
