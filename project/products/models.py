from django.db import models
from django.db.models import base

# Create your models here.

CATEGORY_CHOICES = (
    ('Sports Wear','Sports Wear'),
    ('Shoes','Shoes'),
    ('Trousers','Trousers'),
    ('Electronics','Electronics'),
)

class Product(models.Model):
    product_name = models.CharField(max_length=200, blank=True,null=True)
    price = models.DecimalField(max_digits=9,decimal_places=2,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    discount_price = models.DecimalField(max_digits=9, decimal_places=2,blank=True,null=True)
    isOutOfStock = models.BooleanField(default=False)
    product_category = models.ForeignKey('Category', on_delete=models.SET_NULL,blank=True,null=True)
    product_image = models.ImageField(upload_to="images",blank=True,null=True)
    
    def __str__(self):
        return self.product_name


    class Meta:
        verbose_name_plural = 'Product'

    

class Category(models.Model):
    category_name = models.CharField(max_length=30,choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.category_name
    class Meta:
        verbose_name_plural = 'Category'