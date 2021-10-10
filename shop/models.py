from django.db import models
from django.utils.text import slugify
from random import randint
from os.path import splitext, basename
from datetime import datetime
import unicodedata
# Create your models here.

def imgPath(instance, filepath):
    filename = basename(filepath)
    name, ext = splitext(filename)
    new_name = randint(0,100)
    today_date = datetime.date(datetime.today())
    final_path = f"prducts/{today_date}/{today_date}-{new_name}{ext}"
    return final_path

class Category(models.Model):

    name = models.CharField(max_length=255, unique=True)
    slug = models.CharField(max_length=300, unique=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Product(models.Model):

    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=300, allow_unicode=True, db_index=True)
    image = models.ImageField(upload_to=imgPath, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=16, decimal_places=1)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug',), )

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.name:
            ex = False
            to_slug = str(slugify(self.name))
            ex = Product.objects.filter(slug=to_slug).exists()
            while ex:
                to_slug = str(slugify(self.name))+str(randint(0, 99999999))
                ex = Product.objects.filter(slug=to_slug).exists()
            self.slug = to_slug
            super(*args, **kwargs).save()
