from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.http import Http404
from django.views import generic
from django.views.generic.list import ListView

from braces.views import SelectRelatedMixin

# from . import forms
from . import models

from django.contrib.auth import get_user_model
# we use this below to check that the person on the site
User = get_user_model()

# Create your views here.

# e = Post.objects.select_related('group').get(pk=5)
# select_related will simply grab the objects that are related to the post, and keeps them prepopulated so you dnt have to query the databse again.
# now you can call b = e.group without querying the database again
# this is what selectrealtedmixin does, it prepopulates the associated objects
# it does not return the related object, iut gives you access to it without having to query the databse again
class PostList(SelectRelatedMixin, ListView):
    model = models.Post
    select_related = ('user', 'group')

    template_name = 'groups/group_detail.html'

class PostDetail(SelectRelatedMixin, generic.DeleteView):
    model = models.Post
    select_related = ('user', 'group')

    def get_queryset(self):
        #get the queryset for the post
        queryset = super().get_queryset()

        return queryset.filter(
        # here, group__slug refers to the group's slug. remember, __ can be used to refer to relations.
        # the second __ refers to the querying, and it what follows is the search type(iexact).
            group__slug__iexact=self.kwargs.get("slug")
        )
class CreatePost(LoginRequiredMixin, generic.CreateView, SelectRelatedMixin):
    # here, we track the group that the post is for by adding it as a field
    fields = ('title','content')
    model = models.Post

    # template_name = 'posts/post_form.html'

    # just to check if the form is valid
    #  this also connects the post to the user that made the request
    def form_valid(self, form):
        self.object = form.save(commit=False)
        # connect the post to the user
        self.user = self.request.user
        # connect the post to the group
        # self.group = 

        self.object.save()
        return super().form_valid(form)

class DeletePost(LoginRequiredMixin,SelectRelatedMixin,generic.DeleteView):
    model = models.Post
    select_related = ('user', 'group')
    success_url = reverse_lazy('posts:all')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id = self.request.user.id)

    def delete(self,*args,**kwargs):
        messages.success(self.request, "Post Deleted")
        return super().delete(*args, **kwargs)
