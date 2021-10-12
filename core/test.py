from django.shortcuts import redirect
from django.conf import settings

def printit(request):
  
    print(request.session[settings.CART_SESSION_KEY])
    return redirect('home_url')