from django.apps import AppConfig

# Начало > Tasks > ...
# class TasksConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'tasks'


#  Начало > Задачи и проекты > ...
class TasksConfig(AppConfig):
  default_auto_field = 'django.db.models.BigAutoField'
  name = 'tasks'
  verbose_name = 'Задачи и проекты'  # Название группы в админке

