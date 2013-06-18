from django.shortcuts import redirect, HttpResponse
from django.shortcuts import render_to_response

def user_page(request):
    """Per user page"""
    return render_to_response("users/index.html")

def user_login(request):
    """ Function name says it all """
    # return HttpResponse("Login page coming soon:)")
    return redirect('/users') #skip login for now

def phone_client(request):
    """ Function to store the data from phone calls """
    print 'here'
    return render_to_response("users/phone/index.html")


def chat_client(request):
    """ Function to store the data from chats """
    print 'here'
    return render_to_response("users/chat/index.html")


def note_client(request):
    """ Function to store the data from notes """
    print 'here'
    return render_to_response("users/note/index.html")