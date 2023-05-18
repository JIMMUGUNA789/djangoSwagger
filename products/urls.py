from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from . import views

schema_view = get_schema_view(
    openapi.Info(
        title= "Products API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://github.com/JIMMUGUNA789/NewsToday-PrivacyPolicy/blob/main/privacy-policy.md",
        contact=openapi.Contact(email="mugunajim@gmail.com"),
        license=openapi.License(name="BSD License"),
        
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
# urlpatterns = [
#     path('', views.apiOverview, name='api-overview'),
#     path('category-create/', views.add_category, name='category-create'),
#     path('subcategory-create/', views.add_subcategory, name='subcategory-create'),
#     path('product-create/', views.add_product, name='product-create'),
#     path('categories/', views.get_all_categories, name='all-categories'),
#     path('subcategories/', views.get_all_subcategories, name='all-subcategories'),
#     path('products/', views.get_all_products, name='all-products'),
#     path('category-update/<int:pk>/', views.update_category, name='category-update'),
#     path('subcategory-update/<int:pk>/', views.update_subcategory, name='subcategory-update'),
#     path('product-update/<int:pk>/', views.update_product, name='product-update'),
#     path('category-delete/<int:pk>/', views.delete_category, name='category-delete'),
#     path('subcategory-delete/<int:pk>/', views.delete_sub_category, name='subcategory-delete'),
#     path('product-delete/<int:pk>/', views.delete_product, name='product-delete'),

# ]
# Browsable API
urlpatterns = [
    path('swagger-docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', views.ApiRoot.as_view(), name='api-overview'),
    path('categories/', views.CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoryDetail.as_view(), name='category-detail'),
    path('subcategories/', views.SubCategoryList.as_view(), name='subcategory-list'),
    path('subcategories/<int:pk>/', views.SubCategoryDetail.as_view(), name='subcategory-detail'),
    path('products/', views.ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
]

