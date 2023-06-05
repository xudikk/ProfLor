from django.db import models


class Doctor(models.Model):
    FIO = models.CharField('FIO', max_length=128)
    specialty = models.CharField('Mutaxassisligi', max_length=256)
    about_doctor = models.TextField('Shifokor haqida', null=True, blank=True)
    motto = models.CharField('Shifokor shiori',max_length=512, null=True, blank=True)
    phone = models.CharField('Shaxsiy Telefon raqam', max_length=25, null=True, blank=True)
    email = models.CharField('Shaxsiy Email sissilka', max_length=256, null=True, blank=True)
    instagram = models.CharField('Shaxsiy Instagram sissilka', max_length=256, null=True, blank=True)
    telegram = models.CharField('Shaxsiy Telegram sissilka', max_length=256, null=True, blank=True)
    facebook = models.CharField('Shaxsiy Facebook sissilka', max_length=256, null=True, blank=True)
    twitter = models.CharField('Shaxsiy Twitter sissilka', max_length=256, null=True, blank=True)
    ok = models.CharField('Shaxsiy Ok.ru sissilka', max_length=256, null=True, blank=True)
    img = models.ImageField('Shifokor sur\'ati', upload_to='sayt/doc')

    def __str__(self):
        return self.FIO
