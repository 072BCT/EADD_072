from django import forms
from django.contrib.auth.forms import UserCreationForm

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = '__all__'
from WebApp.models import Member


class UserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Member
        fields = ('username', 'email',)


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('username', 'email')


class UserUpdateFormForAdmin(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
