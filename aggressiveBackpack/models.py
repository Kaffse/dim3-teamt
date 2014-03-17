from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from markdown import markdown

#https://djangosnippets.org/snippets/882/
class MarkdownTextField (TextField):
    """
    A TextField that automatically implements DB-cached Markdown translation.

    Accepts two additional keyword arguments:

    if allow_html is False, Markdown will be called in safe mode,
    which strips raw HTML (default is allow_html = True).

    if html_field_suffix is given, that value will be appended to the
    field name to generate the name of the non-editable HTML cache
    field.  Default value is "_html".

    NOTE: The MarkdownTextField is not able to check whether the model
    defines any other fields with the same name as the HTML field it
    attempts to add - if there are other fields with this name, a
    database duplicate column error will be raised.

    """
    def __init__ (self, *args, **kwargs):
        self._markdown_safe = not kwargs.pop('allow_html', True)
        self._html_field_suffix = kwargs.pop('html_field_suffix', '_html')
        super(MarkdownTextField, self).__init__(*args, **kwargs)

    def contribute_to_class (self, cls, name):
        self._html_field = "%s%s" % (name, self._html_field_suffix)
        TextField(editable=False).contribute_to_class(cls, self._html_field)
        super(MarkdownTextField, self).contribute_to_class(cls, name)

    def pre_save (self, model_instance, add):
        value = getattr(model_instance, self.attname)
        html = markdown(value, safe_mode=self._markdown_safe)
        setattr(model_instance, self._html_field, html)
        return value

    def __unicode__ (self):
        return self.attname

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
    description = models.MarkdownTextField('Description' blank=True)
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
    description = models.MarkdownTextField( blank=True, null=True)
    tags = TaggableManager(blank=True)

    def __unicode__(self):
        return self.project.name + ":" + self.list.name + ":" + self.title
