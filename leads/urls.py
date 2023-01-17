from django.urls import path
from .views import *


app_name = 'leads'

urlpatterns = [
    path('', lead_list),
    path('<int:pk>/', lead_detail),
    path('create/', lead_create),
]
