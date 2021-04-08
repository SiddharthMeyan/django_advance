from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event

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