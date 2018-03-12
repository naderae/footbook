from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):

    class Meta:
        # the fields that we want a user to fill out are available from contrib.auth
        fields = ('username', 'email', 'password1', 'password2')
        # this is just saying that the model belongs to the built-in user model
        model = get_user_model()
    # passing in args and kwargs allows us to recieve any amount of arguments and keyword arguments it wants

    # this wierd function is convention for initializing the forms with special things
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # here we are simply iitializing lebels to every field
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'
