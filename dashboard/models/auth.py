
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_staff=False,
                    is_active=True, **extra_fields):
        'Creates a User with the given username, email and password'

        user = self.model(email=email, is_active=is_active,
                          is_staff=is_staff, **extra_fields)

        if password:
            user.set_password(password)

        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        return self.create_user(email, password, is_staff=True,
                                is_superuser=True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.CharField('User email', max_length=100, unique=True)
    phone = models.CharField('User phone', max_length=20, blank=True, null=True)
    nickname = models.CharField('nickname', max_length=200, blank=False, null=False, )
    firstname = models.CharField(max_length=200, blank=True, null=True, )
    lastname = models.CharField(max_length=200, blank=True, null=True, )

    is_staff = models.BooleanField(default=False, )
    is_active = models.BooleanField(default=True, null=False)
    date_joined = models.DateTimeField(auto_now_add=True, editable=False)

    USERNAME_FIELD = "email"
    objects = UserManager()

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return f"{self.firstname} {self.lastname} {self.phone}"

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        ordering = ["-date_joined"]
        get_latest_by = "date_joined"


class Otp(models.Model):
    key = models.CharField(max_length=512)
    email = models.CharField(max_length=20)
    is_expired = models.BooleanField(default=False)
    tries = models.SmallIntegerField(default=0)
    extra = models.JSONField(default={})
    is_verified = models.BooleanField(default=False)
    step = models.CharField(max_length=25)
    by = models.IntegerField(choices=[
        (1, "By Login"),
    ])

    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def save(self, *args, **kwargs):
        if self.tries >= 3:
            self.is_expired = True
        return super(Otp, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.key}-{self.email}"

