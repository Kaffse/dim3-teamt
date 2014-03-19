import os


def populate():



	u1 = UserProfile(user =  User.objects.create_user('ghost123456', 'email1', 'password1'), picture="av1.gif", about_me = "start up developer")

	u1.save()




	u2 = UserProfile(user =  User.objects.create_user('dark_Stoner', 'email2', 'password2'), picture="logo.gif", about_me = "student at the University of Glasgow")

	u2.save()




	u3 = UserProfile(user =  User.objects.create_user('death_Cap', 'email3', 'password3'), picture="project.gif", about_me = "game developer at a big company")

	u3.save()




	u4 = UserProfile(user =  User.objects.create_user('Henry_J', 'email4', 'password4'), picture="avatar4.gif", about_me = "business manager")

	u4.save()




	p1 = Project(name = "Booking System", description = "undergraduate booking", owner = u1)

	p1.save()


	p1.team_members.add(u1)
	p1.team_members.add(u2)
	p1.team_members.add(u3)




	p2 = Project(name = "Collaborative requirements", description = "todo list system", owner = u2)

	p2.save()


	p1.team_members.add(u1)
	p1.team_members.add(u3)



	p3 = Project(name = "Multi device audio project", description = "multi device recording", owner = u3)

	p3.save()


	p3.team_members.add(u4)



	p4 = Project(name = "Dancing robot", description = "Clopema dancing robot lvl3 project", owner = u4)

	p4.save()


	p4.team_members.add(u1)
	p4.team_members.add(u2)
	p4.team_members.add(u3)
	p4.team_members.add(u4)




	l1 = List(name = "Artificial Intelligence programming", project=p4)

	l1.save()



	l2 = List(name = "Student booking name list", project=p2)

	l2.save()



	l3 = List(name = "Multi device audio project audio synchronization", project=p3)

	l3.save()




	t1 = Task(title = "how to learn programming" ,description = "the quickest way to learn programming", list = l2, project = p3)

	t1.save()



	t2 = Task(title = "robotic engineering" ,description = "a challenging task", list = l1, project = p4)

	t2.save()



	t3 = Task(title = "small bug" ,description = "the system needs an update", list = l1, project = p3)

	t3.save()



	t4 = Task(title = "decision" ,description = "pros and cons", list = l3, project = p1)

	t4.save()



	t5 = Task(title = "resolve defect" ,description = "strange bug occurs at random occasions", list = l2, project = p2)

	t5.save()




	print "\n\nUser - project relationship:\n"

	for u in UserProfile.objects.all():
		for p in Project.objects.filter(owner = u):
			print "- {0} \t\t - \t\t {1}".format(str(u), str(p))


	print "\n\nList - task relationship:\n"

	for l in List.objects.all():
		for t in Task.objects.filter(list = l):
			print "- {0} \t\t - \t\t {1}".format(str(l), str(t))


	print "\n\nProject - task relationship:\n"

	for p in Project.objects.all():
		for t in Task.objects.filter(project = p):
			print "- {0} \t\t - \t\t {1}".format(str(p), str(t))


	print "\n\nProject - team members relationship:\n"

	for p in Project.objects.all():
		for tm in p.team_members.all():
			print "- {0} \t\t - \t\t {1}".format(str(p), str(tm))




if __name__ == '__main__':


	print "Starting dim3 population script..."

	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dim3.settings")

	from aggressiveBackpack.models import UserProfile, Project, List, Task
	from django.contrib.auth.models import User


	UserProfile.objects.all().delete()
	Project.objects.all().delete()
	List.objects.all().delete()
	Task.objects.all().delete()



	populate()

