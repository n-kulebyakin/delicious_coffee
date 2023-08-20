from .views import DishView
from django.urls import path

app_name = 'menu'

urlpatterns = [
path('<slug:slug>/', DishView.as_view(), name='dish')
]