from django.db import models

class Workstation(models.Model):
    location = models.CharField('Расположение рабочего места', max_length=30)
    building = models.CharField('Одно из пяти зданий (АБК, Склад, ЗМК, Бухгалтерия, Отдел продаж)', max_length=20)
    ip = models.CharField('IP-адрес устройства, либо NetBios-имя', max_length=15)
    username = models.CharField('Имя пользователя рабочего места', max_length=20)
    domain = models.BooleanField('Находится ли компьютер в домене')

    def __str__(self):
        return f'{self.username}, {self.building}, {self.location}'

    class Meta:
        verbose_name = 'Рабочая станция'
        verbose_name_plural = 'Рабочие станции'

class Printer(models.Model):
    location = models.CharField('Расположение', max_length=30)
    model = models.CharField('Модель', max_length=20)
    ip = models.CharField('IP-адрес устройства', max_length=15)

    def __str__(self):
        return f'{self.location}, {self.model}'

    class Meta:
        verbose_name = 'Принтер'
        verbose_name_plural = 'Принтеры'
