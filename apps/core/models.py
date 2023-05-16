from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

class Product(models.Model):
    id_product = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Warehouse(models.Model):
    id_warehouse = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

class Customer(models.Model):
    id_customer = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

class Supplier(models.Model):
    id_supplier = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    fax = models.CharField(max_length=255)
    email = models.CharField(max_length=255)