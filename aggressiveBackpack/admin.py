from django.contrib import admin

from aggressiveBackpack.models import Project
from aggressiveBackpack.models import User
from aggressiveBackpack.models import Task

admin.site.register(Project)
admin.site.register(User)
admin.site.register(Task)