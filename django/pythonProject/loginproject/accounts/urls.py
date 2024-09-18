from django.urls import path

from accounts import views # here . is current folder
urlpatterns = [
    path('login/', views.login_view, name='login'),
]