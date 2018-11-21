from django import forms

class UploadFile(forms.Form):
    csv_file=forms.FileField()