from django.shortcuts import render
from .forms import BookNameFilterForm
from .models import Book

def index(request):
    context = {'form':BookNameFilterForm(), 'books':Book.objects.all()}
    return render(request, 'index.html', context)
