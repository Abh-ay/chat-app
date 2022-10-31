from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.loginView, name="index"),
    path("signup/",views.signup,name="signup"),
    path("logout/",views.logoutView,name="logout"),
    # path("<str:room_name>/", views.room, name="room"),
]