from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='home'),
    path('cards/', CardsListViewIceCream.as_view(), name='cards'),
    path('add-icecream/', AddIceCream.as_view(), name='add-icecream'),
    path('category/', CategoriesIceCream.as_view(), name='categories'),
    path('category/<slug:cat_slug>/', CategoryIceCream.as_view(), name='category'),
    path('icecream/<int:icecream_id>/', ShowOneIceCream.as_view(), name='icecream'),
]
