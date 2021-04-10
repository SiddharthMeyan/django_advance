from django.urls import path
from events import views

urlpatterns = [
    path('',views.home,name='home'),
    path('<int:year>/<str:month>/',views.home,name='home'),
    path('contact',views.contact, name='contact'),
    path('events',views.all_events, name='events'),
    path('add_venue',views.add_venue, name='add-venue'),
    path('venue_list',views.venue_list, name='venue-list'),
    path('venue_detail/<venue_id>',views.venue_detail, name='venue-detail'),
    path('search_venue',views.search_venue, name='search-venue'),
    path('update_venue/<venue_id>',views.update_venue, name='update-venue'),
]
