from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from room.models import Room,Message
from room.forms import RoomForm
from django.http import HttpResponseRedirect
from django.contrib import messages


def rooms(request):
    if request.user.is_authenticated:
        fm=RoomForm()
        rooms=Room.objects.all()
        return render(request,'room.html',{'rooms':rooms,"form":fm})
    else:
        return HttpResponseRedirect('/')



@login_required
def create_room(request):
    if request.method=='POST':
        fm=RoomForm(data=request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect("/rooms/")
        else:
            print(fm)
            messages.success(
                        request, 'Something went wrong')
            return HttpResponseRedirect("/rooms/")
        
@login_required
def find_room(request,slug):
    room_object=Room.objects.get(slug=slug)
    messages=Message.objects.filter(room=room_object)[0:10]
    return render(request,"chat.html",{"room_object":room_object,'msg':messages})



