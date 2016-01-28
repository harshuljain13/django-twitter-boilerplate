from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

# from django.template.context import RequestContext


def login(request):
    # context = RequestContext(request, {
    #     'request': request, 'user': request.user})
    # return render_to_response('login.html', context_instance=context)
    return render(request, 'django_social_app/login.html')


@login_required(login_url='/')
def home(request):
    return render_to_response('django_social_app/home.html')


def logout(request):
    auth_logout(request)
    return redirect('/')
