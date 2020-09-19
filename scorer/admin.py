from django.contrib import admin
# Register your models here.
from .models import Teacher, Student

admin.site.site_header = "Scorer Admin"
admin.site.site_title = "Scorer Admin Portal"
admin.site.index_title = "Welcome to The Scorer Admin"

admin.site.register(Teacher)
admin.site.register(Student)