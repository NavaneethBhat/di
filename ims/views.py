from django.shortcuts import redirect, HttpResponse
from django.shortcuts import render_to_response

def user_page(request):
    """Per user page"""
    return redirect('/login') #if not logged in redirect to login

def user_login(request):
    """ Function name says it all """
    return HttpResponse("Login page coming soon:)")
    # return render_to_response("users/index.html")
