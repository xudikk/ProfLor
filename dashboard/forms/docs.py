from django import forms

from dashboard.models import Doctor, Patients, Diagnoz, Suggests


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'


# class TabletsForm(forms.ModelForm):
#     class Meta:
#         model = Tablets
#         fields = '__all__'


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
