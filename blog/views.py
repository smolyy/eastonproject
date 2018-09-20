from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def post_list(request):
    n = ['Maksim', 'Anton', 'Masha']
    return render(request, 'blog/index.html', context={'names' : n})