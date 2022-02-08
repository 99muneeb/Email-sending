from django.urls import path
from . import views

urlpatterns = [
    path('', views.Email_send, name = 'email_send'),
    
]