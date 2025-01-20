from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class Project(models.Model):
  # name = models.CharField(max_length=100)
  # description = models.TextField()
  # created_at = models.DateTimeField(auto_now_add=True)
  class Meta:
    verbose_name = 'проект' # для одного проекта
    verbose_name_plural = 'проекты'  # для нескольких проектов

  name = models.CharField(max_length=100, verbose_name='Название')
  description = models.TextField(verbose_name='Описание')
  created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
  
  def __str__(self):
      return self.name


class User(AbstractUser):
  # username = models.CharField(max_length=100)
  # firstname = models.CharField(max_length=100)
  # lastname = models.CharField(max_length=100)
  # email = models.EmailField() # в классной этого поля нет. попробуем убрать. Может оно есть в AbstractUser
  #  ДЕйствительно, поле в базе данных есть. Но оно доступно только через нашу форму регистрации.
  # При создании пользователя через админку поля email нету.
  # Но после создания пользователя через админку есть возможность указать email
  class Meta:
    verbose_name = 'пользователь'
    verbose_name_plural = 'пользователи'

  firstname = models.CharField(max_length=100, verbose_name='Имя')
  lastname = models.CharField(max_length=100, verbose_name='Фамилия')
  
  def __str__(self):
      return self.username


class TaskStatus(models.Model):
  # name = models.CharField(max_length=100)
  # description = models.TextField()

  class Meta:
    verbose_name = 'статус задачи'
    verbose_name_plural = 'статусы задачи'
  name = models.CharField(max_length=100, verbose_name='Название')
  description = models.TextField(verbose_name='Описание')

  def __str__(self):
    return self.name
 



   

class Task(models.Model):
  # title = models.CharField(max_length=100)
  # description = models.TextField()
  # status = models.CharField(max_length=100)
  # status = models.ForeignKey(TaskStatus, on_delete=models.DO_NOTHING)
  # created_at = models.DateTimeField(auto_now_add=True)
  # due_date = models.DateField()
  # project = models.ForeignKey(Project, on_delete=models.CASCADE)
  # performers = models.ManyToManyField(User)
  
  class Meta:
      verbose_name = 'задача'
      verbose_name_plural = 'задачи'

  title = models.CharField(max_length=100, verbose_name='Название')
  description = models.TextField(verbose_name='Описание')
  status = models.ForeignKey(TaskStatus, on_delete=models.PROTECT, verbose_name='Статус')
  # Что он будет делать при удалении, если on_delete=models.PROTECT?
  # on_delete=models.PROTECT в Django запрещает удаление записи из 
  # первичной модели, если она используется во вторичной. При этом 
  # выдаётся  исключение. Этот параметр  используется, когда  нужно 
  # обеспечить, чтобы удаляемый объект не мог быть удалён, пока 
  # есть зависимые объекты. 

  created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создана')
  due_date = models.DateField(verbose_name='Срок выполнения')
  project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Проект')
  performers = models.ManyToManyField(User, verbose_name='Исполнители')

  def __str__(self):
      return f'{self.title} ({self.status})'