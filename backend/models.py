from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    address = models.CharField(max_length=128)

class Button(models.Model):
    button_id = models.CharField(primary_key=True, max_length=64)
    
    def __str__(self):
        return str(self.button_id)
    class Meta:
        db_table = 'button'

class Regist(models.Model):
    button_id = models.ForeignKey(Button, related_name = 'button_regist', on_delete=models.CASCADE)
    cust_id = models.ForeignKey(User, on_delete=models.CASCADE)
    #bundle = models.ManyToManyField(Product, through='Bundle')

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'regist'
        unique_together = ('button_id', 'cust_id')

    
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=128)
    product_price = models.IntegerField()
    product_stock = models.IntegerField()

    def __str__(self):
        return str(self.product_name)

    class Meta:
        db_table = 'product'

class Bundle(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    regist_id = models.ForeignKey(Regist, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.product_id)
    
    class Meta:
        db_table = 'bundle'

class Record(models.Model):
    regist_id = models.ForeignKey(Regist, on_delete=models.CASCADE)
    button_id = models.CharField(max_length=64)
    sequence_num = models.IntegerField()
    record_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.regist_id)
    
    class Meta:
        db_table = 'record'
