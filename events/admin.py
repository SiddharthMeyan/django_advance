from django.contrib import admin
from .models import Event, Venue, Profile
# Register your models here.


admin.site.register(Event)
admin.site.register(Venue)
admin.site.register(Profile)