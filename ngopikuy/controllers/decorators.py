from django.shortcuts import redirect

# use this for register page and login page. 
def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('employee')
		else:
			return view_func(request, *args, **kwargs)
	return wrapper_func

def employee_only(view_func):
	def wrapper_func(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name
		if group == 'customer':
			return redirect('customer')
		elif group == 'employee':
			return view_func(request, *args, **kwargs)
		elif group == 'admin':
			return view_func(request, *args, **kwargs)
	return wrapper_func

def admin_only(view_func):
	def wrapper_func(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name
		if group == 'customer':
			return redirect('customer')
		elif group == 'employee':
			return redirect('dashboard')
		elif group == 'admin':
			return view_func(request, *args, **kwargs)
	return wrapper_func
