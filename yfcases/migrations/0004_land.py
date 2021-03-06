# Generated by Django 3.1.7 on 2021-04-06 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yfcases', '0003_auto_20210401_0951'),
    ]

    operations = [
        migrations.CreateModel(
            name='Land',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('landNumber', models.CharField(blank=True, max_length=100, null=True, verbose_name='地號')),
                ('landUrl', models.URLField(blank=True, null=True, verbose_name='謄本')),
                ('landArea', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='地坪(平方公尺)')),
                ('landHoldingPointPersonal', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=8, null=True, verbose_name='個人持分')),
                ('landHoldingPointAll', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=8, null=True, verbose_name='所有持分')),
                ('landRemarks', models.CharField(blank=True, max_length=100, null=True, verbose_name='備註')),
                ('landPresentValue', models.CharField(blank=True, max_length=100, null=True, verbose_name='土地現值')),
                ('landTotalArea', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='地坪總面積')),
                ('landAreaWidth', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=8, null=True, verbose_name='土地寬度')),
                ('landAreaDepth', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=8, null=True, verbose_name='土地深度')),
                ('yfcase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lands', to='yfcases.yfcase')),
            ],
        ),
    ]
