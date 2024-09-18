from django.contrib import admin
from django.urls import path
from myapp import views
# from django.contrib import admin
# from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name = 'home'),#Map the root URL to the home view
    path('about/', views.about, name = 'about'),# New about page
]