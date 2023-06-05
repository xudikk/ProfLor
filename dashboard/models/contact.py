from django.db import models


class Contact(models.Model):
    phone = models.CharField('Telefon raqam', max_length=25)
    email = models.CharField('Email ssilka', max_length=256, null=True, blank=True)
    address_uz = models.CharField("Manzil so'z bilan", max_length=256, null=True, blank=True)
    address_ru = models.CharField('Адрес прописью', max_length=256, null=True, blank=True)
    address_en = models.CharField('Address in words', max_length=256, null=True, blank=True)
    instagram = models.CharField('Instagram ssilka', max_length=256, null=True, blank=True)
    telegram = models.CharField('Telegram ssilka', max_length=256, null=True, blank=True)
    facebook = models.CharField('Facebook ssilka', max_length=256, null=True, blank=True)
    twitter = models.CharField('Twitter ssilka', max_length=256, null=True, blank=True)
    ok = models.CharField('Ok.ru ssilka', max_length=256, null=True, blank=True)
    youtube = models.CharField('YOUTUBE ssilka', max_length=256, null=True, blank=True)
    location = models.CharField('Joylashuv ssilka', max_length=256, null=True, blank=True)

    def save(self, *args, **kwargs):
        for i in Contact.objects.all():
            if i.id != self.id:
                i.delete()
        return super(Contact, self).save(*args, **kwargs)

    def __str__(self):
        return self.phone

