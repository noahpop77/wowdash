from django.shortcuts import render
from django.http import HttpResponse
from .wowdash import *

posts = getrealms()
#print(posts)
# Create your views here.
def dash(request):
    context = {'posts': posts}
    return render(request, 'dash.html', context)

def about(request):
    return render(request, 'about.html')