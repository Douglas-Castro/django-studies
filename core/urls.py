from django.urls import path
from .views import IndexView, ContactView, ProductCreate


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contato/', ContactView.as_view(), name='contato'),
    path('produto/', ProductCreate.as_view(), name='produto'),
]