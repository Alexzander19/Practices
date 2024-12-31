from django.urls import path

from tasks import views


urlpatterns = [
  path('', views.index, name='index'),
  
  path('project/create/',views.project_create,name='project_create'),
  path('projects/', views.projects, name='projects'),
  path('project/<int:project_id>', views.project, name='project'),
 
  path('performers/', views.performers, name='performers'),



  path('signup/', views.signup, name='signup'),
  path('signin/', views.signin, name='signin'),
  path('signout/', views.signout, name='signout'),

  path('tasks/', views.tasks, name='tasks'), 
  path('tasks/create/', views.task_create, name='task_create'),
  path('task/<int:task_id>/', views.task, name='task'),

]