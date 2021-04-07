# Generated by Django 3.1.7 on 2021-04-06 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yfcases', '0008_clicklist'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObjectBuild',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectBuildAddress', models.CharField(blank=True, max_length=100, null=True, verbose_name='地址')),
                ('objectBuildTotalPrice', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=10, null=True, verbose_name='總價(NT)')),
                ('objectBuildBuildArea', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='建坪(坪)')),
                ('objectBuildHouseAge', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True, verbose_name='屋齡(年)')),
                ('objectBuildFloorHeight', models.CharField(blank=True, max_length=100, null=True, verbose_name='樓高')),
                ('objectBuildStatus', models.CharField(blank=True, max_length=100, null=True, verbose_name='狀態')),
                ('objectBuildTransactionDate', models.CharField(blank=True, max_length=100, null=True, verbose_name='成交日期')),
                ('objectBuildUrl', models.URLField(blank=True, null=True, verbose_name='附件')),
                ('objectBuildScorerA', models.CharField(blank=True, max_length=100, null=True, verbose_name='勘查員A')),
                ('objectBuildScorerB', models.CharField(blank=True, max_length=100, null=True, verbose_name='勘查員B')),
                ('objectBuildScorerC', models.CharField(blank=True, max_length=100, null=True, verbose_name='勘查員C')),
                ('objectBuildScorRateA', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True, verbose_name='加成A')),
                ('objectBuildScorRateB', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True, verbose_name='加成B')),
                ('objectBuildScorRateC', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True, verbose_name='加成C')),
                ('objectBuildScorReasonA', models.CharField(blank=True, max_length=100, null=True, verbose_name='加成原因A')),
                ('objectBuildScorReasonB', models.CharField(blank=True, max_length=100, null=True, verbose_name='加成原因B')),
                ('objectBuildScorReasonC', models.CharField(blank=True, max_length=100, null=True, verbose_name='加成原因C')),
                ('plusItemA1', models.CharField(blank=True, max_length=100, null=True)),
                ('plusItemA2', models.CharField(blank=True, max_length=100, null=True)),
                ('plusItemA3', models.CharField(blank=True, max_length=100, null=True)),
                ('plusItemA4', models.CharField(blank=True, max_length=100, null=True)),
                ('plusItemA5', models.CharField(blank=True, max_length=100, null=True)),
                ('plusItemOtherA', models.CharField(blank=True, max_length=100, null=True)),
                ('plusValueA1', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('plusValueA2', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('plusValueA3', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('plusValueA4', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('plusValueA5', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('plusValueOtherA', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('plusItemB1', models.CharField(blank=True, max_length=100, null=True)),
                ('plusItemB2', models.CharField(blank=True, max_length=100, null=True)),
                ('plusItemB3', models.CharField(blank=True, max_length=100, null=True)),
                ('plusItemB4', models.CharField(blank=True, max_length=100, null=True)),
                ('plusItemB5', models.CharField(blank=True, max_length=100, null=True)),
                ('plusItemOtherB', models.CharField(blank=True, max_length=100, null=True)),
                ('plusValueB1', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('plusValueB2', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('plusValueB3', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('plusValueB4', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('plusValueB5', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('plusValueOtherB', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('plusItemC1', models.CharField(blank=True, max_length=100, null=True)),
                ('plusItemC2', models.CharField(blank=True, max_length=100, null=True)),
                ('plusItemC3', models.CharField(blank=True, max_length=100, null=True)),
                ('plusItemC4', models.CharField(blank=True, max_length=100, null=True)),
                ('plusItemC5', models.CharField(blank=True, max_length=100, null=True)),
                ('plusItemOtherC', models.CharField(blank=True, max_length=100, null=True)),
                ('plusValueC1', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('plusValueC2', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('plusValueC3', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('plusValueC4', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('plusValueC5', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('plusValueOtherC', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('yfcase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='objectbuilds', to='yfcases.yfcase')),
            ],
        ),
    ]