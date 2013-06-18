from django.db import models
from django import forms
from django.forms import ModelForm
from ims.models import PhoneClient

class PhoneForm(ModelForm):
    class Meta:
        model = PhoneClient
        # fields = ['pub_date', 'headline', 'content', 'reporter']
        exclude = ('ph_id','user_id',)#),'client_name','subject',)
        # Name_of_the_client = forms.CharField(label='Client Name',required=True)
        # Subject = forms.CharField(label='Subject',required=True)
