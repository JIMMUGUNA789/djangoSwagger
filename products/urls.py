from django.urls import path

from . import views
urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('category-create/', views.add_category, name='category-create'),

]