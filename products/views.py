from rest_framework.decorators import api_view
from rest_framework.response import Response


from .models import Category, SubCategory, Product
from .serializers import CategorySerializer, SubCategorySerializer, ProductSerializer
from rest_framework import serializers
from rest_framework import status

@api_view(['GET'])
def apiOverview(request):
    category_urls = {
        'all_categories': '/categories/',
        'Add Category': '/category-create/',
        'Update Category': '/category-update/<str:pk>/',
        'Delete Category': '/category-delete/<str:pk>/',

        'all_subcategories': '/subcategories/',
        'Add SubCategory': '/subcategory-create/',
        'Update SubCategory': '/subcategory-update/<str:pk>/',
        'Delete SubCategory': '/subcategory-delete/<str:pk>/',

        'all_products': '/products/',
        'Add Product': '/product-create/',
        'Update Product': '/product-update/<str:pk>/',
        'Delete Product': '/product-delete/<str:pk>/',
        'Search Product': '/product-search/<str:pk>/',
        'Search by Category': '/product-search/?category=category_name/',
        'Search by SubCategory': '/product-search/?subcategory=subcategory_name/',

    }
    return Response(category_urls)

@api_view(['POST'])
def add_category(request):
    category = CategorySerializer(data=request.data)
    # validating for already existing category
    if Category.objects.filter(**request).exists():
        raise serializers.ValidationError("Category already exists")
    if category.is_valid():
        category.save() 
        return Response(category.data, status=status.HTTP_201_CREATED)
    else:
        return Response(category.errors, status=status.HTTP_400_BAD_REQUEST)  
