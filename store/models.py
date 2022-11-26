
from django.db import models
from category.models import Category
from django.urls import reverse
from accounts.models import Account
# from django.db.models import Avg, Count

class Product(models.Model):
    product_name    = models.CharField(max_length=100, unique=True)
    slug            = models.SlugField(max_length=100, unique=True)
    description     = models.TextField(max_length=700, blank=True)
    price           = models.IntegerField()
    images          = models.ImageField(upload_to='photos/products')
    stock           = models.IntegerField()
    is_available    = models.BooleanField(default=True)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name


class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager, self).filter(variation_category='color', is_active=True)

    def sizes(self):
        return super(VariationManager, self).filter(variation_category='size', is_active=True)


variation_category_choice = (
    ('color', 'color'),
    ('size', 'size'),
)


class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=107, choices=variation_category_choice)
    variation_value = models.CharField(max_length=107)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now=True)

    objects = VariationManager()

    def __str__(self):
        return self.product

    def __str__(self):
        return self.variation_value


    def __unicode__(self):
        return self.variation_value