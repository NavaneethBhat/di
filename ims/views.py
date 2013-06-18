from django.shortcuts import redirect, HttpResponse
from django.shortcuts import render_to_response
from ims.forms import PhoneForm
from django.template import RequestContext

def user_page(request):
    """Per user page"""
    return render_to_response("users/index.html")

def user_login(request):
    """ Function name says it all """
    # return HttpResponse("Login page coming soon:)")
    return redirect('/users') #skip login for now

def phone_client(request):
    """ Function to store the data from phone calls """
    # print 'here'
    # return render_to_response("users/phone/index.html")
    if request.method == 'POST':
        phone_form = PhoneForm(request.POST)
        if phone_form.is_valid():
            phone_form.save()
            return HttpResponse("Done")
    else:
        phone_form = PhoneForm()
    return render_to_response('users/phone/index.html', {'phone_form': phone_form,},context_instance=RequestContext(request))



def chat_client(request):
    """ Function to store the data from chats """
    return render_to_response("users/chat/index.html")


def note_client(request):
    """ Function to store the data from notes """
    return render_to_response("users/note/index.html")

# def add_