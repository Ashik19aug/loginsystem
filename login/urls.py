
from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    # path('', views.home, name='home'),
]
