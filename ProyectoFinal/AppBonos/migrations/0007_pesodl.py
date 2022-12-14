# Generated by Django 4.1.2 on 2022-12-02 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBonos', '0006_pesobd'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pesodl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=30)),
                ('denominacion', models.CharField(max_length=100)),
                ('emisor', models.CharField(max_length=30)),
                ('fecha_emision', models.DateField(null=True)),
                ('fecha_vencimiento', models.DateField(null=True)),
                ('amortizacion', models.CharField(max_length=500)),
                ('interes', models.CharField(max_length=500)),
                ('ley', models.CharField(max_length=30)),
            ],
        ),
    ]
