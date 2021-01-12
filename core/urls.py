from django.urls import path
from .views import index, contact, product


urlpatterns = [
    path('', index, name='index'),
    path('contato/', contact, name='contato'),
    path('produto/', product, name='produto'),
]