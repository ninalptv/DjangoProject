from .models import InterestingFacts
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea




class InterestingFactsForm(ModelForm):
    class Meta:
        model = InterestingFacts
        fields = ['title', 'anons', 'full_text', 'date']
        widgets={
            'title':TextInput(attrs={
                'class':'form-control',
                'placeholder':"Факт о чем: ",
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Анонс",
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': "Дата публикации"

            }),
            'full_text':Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Полный текст",
            }),
        }
