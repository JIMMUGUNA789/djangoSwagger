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
    if category.is_valid():
        # validating for already existing category   
        category_name = category.validated_data['name']
        if Category.objects.filter(name=category_name).exists():
            raise serializers.ValidationError("Category already exists")
        else:
            category.save() 
            return Response(category.data, status=status.HTTP_201_CREATED)
    else:
        return Response(category.errors, status=status.HTTP_400_BAD_REQUEST)  
    
@api_view(['GET'])
def get_all_categories(request):
    # check for the parameters from the url
    if request.query_params:
        categories = Category.objects.filter(**request.query_params.dict())
    else:
        categories = Category.objects.all()
    # check if categories contains any data
    if categories:
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['POST'])
def add_subcategory(request):
    subcategory = SubCategorySerializer(data = request.data)
    
    if subcategory.is_valid():
        # validating for already existing subcategory
        subcategory_name = subcategory.validated_data['name']
        if SubCategory.objects.filter(name = subcategory_name).exists():
            raise serializers.ValidationError("SubCategory already exists")
        else:
            subcategory.save()
            return Response(subcategory.data, status = status.HTTP_201_CREATED)
    else:
        return Response(subcategory.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def get_all_subcategories(request):
    # check for parameters from the url
    if request.query_params:
        subcategories = SubCategory.objects.filter(**request.query_params.dict())
    else:
        subcategories = SubCategory.objects.all()
    # check if subcategories contains any data
    if subcategories:
        serializer = SubCategorySerializer(subcategories, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['POST'])
def add_product(request):
    product = ProductSerializer(data = request.data)    
    if product.is_valid():
        # validating for already existing product
        product_name = product.validated_data['name']
        if Product.objects.filter(name = product_name).exists():
            raise serializers.ValidationError("Product already exists")
        else:
            product.save()
            return Response(product.data, status = status.HTTP_201_CREATED)
    else:
        return Response(product.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def get_all_products(request):
    # check for parameters from the url
    if request.query_params:
        products = Product.objects.filter(**request.query_params.dict())
    else:
        products = Product.objects.all()
    # check if products contains any data
    if products:
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


