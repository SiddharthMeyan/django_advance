from django.contrib import admin
from .models import Event, Venue, Profile
# Register your models here.


# admin.site.register(Event)
# admin.site.register(Venue)
admin.site.register(Profile)

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    search_fields= ('name','address')
    list_display= ('name','address','phone')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields=(('name','venue'),'event_date','desc','manager')
    search_fields=('name','venue')
    list_display=('name','event_date','venue')
    list_filter=('event_date','venue')
    ordering=('-event_date',)