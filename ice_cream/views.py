from django.shortcuts import render
from django.urls import reverse_lazy
from .services import returns_all_categories, returns_top_six_popularity_icecream, \
    returns_top_six_the_most_expensive_icecream, add_views, returns_all_photos_icecream
from .form import AddIceCreamForm
from .models import IceCream
from django.views.generic import ListView, DetailView, CreateView


def homepage(request):
    icecream_popularity = returns_top_six_popularity_icecream()
    icecream_expensive = returns_top_six_the_most_expensive_icecream()
    products = returns_all_photos_icecream()
    user_name = request.user
    context = {
        'title': 'Мороженые',
        'icecream_popularity': icecream_popularity,
        'icecream_expensive': icecream_expensive,
        'user_name': user_name,
        'products': products
    }
    return render(request, 'ice_cream/index.html', context=context)


class CardsListViewIceCream(ListView):
    model = IceCream
    template_name = 'ice_cream/cards.html'
    context_object_name = "ice_cream"
    paginate_by = 9

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Мороженые'
        return context


class ShowOneIceCream(DetailView):
    model = IceCream
    template_name = 'ice_cream/icecream.html'
    context_object_name = 'ice_cream'
    pk_url_kwarg = 'icecream_id'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Мороженое'
        context['user_name'] = self.request.user
        add_views(context['object'].id)
        return context


class CategoriesIceCream(ListView):
    model = IceCream
    template_name = 'ice_cream/category.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = returns_all_categories()
        context['title'] = 'Категории'
        context['categories'] = categories
        return context


class CategoryIceCream(ListView):
    model = IceCream
    template_name = 'ice_cream/category.html'
    context_object_name = 'products'
    page_kwarg = 'cat_slug'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = returns_all_categories()
        context['title'] = 'Категория'
        context['categories'] = categories
        return context

    def get_queryset(self):
        return IceCream.objects.filter(category__slug=self.kwargs['cat_slug'])


class AddIceCream(CreateView):
    form_class = AddIceCreamForm
    template_name = 'ice_cream/add_icecream.html'
    success_url = reverse_lazy('cards')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление мороженого'
        return context
