from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

cont = {'header':"Collaborative Requirement Tracker Team T",
		'title':"Team T Distributed Information Management 3 Project",
		'description':"Tasked to create a collaborative system to sort, prioritise and organise requirements ala Trello. To be made in Django.",
		'members': "Team Members: Alastair Weir (110682w), Keir Smith, Peter Yordanov, Gordon Adam, Georgi Dimitrov"
		}


def index(request):
	context = RequestContext(request)
	return render_to_response('webapp/index.htm',cont, context)
	
def create(request):
	return HttpResponse("create task <a href='/'>home</a>")
	
def plist(request):
	context = RequestContext(request)
	return render_to_response('webapp/plist.htm',cont, context)
	
def collaborate(request):
	return HttpResponse("collab <a href='/'>home</a>")
	
def about(request):
	context = RequestContext(request)
	return render_to_response('webapp/about.htm',cont, context)
	
def register(request):
	return HttpResponse("register form here <a href='/'>home</a>")

def login(request):
	return HttpResponse("login here <a href='/'>home</a>")
