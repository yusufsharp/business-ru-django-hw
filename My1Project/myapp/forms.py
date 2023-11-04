from django import forms
from myapp.models import User


class MyProfileForm(forms.ModelForm):
    GENDER_CHOICES = (('Парень', 'Парень'), ('Парень', 'Девушка'),)
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'id': 'inputFile',
        'accept': 'image/*',
    }))

    name_surname = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input error',
        'id': 'inputName',
    }))
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect(attrs={
            'class': 'radio-label',
        }),)
    birth_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={
        'class': 'input',
        'id': 'inputDate',
        'placeholder': '2023-11-03',
    }))
    telegram = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input',
        'placeholder': 'Телеграм',
    }))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input',
        'placeholder': '+7 901 123 45 67',
    }))
    about = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 40, 'class': 'input', }))

    class Meta:
        model = User
        fields = '__all__'
