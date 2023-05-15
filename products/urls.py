from django.urls import path

from . import views
urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('category-create/', views.add_category, name='category-create'),
    path('subcategory-create/', views.add_subcategory, name='subcategory-create'),
    path('product-create/', views.add_product, name='product-create'),
    path('categories/', views.get_all_categories, name='all-categories'),
    path('subcategories/', views.get_all_subcategories, name='all-subcategories'),
    path('products/', views.get_all_products, name='all-products'),

]