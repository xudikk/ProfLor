# Generated by Django 4.2.1 on 2023-06-04 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_new_rename_instagramm_doctor_instagram_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='img',
            field=models.ImageField(upload_to='sayt/doc', verbose_name="Shifokor sur'ati"),
        ),
        migrations.AlterField(
            model_name='new',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='new',
            name='img',
            field=models.ImageField(upload_to='sayt/news'),
        ),
    ]
