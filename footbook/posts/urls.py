from django.conf.urls import url
# with this, we do not have to create a login and logout views, which we name auth_views, takes care of this for us
from django.contrib.auth import views as auth_views
from . import views

app_name = 'posts'

urlpatterns = [

    url(r"^(?P<slug>[-\w]+)/$",views.PostList.as_view(),name="all"),
    url(r"^(?P<pk>\d+)/(?P<slug>[-\w]+)/$",views.PostDetail.as_view(),name="single"),
    url(r"^(?P<slug>[-\w]+)/new/$", views.CreatePost.as_view(), name="create"),




]
