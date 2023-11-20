from rest_framework import serializers
from .models import FinancialPrdt, FinancialOptions,YearSavingPrdt,YearSavingOptions, DepositLoanPrdt,DepositLoanOptions, SavingPrdt,SavingOptions, PersonalCreditLoanPrdt, PersonalCreditLoanOptions,HouseLoanPrdt,HouseLoanOptions,FinCompanyInfo,FinCompanyOptions


class FinancialPrdtSerializer(serializers.ModelSerializer):
    class Meta():
        model = FinancialPrdt
        fields = '__all__'




class FinancialOptionsSerializer(serializers.ModelSerializer):
    # product 는 읽기 전용 필드로 지정한다.
    product = serializers.ReadOnlyField(source='FinancialOptions.product')
    class Meta:
        model = FinancialOptions
        # fields =  ('fin_prdt_cd_id', 'intr_rate_type_nm', 'intr_rate', 'intr_rate2', 'save_trm', )
        fields = '__all__'


class YearSavingPrdtSerializer(serializers.ModelSerializer):
    class Meta():
        model = YearSavingPrdt
        fields = '__all__'

class YearSavingOptionsSerializer(serializers.ModelSerializer):
    # product 는 읽기 전용 필드로 지정한다.
    product = serializers.ReadOnlyField(source='YearSavingOptions.product')
    class Meta():
        model = YearSavingOptions
        fields = '__all__'

class DepositLoanPrdtSerializer(serializers.ModelSerializer):
    class Meta():
        model = DepositLoanPrdt
        fields = '__all__'

class DepositLoanOptionsSerializer(serializers.ModelSerializer):
    # product 는 읽기 전용 필드로 지정한다.
    product = serializers.ReadOnlyField(source='DepositLoanOptions.product')
    class Meta():
        model = DepositLoanOptions
        fields = '__all__'

class SavingPrdtSerializer(serializers.ModelSerializer):
    class Meta():
        model = SavingPrdt
        fields = '__all__'

class SavingOptionsSerializer(serializers.ModelSerializer):
    # product 는 읽기 전용 필드로 지정한다.
    product = serializers.ReadOnlyField(source='SavingOptions.product')
    class Meta():
        model = SavingOptions
        fields = '__all__'

class PersonalCreditLoanPrdtSerializer(serializers.ModelSerializer):
    class Meta():
        model = PersonalCreditLoanPrdt
        fields = '__all__'

class PersonalCreditLoanOptionsSerializer(serializers.ModelSerializer):
    # product 는 읽기 전용 필드로 지정한다.
    product = serializers.ReadOnlyField(source='PersonalCreditLoanOptions.product')
    class Meta():
        model = PersonalCreditLoanOptions
        fields = '__all__'

class HouseLoanPrdtSerializer(serializers.ModelSerializer):
    class Meta():
        model = HouseLoanPrdt
        fields = '__all__'

class HouseLoanOptionsSerializer(serializers.ModelSerializer):
    # product 는 읽기 전용 필드로 지정한다.
    product = serializers.ReadOnlyField(source='HouseLoanOptions.product')
    class Meta():
        model = HouseLoanOptions
        fields = '__all__'

class FinCompanyInfoSerializer(serializers.ModelSerializer):
    class Meta():
        model = FinCompanyInfo
        fields = '__all__'

class FinCompanyOptionSerializer(serializers.ModelSerializer):
    # product 는 읽기 전용 필드로 지정한다.
    product = serializers.ReadOnlyField(source='FinCompanyOption.product')
    class Meta():
        model = FinCompanyOptions
        fields = '__all__'









