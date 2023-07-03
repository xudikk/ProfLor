from django import forms

from dashboard.models import Doctor, Patients, Diagnoz, Suggests, Tablets


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'


class TabletsForm(forms.ModelForm):
    class Meta:
        model = Tablets
        fields = '__all__'


class PatientsForm(forms.ModelForm):
    class Meta:
        model = Patients
        fields = '__all__'


class DiagnozForm(forms.ModelForm):
    class Meta:
        model = Diagnoz
        fields = '__all__'


class SuggestForm(forms.ModelForm):
    class Meta:
        model = Suggests
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        root = kwargs.pop('diagnoz')
        super().__init__(*args, **kwargs)
        self.fields['diagnoz'].initial = root

    def save(self, commit=True):
        instance = super(SuggestForm, self).save(commit=commit)
        return instance
