from django import forms
from django.core.exceptions import ValidationError
from .models import studentModel

class StudentForms(forms.ModelForm):
    class Meta:
        model = studentModel
        fields = "__all__"

    def clean_rno(self):
        rno = self.cleaned_data.get('rno')
        if rno < 1:
            raise ValidationError('Roll number should be minimum 1')
        return rno

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name.isalpha():
            raise ValidationError('Name should contain only alphabets')
        if len(name) < 2:
            raise ValidationError('Name should have a minimum of 2 characters')
        return name

    def clean_marks(self):
        marks = self.cleaned_data.get('marks')
        if marks < 0 or marks > 100:
            raise ValidationError('Marks should be between 0 and 100')
        return marks