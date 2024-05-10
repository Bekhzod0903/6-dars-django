from django.urls import path
from .views import RegisterView

app_name = 'users'  # Ensure correct app name

urlpatterns = [  # Corrected the variable name
    path('register/', RegisterView.as_view(), name='register'),  # Ensure correct import and path
]
