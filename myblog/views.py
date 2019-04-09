from django.shortcuts import render
from django.http import HttpResponse
from myblog.models import Item
from django.shortcuts import render
from django.views.generic import TemplateView

class Index(TemplateView):
    template_name = 'myblog/index.html'
    def get_context_data(self, **kwargs):
        contest = {
            'items' : Item.objects.all(),
        }
        return contest
