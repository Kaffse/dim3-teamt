from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
	context = RequestContext(request)
	cont = {'boldmessage':"test bold"}
	return render_to_response('webapp/index.htm',cont, context)
	
def create(request):
	return HttpResponse("create task <a href='/'>home</a>")
	
def plist(request):
	return HttpResponse("project list <a href='/'>home</a>")
	
def about(request):
	return HttpResponse("about <a href='/'>home</a>")
