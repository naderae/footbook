from django.conf.urls import url
# with this, we do not have to create a login and logout views, which we name auth_views, takes care of this for us

from . import views

app_name = 'groups'

urlpatterns = [

    url(r"^$",views.ListGroups.as_view(),name="all"),
    url(r"^(?P<slug>[-\w]+)/single/$",views.SingleGroup.as_view(),name="single"),
    url(r"^new/$", views.CreateGroup.as_view(), name="create"),
    url(r"^(?P<username>[-\w]+)/$",views.UsersGroups.as_view(),name="for_user"),
    url(r"join/(?P<slug>[-\w]+)/$",views.JoinGroup.as_view(),name="join"),
    url(r"leave/(?P<slug>[-\w]+)/$",views.LeaveGroup.as_view(),name="leave"),

]
