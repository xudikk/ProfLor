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


class Patients(models.Model):
    FIO = models.CharField('FIO', max_length=128)
    birth = models.IntegerField("Tug'ulgan yili")

    def __str__(self):
        return self.FIO


class Diagnoz(models.Model):
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
    name = models.CharField(max_length=512)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.FIO} | {self.name}"


# class Tablets(models.Model):
#     name = models.CharField("Nomi", max_length=128)
#     type = models.CharField("Turi", max_length=50, default="Tabletka", choices=[
#         ('Tomchi', 'Tomchi'),
#         ('Tabletka', 'Tabletka'),
#         ('Sirop', 'Sirop'),
#     ])


class Suggests(models.Model):
    diagnoz = models.ForeignKey(Diagnoz, on_delete=models.CASCADE)
    tablet = models.CharField("Dorining Nomi", max_length=256)
    suggest = models.CharField("Maslahat", max_length=512, null=True, blank=True)
