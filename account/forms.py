from django import forms

class SignIn(forms.Form):
    username            = forms.CharField(min_length=3, widget=forms.TextInput(attrs= {'class':'form-control','placeholder':'Username',} ))
    password            = forms.CharField( widget= forms.PasswordInput(attrs= {'class':'form-control','placeholder':'Password' }))
   
class SignUp(forms.Form):
    username            = forms.CharField(widget=forms.TextInput( attrs={'class' : 'form-control', 'placeholder': 'Username'}))
    email               = forms.CharField(required=True, widget=forms.TextInput( attrs={'class' : 'form-control', 'placeholder': 'Email', 'onkeyup':'check_mail()' }))
    password            = forms.CharField(widget=forms.PasswordInput( attrs={'class' : 'form-control', 'onkeyup':'check()', 'placeholder': 'Password'}))
    confirm_password    = forms.CharField(widget=forms.PasswordInput( attrs={'class' : 'form-control', 'onkeyup':'check()', 'placeholder': 'Confirmation Password'}))

class forgotPass(forms.Form):
    username            = forms.CharField(min_length=3, widget=forms.TextInput(attrs= {'class':'form-control','placeholder':'Username',} ))

class resetPass(forms.Form):
    password            = forms.CharField(widget=forms.PasswordInput( attrs={'class' : 'form-control pass_cek', 'placeholder': 'Password'}))
    confirm_password    = forms.CharField(widget=forms.PasswordInput( attrs={'class' : 'form-control  border-light pass_cek', 'placeholder': 'Confirmation Password'}))
