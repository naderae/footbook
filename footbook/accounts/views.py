from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms

# u only need the write the logic for the sinup form, the login and logout is taken care of by django. in URLS.py we create the login and logout views, and django creates the the forms.
class Signup(CreateView):
    form_class = forms.UserCreateForm
    #we use revere_lazy when we want to redirect after they submit. reverse alone redirects when they hit that page.
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"
