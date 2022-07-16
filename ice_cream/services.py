from django.db.models import F
from .models import IceCream, Category


def add_views(id_product):
    """Добавление просмотра"""
    IceCream.objects.filter(pk=id_product).update(views=F('views') + 1)


def returns_all_categories():
    """Получение всех категорий"""
    categories = Category.objects.all()
    return categories


def returns_top_six_popularity_icecream():
    """Получение топ шесть самых популярных мороженых"""
    icecream = IceCream.objects.order_by('-views')[:6]
    return icecream


def returns_all_photos_icecream():
    """Получение все фотографии мороженых"""
    photos = IceCream.objects.all().only('photo')
    return photos


def returns_top_six_the_most_expensive_icecream():
    """Получение топ шесть самых дорогих мороженых"""
    icecream = IceCream.objects.order_by('-price')[:6]
    return icecream
