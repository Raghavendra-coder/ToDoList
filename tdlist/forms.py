from django import forms
from .models import todoList


class ToDoListForm(forms.ModelForm):
    class Meta:
        model = todoList
        fields = ('title', 'start_date', 'com_date', 'content')
        widgets = {
            'start_date' : forms.TextInput(attrs={'type': 'date'}),
            'com_date': forms.TextInput(attrs={'type': 'date'}),

            'title': forms.TextInput(attrs={'placeholder': 'Title...'}),
        }



