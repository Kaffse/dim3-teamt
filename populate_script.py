import os, sys
import datetime
from django.contrib.auth.models import User

def populate():



	tag1 = Tag(creation_time = datetime.date.today(), word = "os3", slug="os3")
	tag1.save()

	tag2 = Tag(creation_time = datetime.date.today(), word = "psd3", slug="psd3")
	tag2.save()

	tag3 = Tag(creation_time = datetime.date.today(), word = "ns3", slug="ns3")
	tag3.save()

	tag4 = Tag(creation_time = datetime.date.today(), word = "tp3", slug="tp3")
	tag4.save()

	tag5 = Tag(creation_time = datetime.date.today(), word = "hello world", slug="hello-world")
	tag5.save()

	tag6 = Tag(creation_time = datetime.date.today(), word = "world", slug="world")
	tag6.save()



	p1 = Project(name = "Booking System", description = "undergraduate booking", category = 0)

	p1.save()


	p2 = Project(name = "Collaborative requirements", description = "todo list system", category = 2)

	p2.save()


	p3 = Project(name = "Multi device audio project", description = "multi device recording", category = 3)

	p3.save()



	u1 = UserAcc(user =  User.objects.create_user('user01', 'email1', 'password1'), picture="avatar1.gif")

	u1.save()

	u1.project.add(p1,p2)


	u2 = UserAcc(user =  User.objects.create_user('user02', 'email2', 'password2'), picture="avatar2.gif")

	u2.save()

	u2.project.add(p3)



	u3 = UserAcc(user =  User.objects.create_user('user02', 'email3', 'password3'), picture="avatar3.gif")

	u3.save()

	u3.project.add(p1, p2, p3)




	t1 = Task(name = "task1" ,content = "this is task1", category = "category1", priority='M', progress = 0, deadline = datetime.date.today(), project_id=p1.id)

	t1.save()

	t1.tags.add(tag1)
	t1.assignee.add(u1)


	t2 = Task(name = "task2" ,content = "this is task2", category = "category2", priority='C', progress = 4, deadline = datetime.date.today(), project_id=p1.id)

	t2.save()
	
	t2.tags.add(tag1, tag3)
	t2.assignee.add(u1, u2)


	t3 = Task(name = "task3" ,content = "this is task3", category = "category3", priority='S', progress = 10, deadline = datetime.date.today(), project_id=p2.id)

	t1.save()
	
	t1.tags.add(tag5)
	t1.assignee.add(u3)


	t4 = Task(name = "task4" ,content = "this is task4", category = "category4", priority='W', progress = 5, deadline = datetime.date.today(), project_id=p3.id)

	t1.save()
	
	t1.tags.add(tag1, tag3, tag4, tag6)
	t1.assignee.add(u2)


	t5 = Task(name = "task5" ,content = "this is task5", category = "category5", priority='M', progress = 8, deadline = datetime.date.today(), project_id=p3.id)

	t5.save()
	
	t5.tags.add(tag1, tag2, tag3, tag4, tag6)
	t5.assignee.add(u1, u2, u3)



	fs1 = Friendship(date = datetime.date.today(), initiator = u1, friend = u2)

	fs1.save()


	fs2 = Friendship(date = datetime.date.today(), initiator = u1, friend = u3)

	fs2.save()


	fs3 = Friendship(date = datetime.date.today(), initiator = u3, friend = u2)

	fs3.save()



	print "\n\nProject - user relationship:\n"

	for p in Project.objects.all():
		for u in UserAcc.objects.filter(project = p):
			print "- {0} - {1}".format(str(p), str(u))


	print "\n\nProject - task relationship:\n"

	for p in Project.objects.all():
		for t in Task.objects.filter(project = p):
			print "- {0} - {1}".format(str(p), str(t))


	print "\n\nTag - task relationship:\n"

	for tg in Tag.objects.all():
		for tsk in Task.objects.filter(tags = tg):
			print "- {0} - {1}".format(str(tg), str(tsk))


	print "\n\nProject - Assignee relationship:\n"

	for u in UserAcc.objects.all():
		for t in Task.objects.filter(assignee = u):
			print "- {0} - {1}".format(str(u), str(t))


	print "\n\nFriendship relationships:\n"

	for f in Friendship.objects.all():
		print "- {0} - {1}".format(str(f.initiator), str(f.friend))



if __name__ == '__main__':

	print "Starting dim3 population script..."
	sys.path.append(' /Users/Sreek/django_demo/godjango/bookings')
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dim3.settings')
	from dim3app.models import Project, UserAcc, Task, Tag, Friendship
	populate()

