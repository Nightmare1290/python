from django import forms
from .models import concursoImage, promocionImage


class UploadConcursoImageForm(forms.ModelForm):
    class Meta:
        model = concursoImage
        fields = ['concurso','image']


class UploadPromocionImageForm(forms.ModelForm):
    class Meta:
        model = promocionImage
        fields = ['promocion', 'image']