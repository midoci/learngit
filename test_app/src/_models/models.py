# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    open_id = models.IntegerField(blank=True, null=True)
    nickname = models.CharField(max_length=32, blank=True)
    ad_type = models.IntegerField(blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    province = models.CharField(max_length=16, blank=True)
    city = models.CharField(max_length=16, blank=True)
    headimgurl = models.CharField(max_length=128, blank=True)

    class Meta:
        managed = False
        db_table = 'user_info'
