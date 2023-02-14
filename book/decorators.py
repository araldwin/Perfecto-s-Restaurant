from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    '''
    if you do the @unauthenticated_user above the function
    it will pass through the functio if it is authenticated
    and it will send the user to home page or if it is not
    authenticated it will call the original function
    '''
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')
        return wrapper_func
    return decorator


def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'customer':
            return redirect('user-page')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func
        