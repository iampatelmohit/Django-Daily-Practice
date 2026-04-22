from django import forms
from .models import Student_create


class StudentForm(forms.ModelForm):
    class Meta:
        model=Student_create
        fields = ['name','age','email']
# we want to applied a validation on age
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age is None:
             raise forms.ValidationError("Please enter a valid age.")

    # Validation logic
        if age < 18:
             raise forms.ValidationError("Age must be at least 18.")
        
        return age
    
 