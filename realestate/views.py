from django.shortcuts import render
from django.views import generic

from .models import Estate

class Home(generic.ListView):
    model = Estate
    template_name = "realestate/index.html"
    context_object_name = 'estates'

    def get_queryset(self):
        return Estate.objects.all()
    
class Detail(generic.DetailView):
    model = Estate
    template_name = "realestate/detail.html"
    context_object_name = 'estate'

