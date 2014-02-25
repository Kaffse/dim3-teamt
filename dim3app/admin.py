from django.contrib import admin

from dim3app.models import Project
from dim3app.models import UserAcc
from dim3app.models import Task

admin.site.register(Project)
admin.site.register(UserAcc)
admin.site.register(Task)