from django.shortcuts import render
from firstapp.models import Item
# Create your views here.


def index(request):
    data = Item.objects.all()
    context = {
        'data' : data,
    }
    return render(request, 'firstapp/index.html', context=context)

def contact(request):
    context = {
        'data' : ['a', 'b', 'c', 'd']
    }
    return render(request, 'firstapp/contact.html', context=context)