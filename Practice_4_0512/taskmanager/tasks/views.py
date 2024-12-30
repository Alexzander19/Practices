import re
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Project, Task, User
from .forms import ProjectAddForm

# Create your views here.

def index(request):
  return render(request, 'tasks/index.html')

def projects(request):
  projects_list = Project.objects.all()
  return render(request, 'tasks/projects.html', context={'projects': projects_list})

def performers(request):
  performers_list = User.objects.all()
  return render(request, 'tasks/performers.html', context={'performers': performers_list})

def tasks(request):
  tasks_list = Task.objects.all()
  return render(request, 'tasks/tasks.html', context={'tasks': tasks_list})

def project(request, project_id):
  project_view = Project.objects.get(pk=project_id)
  tasks_list = Task.objects.filter(project_id=project_id)
  return render(request, 'tasks/project.html', context={'project': project_view, 'tasks': tasks_list})

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



def project_create_form(request):
  if request.method == "POST":
    form = ProjectAddForm(data=request.POST)
    if form.is_valid():
      form.save()
      return redirect('index')
  else:
      form = ProjectAddForm()

  return render(request, "tasks/project_create.html", {"form": form})