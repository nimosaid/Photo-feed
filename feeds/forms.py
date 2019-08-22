from django import forms
from .models import Feeds

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Feeds
        fields = ('description', 'document', )