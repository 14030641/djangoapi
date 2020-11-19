from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Category(models.Model):
    nameCategory = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.nameCategory

class Product(models.Model):
    nameProduct = models.CharField(max_length=30, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField()
    discontinued = models.BooleanField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.nameProduct

class Customer(models.Model):
    nameCustomer = models.CharField(max_length=50)
    addCustomer = models.CharField(max_length=50)
    emailCustomer = models.EmailField(unique=True)
    phoneCustomer = models.CharField(max_length=13)

    def __str__(self):
        return self.nameCustomer

class Order(models.Model):
    dateOrder = models.DateTimeField(db_index=True)
    shippedDate = models.DateTimeField(db_index=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.dateOrder

class OrderDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.id