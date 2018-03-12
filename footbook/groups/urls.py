from django.conf.urls import url
# with this, we do not have to create a login and logout views, which we name auth_views, takes care of this for us

from . import views

app_name = 'groups'

urlpatterns = [

    url(r"^$",views.ListGroups.as_view(),name="all"),
    url(r"^(?P<slug>[-\w]+)/single/(?P<pk>\d+)/$",views.SingleGroup.as_view(),name="single"),


]
