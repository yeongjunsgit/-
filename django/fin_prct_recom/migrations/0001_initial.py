# Generated by Django 4.2.4 on 2023-11-22 01:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DepositLoanPrdt',
            fields=[
                ('dcls_month', models.CharField(max_length=20)),
                ('fin_co_no', models.CharField(max_length=200)),
                ('kor_co_nm', models.CharField(max_length=200, null=True)),
                ('fin_prdt_cd', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('fin_prdt_nm', models.CharField(max_length=200, null=True)),
                ('join_way', models.CharField(max_length=200, null=True)),
                ('loan_inci_expn', models.CharField(max_length=500, null=True)),
                ('erly_rpay_fee', models.CharField(max_length=200, null=True)),
                ('dly_rate', models.CharField(max_length=200, null=True)),
                ('loan_lmt', models.CharField(max_length=200, null=True)),
                ('dcls_strt_day', models.CharField(max_length=20, null=True)),
                ('dcls_end_day', models.CharField(max_length=20, null=True)),
                ('fin_co_subm_day', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FinancialPrdt',
            fields=[
                ('dcls_month', models.CharField(max_length=10)),
                ('fin_co_no', models.CharField(max_length=100)),
                ('kor_co_nm', models.CharField(max_length=200)),
                ('fin_prdt_cd', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('fin_prdt_nm', models.CharField(max_length=200)),
                ('join_way', models.CharField(max_length=200, null=True)),
                ('mtrt_int', models.CharField(max_length=200)),
                ('spcl_cnd', models.CharField(max_length=200, null=True)),
                ('join_deny', models.IntegerField(null=True)),
                ('join_member', models.CharField(max_length=1000, null=True)),
                ('etc_note', models.CharField(max_length=200, null=True)),
                ('max_limit', models.CharField(max_length=200, null=True)),
                ('dcls_strt_day', models.CharField(max_length=20)),
                ('dcls_end_dat', models.CharField(max_length=20, null=True)),
                ('fin_co_subm_day', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FinCompanyInfo',
            fields=[
                ('dcls_month', models.CharField(max_length=6, null=True)),
                ('fin_co_no', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('kor_co_nm', models.CharField(max_length=200, null=True)),
                ('dcls_chrg_man', models.CharField(max_length=200, null=True)),
                ('homp_url', models.CharField(max_length=200, null=True)),
                ('cal_tel', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HouseLoanPrdt',
            fields=[
                ('dcls_month', models.CharField(max_length=6)),
                ('fin_co_no', models.CharField(max_length=200)),
                ('kor_co_nm', models.CharField(max_length=200, null=True)),
                ('fin_prdt_cd', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('fin_prdt_nm', models.CharField(max_length=200, null=True)),
                ('join_way', models.CharField(max_length=200, null=True)),
                ('loan_inci_expn', models.CharField(max_length=200, null=True)),
                ('erly_rpay_fee', models.CharField(max_length=200, null=True)),
                ('dly_rate', models.CharField(max_length=200, null=True)),
                ('loan_lmt', models.CharField(max_length=200, null=True)),
                ('dcls_strt_day', models.CharField(max_length=20, null=True)),
                ('dcls_end_day', models.CharField(max_length=20, null=True)),
                ('fin_co_subm_day', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalCreditLoanPrdt',
            fields=[
                ('dcls_month', models.CharField(max_length=200)),
                ('fin_co_no', models.CharField(max_length=200)),
                ('kor_co_nm', models.CharField(max_length=200, null=True)),
                ('fin_prdt_cd', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('fin_prdt_nm', models.CharField(max_length=200, null=True)),
                ('join_way', models.CharField(max_length=200, null=True)),
                ('crdt_prdt_type', models.CharField(max_length=200, null=True)),
                ('crdt_prdt_type_nm', models.CharField(max_length=200, null=True)),
                ('cb_name', models.CharField(max_length=200, null=True)),
                ('dcls_strt_day', models.CharField(max_length=20, null=True)),
                ('dcls_end_day', models.CharField(max_length=20, null=True)),
                ('fin_co_subm_day', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SavingPrdt',
            fields=[
                ('dcls_month', models.CharField(max_length=20, null=True)),
                ('fin_co_no', models.CharField(max_length=200, null=True)),
                ('kor_co_nm', models.CharField(max_length=200, null=True)),
                ('fin_prdt_cd', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('fin_prdt_nm', models.CharField(max_length=200, null=True)),
                ('join_way', models.CharField(max_length=200, null=True)),
                ('mtrt_int', models.CharField(max_length=200, null=True)),
                ('spcl_cnd', models.CharField(max_length=200, null=True)),
                ('join_deny', models.CharField(max_length=200, null=True)),
                ('join_member', models.CharField(max_length=200, null=True)),
                ('etc_note', models.CharField(max_length=200, null=True)),
                ('max_limit', models.CharField(max_length=200, null=True)),
                ('dcls_strt_day', models.CharField(max_length=20, null=True)),
                ('dcls_end_day', models.CharField(max_length=20, null=True)),
                ('fin_co_subm_day', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='YearSavingPrdt',
            fields=[
                ('dcls_month', models.CharField(max_length=200)),
                ('fin_co_no', models.CharField(max_length=200)),
                ('kor_co_nm', models.CharField(max_length=200)),
                ('fin_prdt_cd', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('fin_prdt_nm', models.CharField(max_length=200)),
                ('join_way', models.CharField(max_length=200, null=True)),
                ('pnsn_kind', models.CharField(max_length=200, null=True)),
                ('pnsn_kind_nm', models.CharField(max_length=200, null=True)),
                ('sale_strt_day', models.CharField(max_length=20, null=True)),
                ('mntn_cnt', models.CharField(max_length=200, null=True)),
                ('prdt_type', models.CharField(max_length=200, null=True)),
                ('prdt_type_nm', models.CharField(max_length=200, null=True)),
                ('dcls_rate', models.CharField(max_length=20, null=True)),
                ('guar_rate', models.CharField(max_length=20, null=True)),
                ('btrm_prft_rate_1', models.CharField(max_length=20, null=True)),
                ('btrm_prft_rate_2', models.CharField(max_length=20, null=True)),
                ('btrm_prft_rate_3', models.CharField(max_length=20, null=True)),
                ('etc', models.CharField(max_length=200, null=True)),
                ('sale_co', models.CharField(max_length=1000, null=True)),
                ('dcls_strt_day', models.CharField(max_length=20)),
                ('dcls_end_day', models.CharField(max_length=20, null=True)),
                ('fin_co_subm_day', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='YearSavingOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.CharField(max_length=20, null=True)),
                ('fin_co_no', models.CharField(max_length=20, null=True)),
                ('fin_prdt_cd', models.CharField(max_length=20, null=True)),
                ('pnsn_recp_trm', models.CharField(max_length=20, null=True)),
                ('pnsn_recp_trm_nm', models.CharField(max_length=20, null=True)),
                ('pnsn_entr_age', models.CharField(max_length=20, null=True)),
                ('pnsn_entr_age_nm', models.CharField(max_length=20, null=True)),
                ('mon_paym_atm', models.CharField(max_length=20, null=True)),
                ('mon_paym_atm_nm', models.CharField(max_length=20, null=True)),
                ('paym_prd', models.CharField(max_length=20, null=True)),
                ('paym_prd_nm', models.CharField(max_length=20, null=True)),
                ('pnsn_strt_age', models.CharField(max_length=20, null=True)),
                ('pnsn_strt_age_nm', models.CharField(max_length=20, null=True)),
                ('pnsn_recp_amt', models.CharField(max_length=20, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='option', to='fin_prct_recom.yearsavingprdt')),
            ],
        ),
        migrations.CreateModel(
            name='UserJoinPrdt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_age', models.IntegerField(null=True)),
                ('product', models.TextField(null=True)),
                ('product_type', models.TextField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SavingOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intr_rate_type', models.CharField(max_length=200, null=True)),
                ('intr_rate_type_nm', models.CharField(max_length=200, null=True)),
                ('rsrv_type', models.CharField(max_length=200, null=True)),
                ('rsrv_type_nm', models.CharField(max_length=200, null=True)),
                ('save_trm', models.CharField(max_length=20, null=True)),
                ('intr_rate', models.CharField(max_length=20, null=True)),
                ('intr_rate2', models.CharField(max_length=20, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='option', to='fin_prct_recom.savingprdt')),
            ],
        ),
        migrations.CreateModel(
            name='PersonalCreditLoanOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crdt_lend_rate_type', models.CharField(max_length=20, null=True)),
                ('crdt_lend_rate_type_nm', models.CharField(max_length=20, null=True)),
                ('crdt_grad_1', models.CharField(max_length=20, null=True)),
                ('crdt_grad_4', models.CharField(max_length=20, null=True)),
                ('crdt_grad_5', models.CharField(max_length=20, null=True)),
                ('crdt_grad_6', models.CharField(max_length=20, null=True)),
                ('crdt_grad_10', models.CharField(max_length=20, null=True)),
                ('crdt_grad_11', models.CharField(max_length=20, null=True)),
                ('crdt_grad_12', models.CharField(max_length=20, null=True)),
                ('crdt_grad_13', models.CharField(max_length=20, null=True)),
                ('crdt_grad_avg', models.CharField(max_length=20, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='option', to='fin_prct_recom.personalcreditloanprdt')),
            ],
        ),
        migrations.CreateModel(
            name='HouseLoanOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mrtg_type', models.CharField(max_length=200, null=True)),
                ('mrtg_type_nm', models.CharField(max_length=200, null=True)),
                ('rpay_type', models.CharField(max_length=200, null=True)),
                ('rpay_type_nm', models.CharField(max_length=200)),
                ('lend_rate_type', models.CharField(max_length=200, null=True)),
                ('lend_rate_type_nm', models.CharField(max_length=200, null=True)),
                ('lend_rate_min', models.CharField(max_length=10, null=True)),
                ('lend_rate_max', models.CharField(max_length=10, null=True)),
                ('lend_rate_avg', models.CharField(max_length=10, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='option', to='fin_prct_recom.houseloanprdt')),
            ],
        ),
        migrations.CreateModel(
            name='FinCompanyOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_cd', models.CharField(max_length=20, null=True)),
                ('area_nm', models.CharField(max_length=20, null=True)),
                ('exis_yn', models.CharField(max_length=5, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='option', to='fin_prct_recom.fincompanyinfo')),
            ],
        ),
        migrations.CreateModel(
            name='FinancialOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intr_rate_type', models.CharField(max_length=200)),
                ('intr_rate_type_nm', models.CharField(max_length=200, null=True)),
                ('save_trm', models.IntegerField()),
                ('intr_rate', models.CharField(max_length=10, null=True)),
                ('intr_rate2', models.CharField(max_length=10, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='option', to='fin_prct_recom.financialprdt')),
            ],
        ),
        migrations.CreateModel(
            name='DepositLoanOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rpay_type', models.CharField(max_length=200, null=True)),
                ('rpay_type_nm', models.CharField(max_length=200)),
                ('lend_rate_type', models.CharField(max_length=200, null=True)),
                ('lend_rate_type_nm', models.CharField(max_length=200, null=True)),
                ('lend_rate_min', models.CharField(max_length=20, null=True)),
                ('lend_rate_max', models.CharField(max_length=20, null=True)),
                ('lend_rate_avg', models.CharField(max_length=20, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='option', to='fin_prct_recom.depositloanprdt')),
            ],
        ),
    ]
