####  APP LEVEL ####

from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('options/', views.OptionList.as_view(), name='option-list'),
    # Add more URL patterns that this app handles
]