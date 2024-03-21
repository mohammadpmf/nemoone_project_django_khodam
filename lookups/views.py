from django.shortcuts import render
from .models import Animation


def show(request):
    animations = Animation.objects.filter(price__range=[0, 25000000], director__contains='sam',)
    context = {
        'animations': animations
    }
    return render(request, 'animations.html', context)