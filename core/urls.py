from django.contrib import admin
from django.urls import path,include
from core.views import *

urlpatterns = [
      path('',HomePage.as_view(), name='home'),  
      path('create_modal',EventCreate.as_view(), name='createevent'),  
      path('calendar',calendar_list, name='calendar'),  
     
      path('update',update, name='update'),  
      path('delete',delete, name='delete'),  
]
