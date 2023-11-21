from django.shortcuts import render,redirect
from .models import Post
# Create your views here.
# ======================= create crud opertions bf class based view ===============
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

class Post_list(ListView):                                      # context in templates  name of model _list    post_list  object_list
    model=Post                                                  # template name     name of model_action       post_list

class Post_detail(DetailView):                                  # context in template name of model            post   object    
    model=Post                                                  # name of template   name of modes _action     post_detail

class Create_post(CreateView):
    model=Post
    fields='__all__'
    success_url='/posts/'
    template_name='posts/create.html'
class Update_post(UpdateView):
    model=Post
    fields='__all__'
    success_url='/posts/'
    template_name='posts/edit.html'
class Delete_post(DeleteView):
    model=Post
    success_url='/posts/'
    template_name='posts/delete.html'