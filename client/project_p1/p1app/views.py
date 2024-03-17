from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .forms import MonthForm


# Create your views here.

months = {
    "January": "14 January Makar Sankrati ,    26 January Republic Day",
    "February": "19 February Shivaji Jayanti",
    "March": "8 March Maha-shivratri  , 25 March Holi   ",
    "April": "9 April Gudhi Padwa  , 11 April  Ramzan Eid ,  14 April  Ambedkar Jayanti  ",
    "May": "1 May International Worker's Day  ",
    "June": "17 June Bakri eid",
    "July": "21 July Guru Purnima",
    "August": "15 August  Independence Day , 19 August  Raksha Bandhan , 26 August  Janmashtami",
    "September": "7 September Ganesh Chaturthi",
    "October": "12 October Dussehra ,  31 October  Diwali   " ,
    "November": "3 November  Bhaubij  , 15 Guru Nanak Jayanti  ",
    "December": "25 December  Mary Christmas ",
}


@api_view(["GET" , "POST"])

def home(request):
    if request.method == "POST":
        form = MonthForm(request.POST)
        if form.is_valid():
            selected_date = form.cleaned_data['selected_date']
            # Extract the month in title case format (e.g., "January")
            month_name = selected_date.strftime('%B')
            if month_name in months:
                events = months[month_name]
                return render(request, "nh.html", {"msg": f"Holidays in {month_name} are: {events}"})
            else:
                return render(request, "nh.html", {"msg": "Month not found"})
    else:
        form = MonthForm()

    return render(request, "home.html", {"form": form})

def nh(request) :
	return render(request , "nh.html")