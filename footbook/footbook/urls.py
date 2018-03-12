"""footbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include
from . import views

urlpatterns = [

    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^test/$', views.TestPage.as_view(), name='test'),
    url(r'^thanks/$', views.ThanksPage.as_view(), name='thanks'),
    url('admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls',namespace='accounts')),
    # this allows us to connect to all the authorization stuff django does for us
    url(r'^accounts/',include('django.contrib.auth.urls')),

    url(r'^posts/', include("posts.urls", namespace="posts")),
    url(r"^groups/",include("groups.urls", namespace="groups")),
]


]