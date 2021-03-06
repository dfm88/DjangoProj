from django import forms
from .models import Lead
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model


User = get_user_model()


class LeadForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)


class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ('first_name',
                  'last_name',
                  'age',
                  'agent',
                  )


class CustomUserCreationForm(UserCreationForm):
    # COPIED FROM built in UserCreationForm
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}
