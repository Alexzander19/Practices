import re
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import TaskCreateForm, TaskForm

from .models import Project, Task, TaskStatus, User


# Create your views here.

def index(request):
  return render(request, 'tasks/index.html')

def projects(request):
  projects_list = Project.objects.all()
  return render(request, 'tasks/project/projects.html', context={'projects': projects_list})

def performers(request):
  performers_list = User.objects.all()
  return render(request, 'tasks/performers.html', context={'performers': performers_list})

def tasks(request):
  tasks_list = Task.objects.all()
  return render(request, 'tasks/task/tasks.html', context={'tasks': tasks_list})

def project(request, project_id):
  project_view = Project.objects.get(pk=project_id)
  tasks_list = Task.objects.filter(project_id=project_id)
  return render(request, 'tasks/project/project.html', context={'project': project_view, 'tasks': tasks_list})

def user_create(request):
  if request.method == "POST":
    username = request.POST.get("username")
    email = request.POST.get("email")
    
    # Валидация данных (например, емени проверка email)
    # буква, цифра или _, от 4 до 10 символов
    pattern = r'\w{4,10}' 
    
    # проверяем, соответствует ли строка шаблону
    if not re.fullmatch(pattern, username):
      return HttpResponse('Имя введено некорректно.')
    
    # проверяем, соответствует ли email шаблону (Хотя HTML итак не дает пройти с неккоректным email)
    regex_email = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")

    if not re.fullmatch(regex_email, email):
      return HttpResponse('email введен некорректно.')
 
      
    if not username or not email:
      return HttpResponse("Ошибка: Все поля обязательны для заполнения.")
    
    try:
      user = User(username=username, email=email)
      user.save()
    except:
      return HttpResponse(f"Данные получены НО не записаны: {username}, {email}")
    
    return HttpResponse(f"Данные получены И ЗАПИСАНЫ {username}, {email}")
    
  return render(request, "tasks/user_create.html")



def project_create(request):
  
  if request.method == 'POST':
      name = request.POST['name']
      description = request.POST['description']
      project_view = Project.objects.create(name=name, description=description)
      return redirect('project', project_view.id)
  
  return render(request, 'tasks/project/create.html')


def task_create(request):
  if request.method == "POST":
    form = TaskCreateForm(request.POST)
    if form.is_valid():
      # form.save()  # В случае если не нужно изменять сущность задачи
      task = form.save(commit=False)
      task.status = TaskStatus.objects.get(id=1)
      task.save()
      return redirect('tasks')
  else:
    form = TaskCreateForm()
  
  projects_list = Project.objects.all()
  return render(request, 'tasks/task/create.html', context={'form': form, 'projects': projects_list})


def task(request, task_id):
  task_view = Task.objects.get(pk=task_id)  # Получаем объект Task по первичному ключу
  if request.method == "POST":
    form = TaskForm(request.POST, instance=task_view)  # Передаём существующий объект в форму
    if form.is_valid():
      form.save()
      return redirect('tasks')
  else:
    form = TaskForm(instance=task_view)  # Предзаполняем форму текущими данными
  return render(request, 'tasks/task/details.html', {'form': form, 'task': task})
