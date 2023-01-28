from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.

@login_required(login_url="/login/")
def homepg(request):
    return render(request, 'home.html')


@login_required
def logoutpg(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("")