from django.db import models
from user.models import User
from datetime import datetime
from master.models import Occupation

class Need(models.Model):

        id = models.AutoField('ID', primary_key=True)
        user_id = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user', null=False)
        username = models.CharField('ニックネーム', max_length=255, null=False)
        occupation_id = models.ForeignKey(Occupation, on_delete=models.PROTECT, null=False)
        content = models.TextField('投稿内容', max_length=1000, null=False)
        is_passed = models.BooleanField('審査済みフラグ', null=False, default=False)
        created_at = models.DateTimeField('投稿日時', default=datetime.now())

        def __str__(self):
            status = ""
            if not self.is_passed:
                status = "審査待ち"
            return f"{self.id} / {self.content} / {status}"

# class Comment(models.Model):
#
#         id = models.AutoField('ID', primary_key=True)
#         user_id = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user', null=False)
#         need_id = models.ForeignKey(Need, on_delete=models.PROTECT, null=False)
#         content = models.TextField('投稿内容', max_length=1000, null=False)
#
#         def __str__(self):
#             return f"{self.id} / {self.content}"

# Create your models here.
