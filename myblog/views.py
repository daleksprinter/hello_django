from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
def index(request):
    context = {
        'hoge' : 'fuga',
    }
    return render(request, 'myblog/index.html', context)
