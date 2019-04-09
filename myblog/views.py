from django.shortcuts import render
from django.http import HttpResponse
from myblog.models import Item
from django.shortcuts import render
def index(request):
    context = {
        'items' : Item.objects.all(),
    }
    return render(request, 'myblog/index.html', context)
