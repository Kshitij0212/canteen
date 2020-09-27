from django.shortcuts import render
from django.views.generic import (TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView)
from .models import Message
from django.urls import reverse_lazy
# Create your views here.

class OrderCreateView(CreateView):
    model = Message
    fields = ['name', 'contact_no', 'room_no', 'order']

class OrderDetailView(DetailView):
    context_object_name = 'order_detail'
    model = Message
    template_name = 'order/order_detail.html'

class OrderListView(ListView):
    model = Message

class OrderUpdateView(UpdateView):
    fields = ['name', 'contact_no', 'room_no', 'order']
    model = Message

class OrderDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('home')
