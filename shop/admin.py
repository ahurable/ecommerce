from django.contrib import admin
from .models import Category, Product
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'category', 'description', 'available', 'created', 'updated', 'price', )
    list_filter = ('name', 'category', 'available', 'created', 'updated', 'price',)
    fieldsets = (
            ('Product Details',
                     {'fields':(
                            'name',
                            'category',
                            'available',
                            'price',
                        )
                     }),
                ('Product Additional Details',
                    {'fields':(
                        'slug',
                        'description',
                        'image',
                    )})
                 )
    prepopulated_fields = {'slug':('name', )}

@admin.register(Category)
class CategoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', )
    prepopulated_fields = {
        "slug": ("name", )
    }
