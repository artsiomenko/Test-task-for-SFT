from django.db import models


class Contract(models.Model):
    customer = models.CharField(max_length=100)
    price    = models.IntegerField() 
    created  = models.DateTimeField(auto_now_add=True)


class Producer(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    title = models.CharField(max_length=100)
    producer = models.ForeignKey(Producer, on_delete=models.RESTRICT, related_name='producer')
    created  = models.DateTimeField(auto_now_add=True)


class Statement(models.Model):
    contract  = models.OneToOneField(Contract, on_delete=models.RESTRICT, related_name='contract')
    products  = models.ManyToManyField(Product, through="StatementProduct")
    created   = models.DateTimeField(auto_now_add=True)


class StatementProduct(models.Model):
    statement_id = models.ForeignKey(Statement, on_delete=models.RESTRICT, related_name='statement')
    product_id   = models.OneToOneField(Product, on_delete=models.RESTRICT, related_name='product')
