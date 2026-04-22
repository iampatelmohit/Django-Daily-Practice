from django.contrib import admin
from Student.models import Student
from Student.models import Contact
# Register your models here.
# admin.site.register(Student)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display =('name','age')
    search_fields =('name','city')
    list_filter = ('age','city')
    

admin.site.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display= ('name','message')
    
