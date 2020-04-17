from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from djangoapp.models import Computer
class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = '__all__'

    # def clean_computer_name(self):
    #     computer_name = self.cleaned_data.get('computer_name')
    #     if(computer_name == ''):
    #         raise forms.ValidationError("This Filed Cannot be Left Blank")
    #     return computer_name
    #
    # def clean_IP_address(self):
    #     IP_address = self.cleaned_data.get('IP_address')
    #     if (IP_address == ''):
    #         raise forms.ValidationError("This Filed Cannot be Left Blank")
    #     return IP_address

class ComputerSearchForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ['computer_name','users_name','export_to_CSV']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']

