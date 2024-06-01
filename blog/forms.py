from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import *
class UserLogin(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'from-control',
        'placeholder': 'Nickname'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "from-control",
        'placeholder': 'Parol'
    }))


class UserRegister(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'from-control',
        'placeholder': 'Nickname'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "from-control",
        'placeholder': 'Parol'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "from-control",
        'placeholder': 'Parolni tasdiqlang'
    }))
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea({
                'class': "from-control"
            })
        }

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title','content', 'photo', 'category')
        widgets ={
            'title': forms.TextInput(attrs={
                'class': "form-control"
            }),
            'content': forms.Textarea(attrs={
                'class': "form-control"
            }),
            'photo': forms.FileInput(attrs={
                'class': "form-control"
            }),
            'category': forms.Select(attrs={
                'class': "form-control"
            })
        }
