from django.contrib.auth.forms import UserChangeForm , UserCreationForm
from .models import CustomUser


class CustomeUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('picture','acsses')
        
class CustomeUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
        