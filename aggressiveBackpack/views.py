from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
	context = RequestContext(request)
	return render_to_response('aggressiveBackpack/index.html', context)
	
def dashboard(request):
	context = RequestContext(request)
	return render_to_response('aggressiveBackpack/dashboard.html', context)

def settings(request):
	context = RequestContext(request)
	return render_to_response('aggressiveBackpack/settings.html', context)
	
def register(request):
	context = RequestContext(request)
	return render_to_response('aggressiveBackpack/register.html', context)

def login(request):
	context = RequestContext(request)
	return render_to_response('aggressiveBackpack/login.html', context)

def logout(request):
	context = RequestContext(request)
	return render_to_response('aggressiveBackpack/logout.html', context)

def new_project(request):
	context = RequestContext(request)
	return render_to_response('aggressiveBackpack/new_project.html', context)
