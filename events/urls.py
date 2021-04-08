from django.urls import path
from events import views

urlpatterns = [
    path('',views.home,name='home'),
    path('<int:year>/<str:month>/',views.home,name='home'),
    path('contact',views.contact, name='contact'),
    path('events',views.all_events, name='events'),
]
