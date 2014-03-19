from django.contrib import admin

from aggressiveBackpack.models import UserProfile, Project, List, Task


admin.site.register(UserProfile)
admin.site.register(Project)
admin.site.register(List)
admin.site.register(Task)
