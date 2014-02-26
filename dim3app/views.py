from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from dim3app.forms import UserForm, UserAccForm
from django.contrib.auth import authenticate, login

cont = {'header':"Collaborative Requirement Tracker Team T",
		'title':"Team T Distributed Information Management 3 Project",
		'description':"Tasked to create a collaborative system to sort, prioritise and organise requirements ala Trello. To be made in Django.",
		'members': "Team Members: Alastair Weir (110682w), Keir Smith, Peter Yordanov, Gordon Adam, Georgi Dimitrov",
		}


def index(request):
	context = RequestContext(request)
	return render_to_response('webapp/index.htm',cont, context)

def create(request):
	context = RequestContext(request)
	return render_to_response('webapp/create.htm',cont, context)

def plist(request):
	context = RequestContext(request)
	return render_to_response('webapp/plist.htm',cont, context)

def collaborate(request):
	context = RequestContext(request)
	return render_to_response('webapp/collaborate.htm',cont, context)

def about(request):
	context = RequestContext(request)
	return render_to_response('webapp/about.htm',cont, context)

def register(request):

	context = RequestContext(request)
	registered = False


	if request.method == 'POST':
		u_form = UserForm(data=request.POST)
		acc_form = UserAccForm(data=request.POST)

		if u_form.is_valid() and acc_form.is_valid():
			user = u_form.save()

			user.set_password(user.password)
			user.save()
			profile = acc_form.save(commit=False)
			profile.user = user

			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

			profile.save()
			registered = True

		else:
			print u_form.errors, acc_form.errors

	else:
		u_form = UserForm()
		acc_form = UserAccForm()

	return render_to_response(
		'webapp/register.htm',
		{'u_form': u_form, 'acc_form': acc_form, 'registered': registered},
		context)

def login(request):

	context = RequestContext(request)

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username,password=password)

		if user is not None:
			if user.is_active:
				login(request)
				return HttpResponseRedirect('webapp/index.htm')

			else:
				return HttpResponse("Account error.")
		else:
			print "Invalid username/password: {0}, {1}".format(username, password)

	else:

		return render_to_response('webapp/login.htm',cont, context)

def user_logout(request):

	logout(request)

	return HttpResponseRedirect('/')
