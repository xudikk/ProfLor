from django import forms

from dashboard.models import Doctor, Tablets, Patients


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

