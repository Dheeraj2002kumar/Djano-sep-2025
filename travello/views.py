from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):

    # access Destination class and  create object
    # dest1 = Destination()
    # dest1.name = 'California'
    # dest1.desc = 'United State of America (California)'
    # dest1.img = '1.png'
    # dest1.price = 700

    # dest2 = Destination()
    # dest2.name = 'Korola Megna'
    # dest2.desc = 'United State of America (Korola Megna)'
    # dest2.img = '2.png'
    # dest2.price = 800

    # dest3 = Destination()
    # dest3.name = 'London'
    # dest3.desc = 'United State of America (London)'
    # dest3.img = '3.png'
    # dest3.price = 900

    # dest4 = Destination()
    # dest4.name = 'Miami Beach'
    # dest4.desc = 'United State of America (Miami Beach)'
    # dest4.img = '4.png'
    # dest4.price = 700

    # dest5 = Destination()
    # dest5.name = 'California'
    # dest5.desc = 'United State of America (California)'
    # dest5.img = '5.png'
    # dest5.price = 950
    
    # dest6 = Destination()
    # dest6.name = 'Saintmartine Iceland'
    # dest6.desc = 'United State of America (Saintmartine Iceland)'
    # dest6.img = '6.png'
    # dest6.price = 800
    
    # dest7 = Destination()
    # dest7.name = 'Saintmartine Iceland'
    # dest7.desc = 'United State of America (Saintmartine Iceland)'
    # dest7.img = '6.png'
    # dest7.price = 800

    # dests = [dest1, dest2, dest3, dest4, dest5, dest6, dest7]


    dests = Destination.objects.all()

    return render(request, "index.html", {'dests': dests})