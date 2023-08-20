from django.views.generic.detail import DetailView

from .models import Dish


class DishView(DetailView):
    model = Dish
    template_name = 'menu/dish/dish_detail.html'
