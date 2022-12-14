# Generated by Django 4.1.2 on 2022-12-01 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBonos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dolar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=30)),
                ('denominacion', models.CharField(max_length=30)),
                ('emisor', models.CharField(max_length=30)),
                ('fecha_emision', models.DateField(null=True)),
                ('fecha_vencimiento', models.DateField(null=True)),
                ('amortizacion', models.CharField(max_length=30)),
                ('interes', models.CharField(max_length=30)),
                ('ley', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Cantante',
        ),
    ]
