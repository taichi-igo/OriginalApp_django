from django.db import models

class Occupation(models.Model):

    id = models.AutoField('ID', primary_key=True)
    name = models.CharField('業種名', max_length=255, null=False)


    def __str__(self):
        return f'{self.id}/{self.name}'

# Create your models here.
