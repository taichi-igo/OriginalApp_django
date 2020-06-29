from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    _user_has_perm
)
from django.core import validators
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from master.models import Occupation
from datetime import datetime

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **user_data):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            **user_data
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    id = models.AutoField('ID', primary_key=True)
    occupation_id = models.ForeignKey(Occupation, null=False, on_delete=models.PROTECT)
    username = models.CharField('ニックネーム', max_length=255, null=False)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True, null=False)
    birthday = models.DateField('生年月日', null=True, blank=True)
    address = models.CharField('現住所', max_length=140, null=True, blank=True)
    password = models.CharField('パスワード', max_length=140, null=False)
    is_tmp_user = models.BooleanField(default=False, null=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return f"{self.id} / {self.username}"

    @property
    def age(self):
        if self.birthday==None:
            return -1

        year = self.birthday.year
        month = self.birthday.month
        day = self.birthday.day
        now = datetime.now()

        #今日の日付
        today_year  = now.year
        today_month = now.month
        today_day   = now.day

        #月が過ぎた場合
        if today_month > month :
            is_passed = True
        #月が同じ場合
        elif today_month == month :
            is_passed = today_day >= day
        else :
            is_passed = False

        if is_passed :
            age = today_year - year
        else :
            age = today_year - year - 1

        return age





# Create your models here.
