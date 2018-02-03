from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, update_session_auth_hash
from .forms import UserCreationForm
from django.contrib.auth.views import login as auth_login
from .models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    if request.user.is_authenticated():
        return redirect('profile')
    else:
        return render(request, 'accounts/index.html')