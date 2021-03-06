# Generated by Django 3.1.7 on 2021-04-07 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yfcases', '0009_objectbuild'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinalDecision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finalDecision', models.CharField(blank=True, max_length=10, null=True, verbose_name='最終判定')),
                ('regionalHead', models.CharField(blank=True, max_length=10, null=True, verbose_name='區域負責人')),
                ('subSigntrueA', models.CharField(blank=True, max_length=10, null=True, verbose_name='副署人員1')),
                ('subSigntrueB', models.CharField(blank=True, max_length=10, null=True, verbose_name='副署人員2')),
                ('regionalHeadDate', models.CharField(blank=True, max_length=10, null=True, verbose_name='簽核日期')),
                ('subSigntrueDateA', models.CharField(blank=True, max_length=10, null=True, verbose_name='簽核日期')),
                ('subSigntrueDateB', models.CharField(blank=True, max_length=10, null=True, verbose_name='簽核日期')),
                ('yfcase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='finaldecisions', to='yfcases.yfcase')),
            ],
        ),
    ]
