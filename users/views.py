from django.shortcuts import render
from django.views import View
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class RegisterView(View):
    def get(self,request):
        create_form = CustomUser()
        context = {
            'form': create_form
        }
        return render(request, 'register.html', context=context)