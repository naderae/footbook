from django.contrib import messages
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)

from django.urls import reverse
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
# genetic gives you access to the class based views.
from django.views import generic
from groups.models import Group
from . import models

# Create your views here.

class CreateGroup(LoginRequiredMixin,generic.CreateView):
    model = Group
    fields = ('name', 'description')

class SingleGroup(generic.DetailView):
    model = Group

class ListGroups(generic.ListView):
    model = Group

class UsersGroups(LoginRequiredMixin, generic.ListView):
    model = models.Group
    template_name = 'groups/user_group_list.html'

    def get_queryset(self):
        return Group.objects.filter(user=self.request.user).order_by('name')






class JoinGroup(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        # it seems that self.kwargs access url parameters, similar to params hash
        return reverse('groups:single',kwargs={'slug': self.kwargs.get('slug')})


    def get(self,request,*args,**kwargs):
        # again, we need to get the group name from the url, which is found in self.kwargs
        group = get_object_or_404(Group, slug=self.kwargs.get('slug'))

        # condition that raises the error
        try:
            # self.request.user is how you grab the user that is logged in
            GroupMember.objects.create(user=self.request.user, group=group)
        except:
            messages.warning(self.request, "You are already a Member of the {} group!" ).format(group.name)
        else:
            messages.success(self.request, "Welcome! You are now a Member of the {} group".format(group.name))
        return super().get(request,*args,**kwargs)

class LeaveGroup(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        # it seems that self.kwargs access url parameters, similar to params hash
        return reverse('groups:single',kwargs={'slug': self.kwargs.get('slug')})


    def get(self,request,*args,**kwargs):

        # condition that raises the error
        try:
            # you shouldnt be able to leave a group if you rnot already in it
            membership = models.Groupmember.objects.filter(
                user = self.request.user,
                # Basic lookups keyword arguments take the form field__lookuptype=value. (That’s a double-underscore).
                #  this is different, its not a lookup.
                # an underscore refers to a relationship, so this means a groups slug is what it gets from the url
                group__slug = self.kwargs.get('slug')
            ).get()

        except models.Groupmember.DoesNotExist:
            messages.warning(self.request, "You are not a member of group {} yet!" ).format(group.name)
        else:
            messages.success(self.request, "You have just left {} group".format(group.name))
        return super().get(request,*args,**kwargs)
