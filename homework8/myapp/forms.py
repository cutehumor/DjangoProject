from django import forms

class UploadForm(forms.Form):
    img = forms.ImageField(label='添加图片')
    