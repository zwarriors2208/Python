from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
def login_view(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') #Redirect to home after successful login
        else:
            messages.error(request,'Invalid username or password.')
    return render(request,'accounts/login.html')
# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']