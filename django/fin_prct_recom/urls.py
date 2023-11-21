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

    # 정기 예금 필터링 URL
    path('list-financial-products/',views.list_financial_products),
    path('list-financial-options/',views.list_financial_options),
    
    # 연금 저축 필터링 URL
    path('list-yearsaving-products/',views.list_yearsaving_products),
    path('list-yearsaving-options/',views.list_yearsaving_options),
    
    # 적금 필터링 URL
    path('list-saving-products/',views.list_saving_products),
    path('list-saving-options/',views.list_saving_options),
    
    # 주택 담보 대출 필터링 URL
    path('list-homeloan-products/',views.list_homeloan_products),
    path('list-homeloan-options/',views.list_homeloan_options),


    # 전세 자금 대출 필터링 URL
    path('list-depositloan-products/',views.list_depositloan_products),
    path('list-depositloan-options/',views.list_depositloan_options),
    
    # 비슷한 나이대 상품 정리 URL
    # path('same_age_filter/',views.same_age_filter),
    
]
