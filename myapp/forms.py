from django import forms

class createNewTask(forms.Form):
    title = forms.CharField(label = 'titúlo de tarea', max_length=200)
    description = forms.CharField(label = 'Descripción de la tarea',widget=forms.Textarea)

