from django.forms import ModelForm
from core.models import *
from django import forms
from bootstrap_datepicker_plus import DateTimePickerInput

class CreateEventForm(ModelForm):
    class Meta:
        model = Event
        fields =  ["title","customer","start","end","is_delete",]
        widgets = {
            'start': DateTimePickerInput(format='%d/%m/%Y HH:MM'), 
            'end': DateTimePickerInput(format='%d/%m/%Y HH:MM'), 
        }