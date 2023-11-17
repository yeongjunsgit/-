from django.urls import path, include
from . import views

app_name='fin_prct_recom'
urlpatterns = [
    # 정기예금 상품 목록 DB에 저장
    path('save-deposit-products/',views.save_deposit_products, name="save_deposit_products" ),
    path('fdrmDpstApi/list/', views.fdrmDpstlists),
]
