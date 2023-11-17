from rest_framework import serializers
from .models import FinancialPrdt, FinancialOptions


class FinancialPrdtSerializer(serializers.ModelSerializer):
    class Meta():
        model = FinancialPrdt
        fields = '__all__'




class FinancialOptionsSerializer(serializers.ModelSerializer):
    # product 는 읽기 전용 필드로 지정한다.
    product = serializers.ReadOnlyField(source='FinancialOptions.fin_prdt_cd')
    class Meta:
        model = FinancialOptions
        # fields =  ('fin_prdt_cd_id', 'intr_rate_type_nm', 'intr_rate', 'intr_rate2', 'save_trm', )
        fields = '__all__'
