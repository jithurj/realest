from django.shortcuts import render,get_object_or_404
from .models import Listings
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from .choices import bedroom_choices,price_choices,state_choices

# Create your views here.
def index(request):
    listing = Listings.objects.order_by('-list_date').filter(is_published = True)
    paginator = Paginator(listing,6)
    page = request.GET.get('page')
    paged_listing = paginator.get_page(page)
    
    context ={
        'listing':paged_listing
        }
    return render(request,'listings/listings.html',context)
def listing(request,listing_id):
    listing = get_object_or_404(Listings,pk = listing_id)
    context = {
        'listn' : listing
    }
    return render(request,'listings/listing.html',context)

def search(request):
    queryset_list = Listings.objects.order_by('-list_date')
    print("request")
    if 'keywords' in request.GET:
        keywords =request.GET['keywords']
        if keywords:
            queryset_list = Listings.objects.order_by('-list_date').filter(description__icontains = keywords)

    if 'city' in request.GET:
        city =request.GET['city']
        if city:
            queryset_list = Listings.objects.order_by('-list_date').filter(city__iexact = city)

    if 'state' in request.GET:
        state =request.GET['state']
        if state:
            queryset_list = Listings.objects.order_by('-list_date').filter(state__iexact = state)

    if 'bedrooms' in request.GET:
        bedrooms =request.GET['bedrooms']
        if bedrooms:
            queryset_list = Listings.objects.order_by('-list_date').filter(bedrooms__lte = bedrooms)

    if 'price' in request.GET:
        price =request.GET['price']
        if price:
            queryset_list = Listings.objects.order_by('-list_date').filter(price__lte = price)
    context= {
        'state_choices': state_choices,
        'bedroom_choices' : bedroom_choices,
        'price_choices' : price_choices,
        'listings' : queryset_list,
        'values' :request.GET
        }
    return render(request,'listings/search.html',context)