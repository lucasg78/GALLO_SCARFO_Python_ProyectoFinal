# Generated by Django 4.1.2 on 2022-12-02 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBonos', '0003_delete_album_delete_articulo_delete_concierto'),
    ]

    operations = [
        migrations.CreateModel(
            name='PesosCer',
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
        migrations.AlterField(
            model_name='dolar',
            name='amortizacion',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='dolar',
            name='denominacion',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='dolar',
            name='interes',
            field=models.CharField(max_length=500),
        ),
    ]
