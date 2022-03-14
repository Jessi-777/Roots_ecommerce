# from distutils.command.upload import upload
# from unicodedata import category
from django.db import models
from django.urls import reverse

class Category(models.Model):
    category_name = models.CharField(max_length=70, unique=True)
    # slug = models.CharField(max_length=100, unique=True)
    # this makes your slug same as category
    slug = models.SlugField(max_length=75, unique=True)
    description = models.TextField(max_length=270, blank=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    # fixed categories spelling


    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.category_name    
