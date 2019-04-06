from django.shortcuts import render

from .forms import AddItemForm


def index(request):
    
    return render(request, 'bucket/index.html', {'form': AddItemForm})
