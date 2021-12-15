from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "User Name ..."
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Password..."
            })
    )


class SignupForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "First Name..."
            }))
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Last Name..."
            }))
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "User Name..."
            }))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Email..."
            }))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Password..."
            }))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': "Confirm Password..."
        }))
    dept = forms.CharField(
        required=False,
        widget=forms.Select(
            choices=DeptChoice,
            attrs={
                'class': 'form-control'
            }))
    year = forms.CharField(
        required=False,
        widget=forms.Select(
            choices=YearChoice,
            attrs={
                'class': 'form-control'
            }))
    semester = forms.CharField(
        required=False,
        widget=forms.Select(
            choices=SemChoice,
            attrs={
                'class': 'form-control'
            }))
    enrollment = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Enrollment Number.."
            }))
    education= forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows':'2',
                'placeholder': "Education Details *"
            }))
    
    address= forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows':'2',
                'placeholder': "Home Address *"
            }))

    skill= forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows':'2',
                'placeholder': "Skill *"
            }))
    
    hobby= forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows':'2',
                'placeholder': "Your Hobby *"
            }))
    profilepic = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={
                # 'class': 'custom-file-input',
                'id': "customFile",
                'onchange': "readURL(this);",
                'style': "display: none;"
            }
        ))
    is_cdc = forms.BooleanField(
        required = False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "chk"
            }
        )
    )
    is_teacher = forms.BooleanField(
        required = False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "chk"
            }
        )
    )
    is_student = forms.BooleanField(
        required = False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "chk"
            }
        )
    )
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'dept', 'year', 'semester',
                  'enrollment', 'profilepic','address','skill','education','hobby', 'status', 'is_cdc', 'is_teacher', 'is_student')



class CategoryManagement(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Category Name..."
            }))

    class Meta:
        model = QuestionCategory
        fields = ('name', 'owner','categorytime','is_approve','is_pending','is_reject','remarks')


class QuestionManagement(forms.ModelForm):
    question = forms.Textarea()

    class Meta:
        model = Question
        fields = ('question', 'questioncategory',
                  'owner', 'status', 'postedtime')


class AnswerManagement(forms.ModelForm):
    answer = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'placeholder': "Provide your Answer Hear..."
            }))

    class Meta:
        model = Answer
        fields = ('answer', 'questionid',
                  'solver', 'answertime', 'status')


