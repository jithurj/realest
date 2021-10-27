from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Contact
# Create your views here.
def contact(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        listing = request.POST.get('listing')

        contact = Contact(name=name,listing_id = listing_id, listing = int(listing),email = email,phone =phone,message =message,user_id=user_id,realtor_email=realtor_email)
        contact.save()

        messages.success(request,"Your request has been submited , a realtor will get back to you soon ")
        
        return redirect('/listings/'+listing_id)