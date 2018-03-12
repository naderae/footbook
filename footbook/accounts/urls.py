from django.conf.urls import url
# with this, we do not have to create a login and logout views, which we name auth_views, takes care of this for us
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    # we are using the LoginView and LogoutView, which we didnt create but we just got from contrib.auth as auth_views
    url(r'login/$', auth_views.LoginView.as_view(template_name = 'accounts/login.html'),name='login'),
    url(r'logout/$',auth_views.LogoutView.as_view(),name='logout'),
    url(r'signup/$',views.Signup.as_view(),name='signup'),

]
