from django.contrib import admin
from . import views
from django.urls import path,include
from django.views.generic.base import TemplateView

app_name='menu'


urlpatterns = [
	path('item_list/',views.item_list,name='item_list'),
	path('<str:category_slug>/',views.item_list,name="items_list_by_category"),
 	path('<int:id>/<slug:slug>/',views.item_detail,name='item_detail'),
]
