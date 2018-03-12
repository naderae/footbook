from django.conf.urls import url
# with this, we do not have to create a login and logout views, which we name auth_views, takes care of this for us
from django.contrib.auth import views as auth_views
from . import views

app_name = 'posts'

urlpatterns = [

    url(r"^(?P<slug>[-\w]+)/posts/$",views.PostList.as_view(),name="all"),
    url(r"^(?P<slug>[-\w]+)/posts/(?P<pk>\d+)/$",views.PostDetail.as_view(),name="single"),



]
