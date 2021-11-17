from django.urls import path

from . import views

urlpatterns = [
    path('login.html', views.login, name="loginPage"),
    path('signup.html', views.signup, name="signup"),
    path('', views.index, name="index"),
    path('events.html', views.events, name="events"),
    path('View.html', views.mission, name="mission"),
    path('Booking.html', views.Df, name="Df"),
    path('logout.html', views.logout, name="logout"),
]
