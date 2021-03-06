from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listings
from realtors.models import Realtors
from listings.choices import bedroom_choices,price_choices,state_choices
# Create your views here.
def index(request):
    Listing = Listings.objects.order_by('-list_date').filter(is_published= True)[:3]
    context= {
        'listings' : Listing,
        'state_choices': state_choices,
        'bedroom_choices' : bedroom_choices,
        'price_choices' : price_choices

    }
    return render(request,'pages/index.html',context)

def about(request):
    realtors =Realtors.objects.order_by('-hire_date')

    mvp_realtors =Realtors.objects.all().filter(is_mvp = True)
    context = {
        'realtors' : realtors,
        'mvp_realtors' : mvp_realtors
     }
    return render(request,'pages/about.html',context)