from django.contrib import admin

# Register your models here.

from tasks.models import Project, Task, User


admin.site.register(Project)
admin.site.register(Task)
admin.site.register(User)