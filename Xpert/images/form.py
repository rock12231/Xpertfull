from django import forms
from django.forms import ModelForm
from .models import *

class SliderForm(forms.ModelForm):

    class Meta:
        model = Slider
        fields = '__all__'
