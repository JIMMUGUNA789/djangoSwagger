from django.contrib import admin
from .models import Category, SubCategory, Product
# Register your models here.
# define a class that contains metadata about the model
class CategoryAdmin(admin.ModelAdmin):
    # define a list of fields to display
    list_display = ('name', 'description')
    # define a list of fields to search
    search_fields = ['name']
class SubCategoryAdmin(admin.ModelAdmin):
    # define a list of fields to display
    list_display = ('name', 'description', 'category')
    # define a list of fields to search
    search_fields = ['name', 'category']
class ProductAdmin(admin.ModelAdmin):
    # define a list of fields to display
    list_display = ('name', 'price', 'description', 'category', 'SubCategory')
    # define a list of fields to search
    search_fields = ['name', 'category', 'SubCategory']
# register the model with the admin site
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Product, ProductAdmin)
