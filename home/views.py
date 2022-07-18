from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'index.html')

def signup_view(request):
    return render(request, 'signup.html')

def signin_view(request):
    return render(request, 'signin.html')