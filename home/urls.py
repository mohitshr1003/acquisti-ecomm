from django.urls import path, include
from .views import *

urlpatterns = [
    path('', homepage),
    path('signup/', signup_view),
    path('signin/', signin_view),
    path('mobiles/',mobilespage),
]
