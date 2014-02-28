from django.contrib import admin

from dim3app.models import Project
from dim3app.models import UserAcc
from dim3app.models import Task
from dim3app.models import Friendship
from dim3app.models import Tag

admin.site.register(Project)
admin.site.register(UserAcc)
admin.site.register(Task)
admin.site.register(Friendship)
admin.site.register(Tag)