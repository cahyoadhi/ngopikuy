from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm 
from ngopikuy.forms import CreateUserForm  
from ngopikuy.controllers.decorators import unauthenticated_user
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import Group

# register page, default user is 'customer' group
@unauthenticated_user
def RegisterPage(request):
    if request.method=='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()  
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            messages.success(request, 'Account was created for ' +username+' . Please login')

    else:  
        form = CreateUserForm()  
    context = {'form':form}  
    return render(request, 'account/register.html', context)  

# login page
@unauthenticated_user
def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate (request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, "Username or password is incorrect")
    form = AuthenticationForm()

    context = {'form':form}
    return render (request, 'account/login.html', context)

# logout
def LogoutUser(request):
    logout(request)
    return redirect('login')