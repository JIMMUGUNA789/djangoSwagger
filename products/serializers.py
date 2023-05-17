from rest_framework import serializers
from .models import Product, Category, SubCategory
from django.db.models import fields


""" A type of `ModelSerializer` that uses hyperlinked relationships instead
    of primary key relationships. Specifically:
    * A 'url' field is included instead of the 'id' field.
    * Relationships to other instances are hyperlinks, instead of primary keys.
    """
# class CategorySerializer(serializers.ModelSerializer):
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.HyperlinkedRelatedField(many=True, view_name='product-detail', read_only=True)
    subcategories = serializers.HyperlinkedRelatedField(many=True, view_name='subcategory-detail', read_only=True)
    class Meta:
        model = Category
        # fields = ('id', 'name', 'description')
        fields = '__all__'
# class SubCategorySerializer(serializers.ModelSerializer):
class SubCategorySerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.HyperlinkedRelatedField(many=True, view_name='product-detail', read_only=True)    
    class Meta:
        model = SubCategory
        # fields = ('id', 'name', 'description', 'category')
        fields = '__all__'
# class ProductSerializer(serializers.ModelSerializer):
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.SlugRelatedField(queryset=Category.objects.all(),slug_field='name')
    SubCategory = serializers.SlugRelatedField(queryset = SubCategory.objects.all(), slug_field = 'name')


    class Meta:
        model = Product
        # fields = ('id', 'name', 'price', 'description', 'category', 'SubCategory')
        fields = '__all__'

