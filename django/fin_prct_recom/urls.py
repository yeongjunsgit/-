from django.urls import path, include
from . import views

app_name='fin_prct_recom'
urlpatterns = [
    # 정기예금 상품 목록 DB에 저장
    
    # 됨
    path('save-financial-products/',views.save_financial_products, name="save_financial_products" ),
    
    # 됨
    path('delete/',views.delete, name="delete" ),
    
    # 됨
    path('save-yearsaving-products/',views.save_yearsaving_products, name="save_yearsaving_products" ),
    
    # 됨
    path('save-deposiloan-products/',views.save_deposiloan_products, name="save_deposiloan_products" ),
    # 됨
    path('save-saving-products/',views.save_saving_products, name="save_saving_products" ),

    # 안됨
    path('save-personalcreditloan-products/',views.save_personalcreditloan_products, name="save_personalcreditloan_products" ),

    # 됨
    path('save-houseloan-products/',views.save_houseloan_products, name="save_houseloan_products" ),

    # 됨
    path('save-fincompany-info/',views.save_fincompany_info, name="save_fincompany_info" ),
]
