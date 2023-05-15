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
    path('category-update/<int:pk>/', views.update_category, name='category-update'),
    path('subcategory-update/<int:pk>/', views.update_subcategory, name='subcategory-update'),
    path('product-update/<int:pk>/', views.update_product, name='product-update'),
    path('category-delete/<int:pk>/', views.delete_category, name='category-delete'),
    path('subcategory-delete/<int:pk>/', views.delete_sub_category, name='subcategory-delete'),
    path('product-delete/<int:pk>/', views.delete_product, name='product-delete'),

]