# Generated by Django 3.0.4 on 2020-03-31 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=100, verbose_name='название услуги')),
                ('service_description', models.TextField(verbose_name='описание услуги')),
                ('service_price', models.FloatField(verbose_name='цена услуги')),
            ],
        ),
        migrations.CreateModel(
            name='SubServices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_service_name', models.CharField(max_length=100, verbose_name='название под-услуги')),
                ('sub_service_description', models.TextField(verbose_name='описание под-услуги')),
                ('sub_service_price', models.FloatField(verbose_name='цена под-услуги')),
                ('sevice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Service')),
            ],
        ),
    ]
