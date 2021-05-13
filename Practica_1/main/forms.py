from django import forms
from django.forms import FileField

from .models import UploadedFiles

class FileForm(forms.ModelForm):
    class Meta:
        model = UploadedFiles
        fields = ['title','p2']

    def clean_p2(self):
        p2 = self.cleaned_data.get('p2')
        rev = p2.name[::-1]
        if rev[0:3] == '2p.':
            return p2

        raise forms.ValidationError('Su archivo debe terminar en .p2')

    def save(self, commit=True, user=None):
        upload = super(FileForm, self).save(commit=False)

        if commit:
            upload.user = user
            upload.save()

        return upload

class EditForm(forms.Form):
    title = forms.CharField(max_length=100)
    contenido = forms.CharField(widget=forms.Textarea)


