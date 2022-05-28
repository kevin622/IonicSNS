from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import EmailField
from django.contrib.auth import get_user_model
User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    email = EmailField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

class CustomUserChangeForm(UserChangeForm):
    email = EmailField(required=True)
    class Meta(UserChangeForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)