# Generated by Django 4.2.4 on 2023-11-22 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fin_prct_recom', '0002_alter_depositloanoptions_lend_rate_max_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='houseloanprdt',
            name='loan_lmt',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
