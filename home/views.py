from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def homepage(request):
    return render(request, 'index.html')

def mobilespage(request):
    return render(request, 'mobiles.html')

def signup_view(request):

    if(request.method == 'POST'):
        user_first_name = request.POST.get('fname')
        user_last_name = request.POST.get('lname')
        user_email = request.POST.get('email_id')
        user_phone = request.POST.get('phn')
        user_address = request.POST.get('adrs')
        user_password = request.POST.get('pswd')

        account_registration = UserDetails(
            first_name = user_first_name,
            last_name = user_last_name,
            user_email = user_email,
            phone = user_phone,
            address = user_address,
            password = user_password
        )
        account_registration.save()
        messages.success(request, f'Your account has been created ! You are now able to log in')
        return render(request, 'signin.html')
    return render(request, 'signup.html')

def signin_view(request):

    return render(request, 'signin.html')