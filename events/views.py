from django.shortcuts import render, redirect, get_object_or_404
import calendar
from django.contrib import messages

from calendar import HTMLCalendar
from datetime import datetime
from .models import Event, Venue
from .form import VenueForm
# from django.http import HttpResponseRedirect

# Create your views here.
def home(request,year=datetime.now().year,month=datetime.now().strftime('%B')):
    
    month=month.capitalize()
    all_month=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'] 
    if month in all_month:                                   #IF month is in fullform eg: january , february or March
        month_number= list(calendar.month_name).index(month) #convert month to number
    else:                                                    #IF month is in shortform eg: jan, feb or Mar
        month_number= list(calendar.month_abbr).index(month) #convert month to number
    #creating a calendar on the webpage itself
    cal = HTMLCalendar().formatmonth(year,month_number)
    day=datetime.now().day
    context={'month':month, 'year':year,'month_number':month_number,'cal':cal,'day':day}
    return render(request,'home.html',context)


def contact(request):
    return render(request, 'contact.html')



def all_events(request):
    listed_events = Event.objects.all()

    return render(request,'event_list.html',{'listed_events':listed_events}) 

def add_venue(request):
    form = VenueForm()
    if request.method=="POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            venue_name=request.POST.get('name')
            form.save()
            messages.success(request," A new venue: %s, has been added!"%venue_name)
            return redirect('add-venue')

    context={'form':form}
    return render(request,'add_venue.html',context)


def venue_list(request):
    list_venue = Venue.objects.all()
    context={'list_venue':list_venue}
    return render(request,'venue_list.html',context)


def venue_detail(request, venue_id):
    venue= Venue.objects.get(pk=venue_id)
    context={
        'venue':venue
    }
    return render(request,'venue_detail.html',context)

def search_venue(request):
    if request.method=='POST':
        search_term=request.POST.get('search_ob')
        search_res= Venue.objects.filter(name__icontains=search_term)
    
        if len(search_res) is 0:
            messages.warning(request, " The Venue you are searching for isnt available")
        else:
            return render(request,'search_venue.html',{'search_res':search_res, 'search_term':search_term})
    return render(request,'search_venue.html')



def update_venue(request, venue_id): 
    instance = get_object_or_404(Venue, id=venue_id)
    form = VenueForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        messages.success(request, " Changes have been made")
        return redirect('venue-list')
    return render(request, 'update_venue.html', {'form': form})