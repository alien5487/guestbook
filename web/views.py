from django.shortcuts import render
from django.views.generic import *
from .models import Message
from django.urls import reverse_lazy

# Create your views here.
class MessageList(ListView):
    model = Message

class MessageDetail(DetailView):
    model = Message 

class MessageCreate(CreateView):
    model = Message
    fields = ['user', 'subjcet', 'content']      # fields = '__all__'
    succuss_url = reverse_lazy('msg_list')       # success_urls = '/message/list/'