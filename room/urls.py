from django.urls import path
from . import views

urlpatterns = [
    path('',views.rooms,name='rooms'),
    path("<slug:slug>",views.find_room,name="find_room"),
    path('create-room/',views.create_room,name='CreateRooms'),
    
]
