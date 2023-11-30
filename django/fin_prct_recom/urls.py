from django.urls import path, include
from . import views

app_name='fin_prct_recom'
urlpatterns = [
    # 정기예금 상품 목록 DB에 저장
    
    path('save-financial-products/',views.save_financial_products, name="save_financial_products" ),
    path('save-yearsaving-products/',views.save_yearsaving_products, name="save_yearsaving_products" ),
    path('save-depositloan-products/',views.save_depositloan_products, name="save_deposiloan_products" ),
    path('save-saving-products/',views.save_saving_products, name="save_saving_products" ),
    path('save-homeloan-products/',views.save_homeloan_products, name="save_homeloan_products" ),
    path('save-fincompany-info/',views.save_fincompany_info, name="save_fincompany_info" ),
    path('delete/',views.delete, name="delete" ),

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
    

    
    path('object_financial_products/<str:fin_prdt_cd>',views.object_financial_products),
    path('object_financial_options/<str:fin_prdt_cd>',views.object_financial_options),
    path('object_yearsaving_products/<str:fin_prdt_cd>',views.object_yearsaving_products),
    path('object_yearsaving_options/<str:fin_prdt_cd>',views.object_yearsaving_options),
    path('object_saving_products/<str:fin_prdt_cd>',views.object_saving_products),
    path('object_saving_options/<str:fin_prdt_cd>',views.object_saving_options),
    path('object_homeloan_products/<str:fin_prdt_cd>',views.object_homeloan_products),
    path('object_homeloan_options/<str:fin_prdt_cd>',views.object_homeloan_options),
    path('object_depositloan_products/<str:fin_prdt_cd>',views.object_depositloan_products),
    path('object_depositloan_options/<str:fin_prdt_cd>',views.object_depositloan_options),



    
]
