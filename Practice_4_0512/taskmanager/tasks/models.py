from django.db import models

# Create your models here.



class Project(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
      return self.name


class User(models.Model):
  username = models.CharField(max_length=100)
  email = models.EmailField()
  
  def __str__(self):
      return self.username

class TaskStatus(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()

  def __str__(self):
    return self.name
 



   

class Task(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField()
  status = models.CharField(max_length=100)
  # status = models.ForeignKey(TaskStatus,default=lambda: TaskStatus.objects.get(id=1), on_delete=models.DO_NOTHING)
  # ValueError: Cannot serialize function: lambda потому, что возвращает self.name (__str__)
  # все-равно не дает, так как уже есть значения поля status
  # Пришлось удалять все файлы миграций и сам файл БД
  # и делать все миграции заново, в том числе создавать супер Юзера.
  status = models.ForeignKey(TaskStatus, on_delete=models.DO_NOTHING)
  created_at = models.DateTimeField(auto_now_add=True)
  due_date = models.DateField()
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  performers = models.ManyToManyField(User)
  
  def __str__(self):
      return f'{self.title} ({self.status})'