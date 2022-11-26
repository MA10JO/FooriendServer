from django.db import models


class Account(models.Model):
    email = models.CharField(max_length = 200, unique=True, verbose_name='유저 이메일')
    password = models.CharField(max_length = 500, verbose_name='유저 비밀번호')
    name = models.CharField(max_length = 300, unique=True, verbose_name='유저 이름')
    nickname = models.CharField(max_length = 200, unique=True, verbose_name='유저 닉네임')
    phoneNum = models.CharField(max_length = 200, unique=True, verbose_name='유저 핸드폰 번호')
    created_at = models.DateTimeField(auto_now_add = True, verbose_name='계정 생성시간')
    updated_at = models.DateTimeField(auto_now = True, verbose_name='계정 업데이트 시간')

    class Meta:
        db_table = "account"
        verbose_name = '유저'
        verbose_name_plural = '유저'