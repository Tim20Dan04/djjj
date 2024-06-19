# projects/admin.py

from django.contrib import admin
from .models import Supervisor, Status, Technology, Student, Project, ProjectStudents, Comment

admin.site.register(Supervisor)
admin.site.register(Status)
admin.site.register(Technology)
admin.site.register(Student)
admin.site.register(Project)
admin.site.register(ProjectStudents)
admin.site.register(Comment)
