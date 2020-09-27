from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('create/', views.OrderCreateView.as_view(), name='order_create'),
    path('<pk>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('list', views.OrderListView.as_view(), name='order_list'),
    path('update/<pk>/', views.OrderUpdateView.as_view(), name='order_update'),
    path('delete/<pk>/', views.OrderDeleteView.as_view(), name='order_delete'),
]
