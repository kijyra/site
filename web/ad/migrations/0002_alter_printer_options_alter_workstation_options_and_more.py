# Generated by Django 4.2.4 on 2023-08-06 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='printer',
            options={'verbose_name': 'Принтер', 'verbose_name_plural': 'Принтеры'},
        ),
        migrations.AlterModelOptions(
            name='workstation',
            options={'verbose_name': 'Рабочая станция', 'verbose_name_plural': 'Рабочие станции'},
        ),
        migrations.RemoveField(
            model_name='workstation',
            name='rdpc_url',
        ),
        migrations.RemoveField(
            model_name='workstation',
            name='rdps_url',
        ),
        migrations.RemoveField(
            model_name='workstation',
            name='vnc_url',
        ),
        migrations.AddField(
            model_name='workstation',
            name='domain',
            field=models.BooleanField(default=1, verbose_name='Находится ли компьютер в домене'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='printer',
            name='ip',
            field=models.CharField(max_length=15, verbose_name='IP-адрес устройства'),
        ),
        migrations.AlterField(
            model_name='printer',
            name='location',
            field=models.CharField(max_length=30, verbose_name='Расположение'),
        ),
        migrations.AlterField(
            model_name='printer',
            name='model',
            field=models.CharField(max_length=20, verbose_name='Модель'),
        ),
        migrations.AlterField(
            model_name='workstation',
            name='building',
            field=models.CharField(max_length=20, verbose_name='Одно из пяти зданий (АБК, Склад, ЗМК, Бухгалтерия, Отдел продаж)'),
        ),
        migrations.AlterField(
            model_name='workstation',
            name='ip',
            field=models.CharField(max_length=15, verbose_name='IP-адрес устройства, либо NetBios-имя'),
        ),
        migrations.AlterField(
            model_name='workstation',
            name='location',
            field=models.CharField(max_length=30, verbose_name='Расположение рабочего места'),
        ),
        migrations.AlterField(
            model_name='workstation',
            name='username',
            field=models.CharField(max_length=20, verbose_name='Имя пользователя рабочего места'),
        ),
    ]