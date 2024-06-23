from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

# class CustomnAuthenticationForm(AuthenticationForm):
#     username = forms.CharField(label="Enter Username or E1mail")
    
#     def clean_username(self):
#         username = self.cleaned_data['username']
#         if '@' in username:
#             UserModel = get_user_model()
            
#             try:
#                 user = UserModel.objects.get(email=username)
#                 return user.username
#             except UserModel.DoesNotExist:
#                 raise forms.ValidationError("No user found with this email address")
#         return username

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')