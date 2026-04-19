from django.contrib import admin
from Student.models import Student
# Register your models here.
# admin.site.register(Student)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display =('name','age')
    search_fields =('name','city')
    list_filter = ('age','city')

