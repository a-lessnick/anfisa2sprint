# ice_cream/admin.py
from django.contrib import admin

# Из модуля models импортируем модель Category...
from .models import Category, IceCream, Topping

# ...и регистрируем её в админке:
admin.site.register(Category)
admin.site.register(IceCream)
admin.site.register(Topping)

