from django.urls import path
from . import views

urlpatterns = [ 
        # path('',views.contact_form, name = 'contact'),
        path('submit/',views.submit_contact, name= 'submit_contact'),
        path('add/',views.student_create, name='student_create'),
        path('',views.student_list,name='student_list'),
        path('edit/<int:pk>/',views.student_edit,name='student_edit'),
        path('delete/<int:pk>/',views.student_delete,name='student_delete'),
        ]