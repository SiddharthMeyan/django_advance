from django.urls import path
from events import views

urlpatterns = [
    path('',views.home,name='home'),
    path('contact',views.contact, name='contact'),
]
