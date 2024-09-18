from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    # return HttpResponse("Hello, world. You're at the polls home view.")
    return render(request, 'myapp/home.html')
# Create your views here.

def about(request):
    # return HttpResponse("this is About page")
    return render(request, 'myapp/about.html')