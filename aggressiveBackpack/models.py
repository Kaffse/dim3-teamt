from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    # The additional attributes we wish to include.
    friends = models.ManyToManyField('self', blank=True, null=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    projects = models.ManyToManyField('Project', blank=True)
    website = models.URLField(blank=True)
    about_me = models.CharField(max_length=400, blank=True)

    # This line is required. Links UserProfile to a User model instance.
    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username


#Project model.
#Attributes = name, website, team members
#Many users can have many projects
class Project(models.Model):
    owner = models.ForeignKey(UserProfile, related_name='owner_relation')
    name = models.CharField(max_length=128)
    description = models.TextField()
    picture = models.ImageField(upload_to='project_images', blank=True)
    website = models.URLField(blank=True)
    team_members = models.ManyToManyField('UserProfile', blank=True, related_name='team_members_relation')
    tags = TaggableManager(blank=True)

    def __unicode__(self):
        return self.name


class List(models.Model):
    #Many lists belong to one project
    project = models.ForeignKey(Project, related_name='project_relation')
    name = models.CharField(max_length=128)
    #tasks = models.ManyToManyField('Task', related_name='tasks_relation', blank=True, null=True)
    colour = models.CharField(max_length=10, blank=True)

    def __unicode__(self):
        return self.project.name + ":" + self.name


#NOTE! - Abstracting the tags (category, progress and priority) to project level.
class Task(models.Model):
    #Many tasks belong to one list
    list = models.ForeignKey('List', related_name='owning_list_relation')
    project = models.ForeignKey(Project, related_name='owning_project_relation')
    title = models.CharField(max_length=100)
    description = models.TextField()
    tags = TaggableManager(blank=True)

    def __unicode__(self):
        return self.project.name + ":" + self.list.name + ":" + self.title
