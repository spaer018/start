from django.shortcuts import render
import datetime


def home(request):
    date = datetime.datetime.now().date()
    time = datetime.datetime.now().time()
    name = 'Dave'
    _context = {'date':date,'name':name,'time':time}
    return render(request, 'home.html', _context)
