from django.db import models

# Create your models here.

class UserAccount(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False, unique=True)
    eventpoint = models.IntegerField(default=0, null=False)
    star = models.IntegerField(default=0, null=False)
    coin = models.IntegerField(default=0, null=False)
    avatar_url = models.CharField(max_length=255, null=True, default=None, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    class Meta:
        db_table = 'user_account'


