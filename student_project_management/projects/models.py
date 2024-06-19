from datetime import date
from django.db import models

class Supervisor(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Technology(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    enrollment_date = models.DateField(default=date.today)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField(default=date.today())
    end_date = models.DateField(default=date.today())
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=None)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE, default=None)
    technologies = models.ManyToManyField(Technology)
    students = models.ManyToManyField(Student, through='ProjectStudents')

    def __str__(self):
        return self.title

class ProjectStudents(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    assigned_date = models.DateField()

    def __str__(self):
        return f'{self.project.title} - {self.student.first_name}'

class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.first_name} on {self.project.title}'
