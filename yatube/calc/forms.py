from django.db import models
from django.forms import ModelForm
from .models import Bb


class BbForm(ModelForm):

    class Meta:
        model = Bb
        fields = ('ammount', 'comment', 'published')
