from django.db import models


class New(models.Model):
    img = models.ImageField("Yangilikning Rasmi", upload_to='sayt/news')
    title_uz = models.CharField('Sarlavha', max_length=512)
    title_ru = models.CharField('Заголовок', max_length=512, null=True)
    title_en = models.CharField('Title', max_length=512, null=True)
    shortdesc_uz = models.TextField("Yangilikning Qisqa matni", null=True)
    shortdesc_ru = models.TextField("Краткий текст сознания", null=True)
    shortdesc_en = models.TextField("Short description", null=True)
    desc_uz = models.TextField("Yangilikning To'liq matni", null=True)
    desc_ru = models.TextField("Полный текст новости", null=True)
    desc_en = models.TextField("Full text of the news", null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title_uz
