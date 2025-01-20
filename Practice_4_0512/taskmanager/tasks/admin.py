from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.

from tasks.models import Project, Task, User, TaskStatus


# admin.site.register(Project)
# admin.site.register(Task)
# admin.site.register(User)
# admin.site.register(TaskStatus)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
  list_display = ('title', 'status', 'due_date', 'project')  # Поля для отображения в списке
  list_filter = ('status', 'project')  # Фильтры в правой части админки
  search_fields = ('title', 'description')  # Поля для поиска
  ordering = ('due_date',)  # Сортировка записей

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
  list_display = ('name', 'description', 'created_at')  # Поля для отображения в списке

@admin.register(User)
class UserAdmin(UserAdmin):
  list_display = ('username', 'email', 'firstname', 'lastname', 'is_staff')
  fieldsets = UserAdmin.fieldsets + (
    ('Дополнительная информация', {'fields': ('firstname', 'lastname')}),
  )

@admin.register(TaskStatus)
class TaskStatusAdmin(admin.ModelAdmin):
  list_display = ('name', 'description')  # Поля для отображения в списке


# Изменение заголовков
#  Вместо стандартного на русском "Администрирование Django"
admin.site.site_header = "Управление проектами"

# Вместо стандартного заголовка на русском " Администрирование сайта|Административный сайт Django"
admin.site.site_title = "Админка Task Manager"
# получим заголовок: "Администрирование сайта|Админка Task Manager"

# Вместо стандартного заголовка на русском " Администрирование сайта|Административный сайт Django"
admin.site.index_title = "Добро пожаловать в Task Manager"
# получим заголовок: "Добро пожаловать в Task Manager|Административный сайт Django"