from django.urls import path, include
from .views import *

urlpatterns = [
    path('', homepage),
    path('mobiles/', mobiles_page),
    path('signup/', signup_view),
    path('signin/', signin_view),
]
