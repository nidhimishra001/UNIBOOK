# from MySQLdb import Date
from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=20, null=True,default=None)
    publisher=models.CharField(max_length=50,null=True,default=None)
    course=models.CharField(max_length=20,null=True,default=None)
    author=models.CharField(max_length=50,null=True,default=None)
    Date_of_publication=models.DateTimeField(null=True,default=None)
    Edition=models.CharField(max_length=50,null=True,default=None)
    def __str__(self):
        return self.title

class Tag(models.Model):
    tag=models.CharField(max_length=20)
    def __str__(self):
        return self.tag


class Contact(models.Model):
    name=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=50,null=True)
    phone=models.CharField(max_length=12,null=True)
    description=models.CharField(max_length=100 ,null=True,default=None)
    def __str__(self):
        return self.name

        

