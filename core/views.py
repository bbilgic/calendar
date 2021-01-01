from django.shortcuts import render, redirect,HttpResponse,HttpResponseRedirect
from django.utils import timezone
from django.views import View
import pandas as pd 
import json 
from django.core import serializers
from django.http import JsonResponse
import threading
from django.http import HttpResponse
from core.models import *
from datetime import datetime
from django.urls import reverse_lazy,reverse
from django.contrib import messages
import os
import traceback
from django.views.generic.edit import CreateView, UpdateView, DeleteView,FormView
from core.forms import *

def create(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event = Event(name=str(title), start=start, end=end)
    event.save()
    data = {}
    return JsonResponse(data)


def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Event.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data)


def delete(request):
    id = request.GET.get("id", None)
    event = Event.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)


class HomePage(View): 
    template_name ='base.html'

    def get(self,request, **kwargs):
        all_events = Event.objects.all()
        context = {
                "events":all_events,
            }

        return render(request,template_name=self.template_name,context=context)


def calendar_list(request):

    all_events = Event.objects.all().values()

    return JsonResponse(list(all_events), safe=False)


class EventCreate(CreateView): 
    
    model = Event
    form_class = CreateEventForm
    
    template_name ='create_modal.html'
    success_url='/'

    def form_valid(self, form):
        model_instance = form.save(commit=False)
        model_instance.create_user = self.request.user

        self.object= form.save()
        return HttpResponseRedirect(self.get_success_url())