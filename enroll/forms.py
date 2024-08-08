from django import forms
from .models import User

class UserRegistration(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('name','email','password')
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','id':'nameid','style':'border-bottom :double; border-bottom-color:black'}),
            
            'email':forms.EmailInput(attrs={'class':'form-control','id':'emailid','style':'border-bottom :double; border-bottom-color:black'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','id':'passwordid','style':'border-bottom :double; border-bottom-color:black'})
            
        }
