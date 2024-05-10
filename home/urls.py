from django.urls import path
from .views import landing_page

ulpatterns = [
    path('', landing_page, name='landing_page'),
]