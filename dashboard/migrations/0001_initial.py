# Generated by Django 4.2.1 on 2023-06-03 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=25, verbose_name='Telefon raqam')),
                ('email', models.CharField(blank=True, max_length=256, null=True, verbose_name='Email ssilka')),
                ('address_uz', models.CharField(blank=True, max_length=256, null=True, verbose_name="Manzil so'z bilan")),
                ('address_ru', models.CharField(blank=True, max_length=256, null=True, verbose_name='Адрес прописью')),
                ('address_en', models.CharField(blank=True, max_length=256, null=True, verbose_name='Address in words')),
                ('instagram', models.CharField(blank=True, max_length=256, null=True, verbose_name='Instagram ssilka')),
                ('telegram', models.CharField(blank=True, max_length=256, null=True, verbose_name='Telegram ssilka')),
                ('facebook', models.CharField(blank=True, max_length=256, null=True, verbose_name='Facebook ssilka')),
                ('twitter', models.CharField(blank=True, max_length=256, null=True, verbose_name='Twitter ssilka')),
                ('ok', models.CharField(blank=True, max_length=256, null=True, verbose_name='Ok.ru ssilka')),
                ('youtube', models.CharField(blank=True, max_length=256, null=True, verbose_name='YOUTUBE ssilka')),
                ('location', models.CharField(blank=True, max_length=256, null=True, verbose_name='Joylashuv ssilka')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Ismi')),
                ('first_name', models.CharField(max_length=128, verbose_name='Familiyasi')),
                ('middle_name', models.CharField(max_length=128, verbose_name='Otasini ismi')),
                ('specialty', models.CharField(max_length=256, verbose_name='Mutaxassisligi')),
                ('about_doctor', models.TextField(blank=True, null=True, verbose_name='Shifokor haqida')),
                ('motto', models.TextField(verbose_name='Shifokor shiori')),
                ('phone', models.CharField(blank=True, max_length=25, null=True, verbose_name='Shaxsiy Telefon raqam')),
                ('email', models.CharField(blank=True, max_length=256, null=True, verbose_name='Shaxsiy Email sissilka')),
                ('instagramm', models.CharField(blank=True, max_length=256, null=True, verbose_name='Shaxsiy Instagram sissilka')),
                ('telegram', models.CharField(blank=True, max_length=256, null=True, verbose_name='Shaxsiy Telegram sissilka')),
                ('facebook', models.CharField(blank=True, max_length=256, null=True, verbose_name='Shaxsiy Facebook sissilka')),
                ('twitter', models.CharField(blank=True, max_length=256, null=True, verbose_name='Shaxsiy Twitter sissilka')),
                ('odnoklassniki', models.CharField(blank=True, max_length=256, null=True, verbose_name='Shaxsiy Ok.ru sissilka')),
                ('img', models.ImageField(upload_to='', verbose_name="Shifokor sur'ati")),
            ],
        ),
        migrations.CreateModel(
            name='Otp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=512)),
                ('email', models.CharField(max_length=20)),
                ('is_expired', models.BooleanField(default=False)),
                ('tries', models.SmallIntegerField(default=0)),
                ('extra', models.JSONField(default={})),
                ('is_verified', models.BooleanField(default=False)),
                ('step', models.CharField(max_length=25)),
                ('by', models.IntegerField(choices=[(1, 'By Login')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.CharField(max_length=100, unique=True, verbose_name='User email')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='User phone')),
                ('nickname', models.CharField(max_length=200, verbose_name='nickname')),
                ('firstname', models.CharField(blank=True, max_length=200, null=True)),
                ('lastname', models.CharField(blank=True, max_length=200, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'ordering': ['-date_joined'],
                'get_latest_by': 'date_joined',
            },
        ),
    ]