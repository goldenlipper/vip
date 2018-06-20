from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from vips.models import GlUser


class RegistrationForm(UserCreationForm):
    sex_choices = (
        ('unknown', 'unknown'),
        ('m', 'male'),
        ('f', 'female'),
    )
    address = forms.CharField(max_length=100, required=True)
    sex = forms.ChoiceField(choices=sex_choices, required=True)
    birthday = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    contact = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ('username',
                  'password1',
                  'password2',
                  'first_name',
                  'last_name',
                  'address',
                  'sex',
                  'birthday',
                  'email',
                  'contact',
                  )



class EditProfileForm(UserChangeForm):
    class Meta:
        model = GlUser
        fields = ('GL_customer',
                  'GL_customer',
                  'GL_address',
                  'GL_sex',
                  'GL_birthday',
                  'GL_email',
                  )
