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

def signup(request):
    user = request.user
    if user.is_authenticated():
        return redirect('profile')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return redirect('view_profile')
        else:
            print(form.errors)
            return render(request, 'accounts/signup.html', {'form': form} )
    else:
        form = UserCreationForm()
        return render(request, 'accounts/signup.html', {'form': form})	


@login_required
def view_profile(request):
    args = {'user': request.user}

    return render(request, 'accounts/view_profile.html', args)