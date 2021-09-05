from django.db import models

# Create your models here.
def productsInBucketDefault():
    # return []
    return []

class MyUser(models.Model):
    id = models.AutoField(primary_key=True)
    moneys = models.IntegerField(default=0)
    productsInBucket = models.JSONField("productsInBucket", default=productsInBucketDefault)
    # productsInBucket = models.JSONField("productsInBucket", default=productsInBucketDefault)
    email = models.TextField()
    password = models.TextField()
    name = models.TextField()
    age = models.IntegerField()

class MyOrder(models.Model):
    id = models.AutoField(primary_key=True)
    ownername = models.TextField()
    price = models.IntegerField()

class MyProduct(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    price = models.IntegerField()
    
class MyProductInner(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    price = models.IntegerField()