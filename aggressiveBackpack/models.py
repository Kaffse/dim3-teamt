from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

#Used to list collaborators on projects and track friends lists
#Borrowed from http://stackoverflow.com/a/1113039/1254402
class SeparatedValuesField(models.TextField):
    __metaclass__ = models.SubfieldBase

    def __init__(self, *args, **kwargs):
        self.token = kwargs.pop('token', ',')
        super(SeparatedValuesField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value: return
        if isinstance(value, list):
            return value
        return value.split(self.token)

    def get_db_prep_value(self, value):
        if not value: return
        assert (isinstance(value, list) or isinstance(value, tuple))
        return self.token.join([unicode(s) for s in value])

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    # The additional attributes we wish to include.
    friends = SeparatedValuesField()
    picture = models.ImageField(upload_to='profile_images', blank=True)
    projects = models.ManyToManyField('Project')
    # This line is required. Links UserProfile to a User model instance.
    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

#Project model.
#Attributes = name, website, team members
#Many users can have many projects

#Using django-taggit to simplify tags
#http://django-taggit.readthedocs.org/en/latest/getting_started.html
class Project(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=300)
    picture = models.ImageField(upload_to='project_images', blank=True)
    website = models.URLField(blank=True)
    team_members = SeparatedValuesField()
    tags = TaggableManager()

class List(models.Model):
    #Many lists belong to one project
    project = models.ForeignKey(Project)
    tasks = models.ManyToManyField('Task')
    name = models.CharField(max_length=128)
    colour = models.CharField(max_length=10)

#NOTE! - Abstracting the tags (category, progress and priority) to project level.
class Task(models.Model):
    #Many tasks belong to one list
    belong_to_list = models.ForeignKey(List)

    #Standard title & description
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

#NOTE! - Abstracting the tags (category, progress and priority) to project level.
#class Tag(models.Model):
#    project = models.ManyToManyField('Project')
#    #User assigns each tag a colour. hex code.
#    colour = models.CharField(max_length=10)
