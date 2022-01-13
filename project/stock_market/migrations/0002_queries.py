# Generated by Django 3.2.11 on 2022-01-12 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_market', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Queries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('security_code', models.IntegerField()),
                ('security_name', models.CharField(max_length=100)),
                ('close', models.FloatField()),
                ('market_cap', models.FloatField()),
                ('query', models.CharField(max_length=500)),
                ('stock_id', models.IntegerField()),
            ],
        ),
    ]