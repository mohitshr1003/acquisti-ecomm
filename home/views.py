from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def homepage(request):
    return render(request, 'index.html')


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

    data = {}

    if(request.method == 'POST'):
        qs = UserDetails.objects.filter(
            user_email = request.POST.get('mail_id'),
            password = request.POST.get('psw')
            )
        
        info = {'query_set': qs}

        if qs:
            return redirect('../', context=info)
        else:
            data['result'] = 'Invalid Details'
            return render(request, 'signin.html', context=data)
    return render(request, 'signin.html')