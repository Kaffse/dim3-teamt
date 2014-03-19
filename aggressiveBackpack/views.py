from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from aggressiveBackpack.forms import UserForm, UserProfileForm, NewProjectForm, NewListForm, NewTaskForm
from aggressiveBackpack.models import Project, User, UserProfile, List, Task
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core import serializers


def index(request):
	context = RequestContext(request)
	return render_to_response('aggressiveBackpack/index.html', context)

#Need to add access to the user's friends.
@login_required
def dashboard(request):

		context = RequestContext(request)
		cur_user = User.objects.get(username=request.user)
		cur_pro = UserProfile.objects.get(user=cur_user)
		users_projects = Project.objects.filter(owner=cur_pro)
		friends_projects = Project.objects.all().filter(owner=cur_pro.friends.all())
		template_context = {'userprojects': users_projects, 'friendsprojects': friends_projects}
		template_context['profile']=cur_pro
		template_context['friends'] = cur_pro.friends.all()
		for project in users_projects:
				project.url = project.name.replace(' ', '_')
		for project in friends_projects:
				project.url = project.name.replace(' ', '_')
		return render_to_response('aggressiveBackpack/dashboard.html', template_context, context)

@login_required
def project(request, project_name_url):
		# Request our context from the request passed to us.
		context = RequestContext(request)

		# Change underscores in the category name to spaces.
		# URLs don't handle spaces well, so we encode them as underscores.
		# We can then simply replace the underscores with spaces again to get the name.
		project_name = project_name_url.replace('_', ' ')
		print 'projectname: ' + project_name

		# Create a context dictionary which we can pass to the template rendering engine.
		# We start by containing the name of the category passed by the user.
		context_dict = {'project_name': project_name}

		try:
			# Can we find a project with the given name?
			# If we can't, the .get() method raises a DoesNotExist exception.
			# So the .get() method returns one model instance or raises an exception.
			project = Project.objects.get(name=project_name)

			# Retrieve all of the associated lists.
			# Note that filter returns >= 1 model instance.
			lists = List.objects.filter(project=project)

			# Retrieve all of the associated tasks.
			# Note that filter returns >= 1 model instance.
			tasks = Task.objects.filter(project=project)

			# Add lists to context_dict.
			context_dict['lists'] = lists

			# Add tasks to context_dict
			context_dict['tasks'] = tasks
			# We also add the category object from the database to the context dictionary.
			# We'll use this in the template to verify that the category exists.
			context_dict['project'] = project
			context_dict['projectURL'] = project.name.replace(' ', '_')

		except Project.DoesNotExist:
			print 'Project doesn\'t exist'
			return render_to_response('aggressiveBackpack/no_project_exists.html', context_dict, context)
			pass
			# We get here if we didn't find the specified category.
			# Don't do anything - the template displays the "no category" message for us.

		#Handling the 2 different forms, new list and new task, here
		created = False
		if request.method == 'POST':
				print("into POST")
				#Attempt to access information from both forms
				list_form = NewListForm(data=request.POST)
				task_form = NewTaskForm(data=request.POST)

				#If list_form is valid
				if list_form.is_valid():
					print("into list form validation")
					list = list_form.save(commit=False)
					list.project=project
					list.save()
					created = True

				elif task_form.is_valid():
					print("Into task form validation")
					task = task_form.save()
					created = True

				else:
					print("Neither are valid. In that wee else")
					print("New List errors")
					print list_form.errors
					print("New Task Errors")
					print task_form.errors
		else:
			list_form = NewListForm()
			task_form = NewTaskForm()

		# Go render the response and return it to the client.
		context_dict['list_form'] = list_form
		context_dict['task_form'] = task_form
		context_dict['created'] = created
		return render_to_response('aggressiveBackpack/project.html', context_dict, context)


@login_required
def settings(request):
		context = RequestContext(request)
		return render_to_response('aggressiveBackpack/settings.html', context)


