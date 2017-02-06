from django.forms import ModelForm
from django.contrib.auth.models import User

from Desktop.collectivework.userprofile.models import UserProfile


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['email','username','passwords']
        labels = {
            'email' : 'Eposta',
            'username' : 'Kullanıcı Adı',
            'password' : 'Parola',
        }
        widgets = {
            'email' : forms.TextInput(attrs={
                'placeholder' : 'E-posta',
            }),
            'username' : forms.TextInput(
                attrs={
                    'placeholder': 'KullaniciAdi',
                }
            ),
            'password' : forms.PasswordInout(
                attrs={
                    'placeholder': 'Parola',
                }
            ),
        }

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profilephoto']
        labels = {
            'profilephoto': "Profil Fotografi"
        }