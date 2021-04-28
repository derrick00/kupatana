from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required


def user_login(request):
    if request.method =='POST':   #if User_login is called with request
        form = LoginForm(request.POST)   #instanntiate a new login formto dispaly intemplate
        if form.is_valid():    #check whether form is valid
            cd = form.cleaned_data
            user = authenticate(request, #authenticates the user in database takes the request object,the pass and usename parameters
                                username=cd['username'],
                                password=cd['password'])
            if user is not None: #if user was successfully authenticated
                if user.is_active:
                    login(request, user) #you call the login method to set the user in session 
                    return HttpResponse('Authenticated '\
                                        'successfully') #return success message
                else:
                    return HttpResponse('Disabled Account') #if the authenticated user is not active
            else:
                return HttpResponse('invalid login') #if object not authenticated return error message
    else:
        form = LoginForm()  #call the login form again to re enter details
    return render (request, 'account/login.html', {'form': form})


@login_required  #check whether the current user is authenticated
def dashboard(request):
    return render (request,
                   'account/dashboard.html',
                   {'section': 'dashboard'})

# Create your views here.
