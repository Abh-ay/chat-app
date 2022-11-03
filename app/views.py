from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate
from .forms import SignUpForm,LoginForm
from django.shortcuts import redirect,render
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages


def loginView(request):
    if request.method=='POST':
            if not request.user.is_authenticated:
                fm = LoginForm(request=request, data=request.POST)
                print(fm)
                if fm.is_valid():
                    uname = fm.cleaned_data['username']
                    password = fm.cleaned_data['password']
                    user = authenticate(username=uname, password=password)
                    if user is not None:
                        login(request, user)
                        
                        return HttpResponseRedirect('/rooms/')
                    return render(request, 'login.html', {'form': fm})
                else:
                    print("FM IS NOT VALID LOGIN FORM========")
                    return HttpResponseRedirect('/')
                    
            else:
                return HttpResponseRedirect('/rooms/')
    else:
        if request.user.is_authenticated:
            messages.success(request,"User is already Logged in")
            return HttpResponseRedirect('/rooms/')
        else:
            return render(request, 'login.html', {'form': LoginForm()})





# def room(request, room_name):
#     username = request.GET.get('username', 'Anonymous')
#     return render(request, 'room.html', {'room_name': room_name, 'username': username})




def signup(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return HttpResponseRedirect('/rooms/')
        else:
            return render(request,'signup.html',{'form':form})
    else:
        if request.user.is_authenticated:
            messages.success(request,"User is already Logged in")
            return HttpResponseRedirect('/rooms/')
        else:
            form=SignUpForm()
            return render(request,'signup.html',{'form':form})


def logoutView(request):
    logout(request)
    return HttpResponseRedirect('/')