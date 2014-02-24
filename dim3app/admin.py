from django.contrib import admin

from dim3app.models import Project
from dim3app.models import User
from dim3app.models import Task

admin.site.register(Project)
admin.site.register(User)
admin.site.register(Task)