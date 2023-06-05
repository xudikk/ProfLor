from django import forms

from dashboard.models import New


class NewsForm(forms.ModelForm):
    class Meta:
        model = New
        fields = '__all__'