def register(request):
		context = RequestContext(request)

		# A boolean value for telling the template whether the registration was successful.
		# Set to False initially. Code changes value to True when registration succeeds.
		registered = False

		# If it's a HTTP POST, we're interested in processing form data.
		if request.method == 'POST':
			# Attempt to grab information from the raw form information.
			# Note that we make use of both UserForm and UserProfileForm.
			user_form = UserForm(data=request.POST)
			profile_form = UserProfileForm(data=request.POST)

			# If the two forms are valid...
			if user_form.is_valid() and profile_form.is_valid():
				# Save the user's form data to the database.
				user = user_form.save()

				# Now we hash the password with the set_password method.
				# Once hashed, we can update the user object.
				user.set_password(user.password)
				user.save()

				# Now sort out the UserProfile instance.
				# Since we need to set the user attribute ourselves, we set commit=False.
				# This delays saving the model until we're ready to avoid integrity problems.
				profile = profile_form.save(commit=False)
				profile.user = user

				# Did the user provide a profile picture?
				# If so, we need to get it from the input form and put it in the UserProfile model.
				if 'picture' in request.FILES:
					profile.picture = request.FILES['picture']

				# Now we save the UserProfile model instance.
				profile.save()

				# Update our variable to tell the template registration was successful.
				registered = True

			# Invalid form or forms - mistakes or something else?
			# Print problems to the terminal.
			# They'll also be shown to the user.
			else:
				print user_form.errors, profile_form.errors

					# Not a HTTP POST, so we render our form using two ModelForm instances.
					# These forms will be blank, ready for user input.
		else:
			user_form = UserForm()
			profile_form = UserProfileForm()

		#If successfully registered then return to index
		if (registered == True):
			return render_to_response("aggressiveBackpack/index.html",{'registered': registered}, context)

		# Render the template depending on the context.
		return render_to_response(
		'aggressiveBackpack/register.html',
		{'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
		context)


def user_login(request):
		# Like before, obtain the context for the user's request.
		context = RequestContext(request)

		# If the request is a HTTP POST, try to pull out the relevant information.
		if request.method == 'POST':
			# Gather the username and password provided by the user.
			# This information is obtained from the login form.
			username = request.POST['username']
			password = request.POST['password']

			# Use Django's machinery to attempt to see if the username/password
			# combination is valid - a User object is returned if it is.
			user = authenticate(username=username, password=password)

			# If we have a User object, the details are correct.
			# If None (Python's way of representing the absence of a value), no user
			# with matching credentials was found.
			if user is not None:
				# Is the account active? It could have been disabled.
				if user.is_active:
					# If the account is valid and active, we can log the user in.
					# We'll send the user back to their dashboard.
					login(request, user)
					return HttpResponseRedirect('/aggressiveBackpack/dashboard')
				else:
					# An inactive account was used - no logging in!
					return HttpResponse("Your aggressiveBackpack account is disabled.")
			else:
				# Bad login details were provided. So we can't log the user in.
				print "Invalid login details: {0}, {1}".format(username, password)
				return HttpResponse("Invalid login details supplied.")

			# The request is not a HTTP POST, so display the login form.
			# This scenario would most likely be a HTTP GET.
		else:
			# No context variables to pass to the template system, hence the
			# blank dictionary object...
			return render_to_response('aggressiveBackpack/login.html', {}, context)


# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
		# Since we know the user is logged in, we can now just log them out.
		logout(request)

		# Take the user back to the homepage.
		return HttpResponseRedirect('/aggressiveBackpack/')


@login_required
def new_project(request):
		context = RequestContext(request)
		cur_user = User.objects.get(username=request.user)
		cur_pro = UserProfile.objects.get(user=cur_user)
		context_dict = {}
		context_dict['UserProfile'] = cur_pro

		# A boolean value for telling the template whether the new project creation was successful.
		# Set to False initially. Code changes value to True when creation succeeds.
		new_project_created = False

		# If it's a HTTP POST, we're interested in processing form data.
		if request.method == 'POST':
			# Attempt to grab information from the raw form information.
			new_project_form = NewProjectForm(data=request.POST)

			# If the form is valid...
			if new_project_form.is_valid():
				# Save the project's form data to the database.
				new_project = new_project_form.save(commit=False)

				new_project.owner=cur_pro

				new_project.save()

				# Update our variable to tell the template creation was successful.
				new_project_created = True

				# Invalid form or forms - mistakes or something else?
				# Print problems to the terminal.
				# They'll also be shown to the user.
			else:
				print new_project_form.errors

				# Not a HTTP POST, so we render our form using two ModelForm instances.
				# These forms will be blank, ready for user input.
		else:
			new_project_form = NewProjectForm()

		context_dict['new_project_form'] = new_project_form
		context_dict['new_project_created'] = new_project_created
		# Render the template depending on the context.
		return render_to_response(
		'aggressiveBackpack/new_project.html', context_dict, context)

@login_required
def user(request):
	context = RequestContext(request)
	cur_user = User.objects.get(username=request.user)
	cur_pro = UserProfile.objects.get(user=cur_user)
	users_projects = Project.objects.filter(owner=cur_pro)

	context_dict = {'userprojects': users_projects}
	context_dict['profile'] = cur_pro
	for project in users_projects:
			project.url = project.name.replace(' ', '_')
	return render_to_response(
	'aggressiveBackpack/user.html', context_dict, context)

#Only deletes top level project and not its lists and tasks that it contains.
#Theoretically a user could make a new project with the exact same name and access these
#Old tasks and lists?
@login_required
def delete_project(request, project_name_url):
	deleted=False
	project_name = project_name_url.replace("_", " ")
	to_delete = Project.objects.filter(name=project_name)
	to_delete.delete()
	deleted=True
	return render_to_response('/aggressiveBackpack/dashboard.html/', {'deleted':deleted}, context)

def getUsers(request):
    context = RequestContext(request)
    if request.method == 'GET':
        data = User.objects.all()
        data = serializers.serialize("json", data)
        return HttpResponse(data,"application/json")
