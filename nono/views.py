#from django.shortcuts import render
from .models import nono
# Create your views here.

def index(request):
    return render(request, 'index.html')

def new(request):
    return render(request, 'new.html')

    from django.shortcuts import render

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    nono = nono()
    nono.title = title
    nono.content = content
    nono.save()

    return render(request, 'create.html') 