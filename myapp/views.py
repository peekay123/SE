from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Events
from .models import Events2
from .models import Events1
from .models import Booking
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login as login__P, logout as logout__P
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
# Create your views here.


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login__P(request, user)
            return redirect('Df')
        else:
            messages.info(request, 'Username OR Password is Incorrect')
    return render(request, 'login.html')


def signup(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was Created for ' + user)
            return redirect('loginPage')

    return render(request, 'signup.html', {"form": form})

def index(request):
    return render(request, "index.html")

def events(request):
    eevnts = Events1.objects.all()
    return render(request, 'events.html',  {'eevnts': eevnts})

def events1(request):
    evntsss = Events2.objects.all()
    return render(request, 'events1.html', {'evntsss': evntsss})



def events2(request):
    evnts = Events.objects.all()

    return render(request, 'events2.html', {'evnts': evnts})

@login_required(login_url='loginPage')
def mission(request):
    all_data = Booking.objects.all().order_by("-date")
    return render(request, 'View.html', {"messages": all_data})

@login_required(login_url='loginPage')
def Df(request):
    if request.method == "POST":
        nm = request.POST["name"]
        dt = request.POST["date"]
        strt = request.POST["start"]
        ed = request.POST["end"]
        fld = request.POST["field"]

        data = Booking(name=nm, date=dt, start=strt, end=ed, field=fld,)
        data.save()
        messages.success(request, 'Succesfully Booked')
    return render(request, 'Booking.html')

# @login_required(login_url='loginPage')
def logout(request):
    logout__P(request)
    return render(request, 'index.html')

