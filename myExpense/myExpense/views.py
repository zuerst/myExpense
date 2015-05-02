import datetime
import urllib2

from django.contrib import auth
from django.core.context_processors import csrf
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import Context, loader, RequestContext
from django.utils import timezone

from forms import RegistrationForm
from models import *


def test(request):
	u = User.objects.get(id = 1)
	c = Category.objects.get(mainCategory = 'Drink')
	t = Transaction(title = 'test title', description = 'test description', transType = 'Debit', amount = 100, date = '2015-05-01', category = c, user = u)
	t.save()
	return render_to_response('login.html')

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def auth_view(request):
    # GET username, if there is no valid data, return ''.
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username = username, password = password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid_login')

def loggedin(request):
    c = {}
    c.update(csrf(request))
    c['username'] = request.user.username
    test = request.POST.get('title', '')
    return HttpResponseRedirect('/')

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')

def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')
        else:
            return render_to_response('register.html', {'form': form})
    args = {}
    args.update(csrf(request))
    args['form'] = RegistrationForm()
    return render(request, 'register.html', args)

def register_success(request):
    return render_to_response('register_success.html')