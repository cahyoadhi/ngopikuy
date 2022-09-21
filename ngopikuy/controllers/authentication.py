from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, AdminPasswordChangeForm
from ngopikuy.forms import CreateUserForm, AccountForm
from ngopikuy.controllers.decorators import unauthenticated_user, admin_only
from django.shortcuts import redirect, render
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Group, User

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

@admin_only
def UserList(request):
    admin = User.objects.filter(groups__name='admin')
    staff = User.objects.filter(groups__name='employee')
    customer = User.objects.filter(groups__name='customer')
    context = {'admin': admin, 'staff': staff, 'customer': customer}
    return render (request, 'account/user_management.html',context)


@admin_only
def EditUser(request, pk):
    instance = get_object_or_404(User, id=pk)
    form = AccountForm(instance=instance)
    if request.method=='POST':
        form = AccountForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, "Update Success!")
    return render(request, 'account/user_edit.html', {'form':form, 'order':instance})    

@admin_only
def DeleteUser(request, pk):
    User.objects.get(id=pk).delete()
    messages.success(request, 'Account deleted!')
    return redirect('userlist')