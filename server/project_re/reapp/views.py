from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

months = {
    "January": "14 January Makar Sankranti, 26 January Republic Day",
    "February": "19 February Shivaji Jayanti",
    "March": "8 March Maha-shivratri, 25 March Holi",
    "April": "9 April Gudhi Padwa, 11 April Ramzan Eid, 14 April Ambedkar Jayanti",
    "May": "1 May International Worker's Day",
    "June": "17 June Bakri Eid",
    "July": "21 July Guru Purnima",
    "August": "15 August Independence Day, 19 August Raksha Bandhan, 26 August Janmashtami",
    "September": "7 September Ganesh Chaturthi",
    "October": "12 October Dussehra, 31 October Diwali",
    "November": "3 November Bhaubij, 15 Guru Nanak Jayanti",
    "December": "25 December Mary Christmas",
}

@api_view(['GET', 'POST'])
def home(request):
    month_name = request.query_params.get("name", "").capitalize()

    if month_name:
        if month_name in months:
            msg = f"Holidays in {month_name} are {months[month_name]}"
        else:
            msg = "Month not Found"
    else:
        msg = "Available months are: " + ", ".join(months.keys())

    return Response({"msg": msg})
