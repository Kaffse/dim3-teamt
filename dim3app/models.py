#pyordanov beta models

from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):

	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	description = models.CharField(max_length = 100)

	C0 = 0
	C1 = 1
	C2 = 2
	C3 = 3

	CATEGORY_CHOICES = (
		(C0, 'general'),
		(C1, 'web 2.0'),
		(C2, 'testing'),
		(C3, 'oose'),
	)
	category = models.IntegerField(choices=CATEGORY_CHOICES, default=C0)

	def __unicode__(self):
		return self.name

class UserAcc(models.Model):

	user = models.OneToOneField(User)
	picture = models.ImageField(upload_to='static/data', blank=True)
	project = models.ManyToManyField(Project, related_name='project+')

	# can be removed/changed to a list field to store insterests as tags
    # not really sure why we even want this...
	#interests = models.CharField(max_length=100)

	def __unicode__(self):
		return self.user.username


class Friendship(models.Model):

    date = models.DateTimeField(auto_now_add=True, editable=False)
    initiator = models.ForeignKey(UserAcc, related_name="friendship_initiator")
    friend = models.ForeignKey(UserAcc, related_name="friend_set")


class Tag(models.Model):
	
	creation_time  = models.DateTimeField(auto_now_add=False)
	word        = models.CharField(max_length=35)
	slug        = models.CharField(max_length=250)

	def __unicode__(self):
		return self.word


class Task(models.Model):

	name = models.CharField(max_length = 50, default='task')
	content = models.CharField(max_length = 300)
	category = models.CharField(max_length = 30)

	MUST = 'M'
	SHOULD = 'S'
	COULD = 'C'
	WOULD = 'W'

	PRIORITY_CHOICES = (
		(MUST, 'Must have'),
		(SHOULD, 'Should have'),
		(COULD, 'Could have'),
		(WOULD, 'Would have'),
	)
	priority = models.CharField(max_length=1,choices=PRIORITY_CHOICES,default=MUST)


	ZER = 0
	TEN = 1
	TWE = 2
	THI = 3
	FOR = 4
	FIF = 5
	SIX = 6
	SEV = 7
	EIG = 8
	NIN = 9
	HUN = 10

	PROGRESS_CHOICES = (
		(ZER, '0% (none)'),
		(TEN, '10%'),
		(TWE, '20%'),
		(THI, '30%'),
		(FOR, '40%'),
		(FIF, '50% (halfway)'),
		(SIX, '60%'),
		(SEV, '70%'),
		(EIG, '80%'),
		(NIN, '90%'),
		(HUN, '100% (complete)'),
	)

	progress = models.IntegerField(choices=PROGRESS_CHOICES, default=ZER)
	assignee = models.ManyToManyField(UserAcc, related_name='user+')
	milestone = models.CharField(max_length = 30, default='prototype')
	deadline = models.DateTimeField()
	tags = models.ManyToManyField(Tag,related_name='tasks')

	project = models.ForeignKey(Project)

	def __unicode__(self):
		return self.name

